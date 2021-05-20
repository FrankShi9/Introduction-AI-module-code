import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse
import requests

class Blockchain(object):
    def __init__(self):#constructor
        self.chain=[]
        self.current_transactions = []
        #create the genesis block
        self.new_block(previous_hash=1, proof=100)
        self.nodes = set()

    def new_block(self):
        #Creates a new Block and adds it to the chain
        pass

    def new_transaction(self):
        #Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        #Returns the last Block in the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        生成新交易信息，信息将加入到下一个待挖的区块中
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append(
            {'sender': sender, 'recipient':recipient, 'amount':amount }

        )

        return self.last_block['index'] + 1


    def new_block(self, proof, previous_hash):#last optional param
        """
        生成新块
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = { #a dict
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof':proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        #Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1] #反向索引

    @staticmethod
    def hash(block):
        """
        生成块的 SHA-256 hash值
        :param block: <dict> Block
        :return: <str>
        """
        # !! We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        简单的工作量证明:
         - 查找一个 p 使得 hash(p'p) 以4个0开头
         - p' 是上一个块的证明,  p 是当前的证明
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        验证证明: 是否hash(last_proof, proof)以4个0开头?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode() #utf-8
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000" #return a bool

    def register_node(self,address):
        """
        Add a new node to the list of nodes
        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False
            # Check that the Proof of Work is correct
            if not self.valid_proof((last_block['proof'], block['proof'])):
                return False

            last_block = block
            current_index += 1
        return True

    def resolve_conflicts(self):
        """
        共识算法解决冲突
        使用网络中最长的链.
        :return: <bool> True 如果链被取代, 否则为False
        """
        neighbors = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_len = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbors:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                len = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if len > max_len and self.valid_chain(chain):
                    max_len = len
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain: #not None
            self.chain = new_chain
            return True
        return False


# Instantiate our Node app
app = Flask(__name__)

# Generate a globally unique address for this node:miner node
node_identifier = str(uuid4()).replace('-','')

# Instantiate the Blockchain
blockchain = Blockchain()



'''
@app.route('/mine', methods=['GET'])
def mine():
    return "We're gonna mine a new Block :)"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll make a new transaction :)"
'''

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200 #return http 200 success in handling requests

@app.route('/transactions/new', methods=['POST'])#point to the specific interface
def new_transaction():
    values = request.get_json()

    #Check that the required fields are in the POST'ed data
    required = ['sender','recipient','amount']
    if not all(k in values for k in required):
        return 'Sorry, values missing', 400 #return more than one value

    #create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():

    # We run the proof of work algorithm to get the next proof
    last_block = blockchain.chain[-1]
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # 给工作量证明的节点提供奖励.
    # 发送者为 "0" 表明是新挖出的币
    blockchain.new_transaction(
        sender='0',
        recipient=node_identifier, #uuid of the miner node
        amount = 1
    )

    # Forge the new Block by adding it to the chain
    block = blockchain.new_block(proof, None)

    response = {# a dict
        'message': "Kudos! A brand new block is forged:)",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == "__main__":
    #blockchain = Blockchain()
    #print(blockchain.last_block())
    # change host here!!
    app.run(host = '192.168.1.106', port=5000)


import csv
import numpy as np
import random
from random import shuffle

csv_file_path = open('binary_data.csv') # set the file relative path
csv_reader = csv.reader(csv_file_path, delimiter=',') # instantiate a csv_reader

binary_data = np.zeros([100,6],dtype=int)  # the matrix used to store the binary data
N = 100  # This is the same N as specified in the task sheet

def load_file_mat(input):
    """
    loadFiletoMat() function loads the data from .csv file to the numpy matrix

    :param: input: matrix where the data will be stored
    :return void
    """
    cnt = 1
    col,row = 0,0
    while (True):
        tmp = []
        try:
            tmp.append(csv_reader.__next__())
            for ele in tmp[0]:
                input[row][col] = int(ele)
                col+=1

            row += 1
            col = 0
        except StopIteration:
            #print('loading stopped at row {}'.format(cnt - 1))
            break

        cnt += 1


def cnt_l(l: int, input):
    """
    cnt_l() function counts the given l value: 0/1 within the binary data

    :param: l: value of l to be counted, input: matrix where the data will be read
    :return cnt_of_l: total count number of l with value l in the binary data
    """
    cnt_of_l = 0
    for index in range(0, 100):
        if input[index][5] == l:
            cnt_of_l += 1

    return cnt_of_l


def prior_pro(l: int):
    """
    prior_pro() function calculates the prior probability of l
    with value: 0/1 within the binary data

    :param: l: value of l to be calculated
    :return: prior probability of l = k
    """
    if(l==1):
        return (l1 / N) # uses prestored count of l=1 to save time
    else:
        return (l0 / N) # uses prestored count of l=0 to save time


def cnt_a(i: int, a: int, l: int, input):
    """
    cnt_a() function counts the occurrences of a(i)=a (i,a given as parameters)
    with l being value: l (l given as parameter) within the binary data

    :param: i: the subscript of a as the same in the task sheet
          a: the value of a(i)
          l: value of l
          input: matrix where the data will be read
    :return: cnt_of_a: total count number of a(i) with value l=j in the binary data
    """
    cnt_of_a = 0
    for index in range(0, 100):
        if input[index][i] == a and input[index][5] == l:
            cnt_of_a += 1
    return cnt_of_a


def condi_pro(i: int, a: int, l: int, input):
    """
    condi_pro() function calculates the conditional probability

    :param: i: the subscript of a as the same in the task sheet
          a: the value of a(i)
          l: value of l
          input: matrix where the data will be read
    :return: conditional probability
    """
    if(l==0):
        return ((cnt_a(i, a, l, input) / l0))
    else:
        return ((cnt_a(i, a, l, input) / l1))

def random_split():
    shuffle(list(binary_data))
    train, test = binary_data[:len(binary_data)*0.7], binary_data[len(binary_data)*0.7:]
    return train, test

def accuracy(result, test):
    return (result[:][-1] == test[:][-1])/len(test)

# main
if __name__ == '__main__':
    load_file_mat(binary_data)
    result = []
    train, test = random_split()

    #prior probability:
    l0 = cnt_l(0, binary_data)
    l1 = cnt_l(1, binary_data)
    print('p(l={})={}'.format(0, prior_pro(0)))
    print('p(l={})={}'.format(1, prior_pro(1)))

    for i in range(0, 5):
        print('p(a{}={}|l={})={}'.format(i, 0, 1, condi_pro(i, 0, 1, binary_data)))

    for i in range(0, 5):
        print('p(a{}={}|l={})={}'.format(i, 1, 1, condi_pro(i, 1, 1, binary_data)))


    result.append(np.argmax())
















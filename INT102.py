#import numpy as np
import math
import queue

graph = [
         {0:0,'h':0,0:0,'j':0},
         {'g':0,0:0,'i':0,0:0},
         {0:0,'h':0,0:0,'j':0},
         {'g':0,0:0,'i':0,0:0}
         ]

map = {'g':0, 'h':1, 'i':2, 'j':3}

cnt = 0

def BFS():
    for ele in graph:
        for i in ele.keys():
            if i != 0:
                if ele.get(i) == 0:
                    bfs(i)

count = 0
bfsQ = queue.Queue

def bfs(input:str):
    global count
    count += 1
    bfsQ.put(input)

    while bfsQ.empty() != True: #not empty
        buf = bfsQ.get()







def DFS():
    for ele in graph:
        for key in ele.keys():
            if key != 0:
                if ele.get(key) == 0:
                    dfs(key)

def dfs(input):
    global cnt
    cnt += 1
    index = map.get(input)

    for ele in graph[index]:
        for key in ele.keys():
            if key != 0:
                if ele.get(key) == 0:
                    dfs(key)

#adjacency list for an undirected graph to be input for PRIM's algorithm
prim_graph = [
                [0,1,1,1],
                [1,0,0,1],
                [1,0,0,1],
                [1,1,1,0]
             ]
# print(prim_graph)

vertices = set({1,2,3,4})
edges = {'12':1,'13':1,'14':1, '24':1, '34':1}
# print(type(vertices))
# print(vertices)

def prim():
    buf_edge_w = math.inf #infinity
    start = 1
    for ele in vertices:
        if ele != start:
            for i in range(0,4):
                if prim_graph[ele-1][i] == 1:
                    buf = edges.get('{}{}'.format(ele,i+1))
                    if buf < buf_edge_w:
                        buf_edge_w = buf

def cnt_uni(input):
    result = []
    for ele in input:
        if ele not in result:
            result.append(ele)
    return result


def counting_sort(input):
    B = [0 for i in range(0,len(input))] #result
    unique = cnt_uni(input)
    C = [0 for i in range(0,len(unique))]

    for j in range (0,len(input)):
        C[input[j]] += 1 #cnt of each ele in input

    for i in range (1,len(unique)): # 2-1=1
        C[i]+=C[i-1]

    for j in range(len(input, 0)):
        B[C[input[j]]] = input[j]
        C[input[j]] -= 1

    return B


kruskal_sorted_list = {('d','f'):14, ('b','h'):11, ('f','e'):10 ,('d','e'):9 ,('a','h'):8 ,('b','c'):8 ,('h','i'):7 ,('c','d'):7 ,('c','f'):4,
                       ('a','b'):4 ,('g','f'):2,('i','c'):2, ('h','g'):1}

def kruskal():
    visited = {('h','g'):1}
    kruskal_sorted_list.popitem()
    while len(kruskal_sorted_list) != 0:
        buf = kruskal_sorted_list.popitem()
        visited.update(buf)
        if cycle_check(visited) != False:
            visited.pop(buf)

def cycle_check(input)->bool:
    #use dfs here
    DFS()


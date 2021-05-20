import csv

import numpy as np

csv_file_path = open('binary_data.csv')

csv_reader = csv.reader(csv_file_path, delimiter=',')

binary_data = np.zeros([100,6],dtype=int)

N = 100

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

load_file_mat(binary_data)

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

l0 = cnt_l(0,binary_data)
l1 = cnt_l(1,binary_data)

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
        return ((cnt_a(i, a, l, input) / l1)




print('shape of the matrix: ', np.shape(binary_data))
print(binary_data)

print('----------------------------------')  # separator

# store the vars here to achieve dynamic programming


    # print the results of the two prior probabilities
    print('p(l={})={}'.format(0, prior_pro(0)))  # output: 'p(l=0)=k' for instance

    print('p(l={})={}'.format(1, prior_pro(1)))  # output: 'p(l=1)=k' for instance

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=0|l=0)=k' for instance
        print('p(a{}={}|l={})={}'.format(i, 0, 0, condi_pro(i, 0, 0, binary_data)))

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=1|l=0)=k' for instance
        print('p(a{}={}|l={})={}'.format(i, 1, 0, condi_pro(i, 1, 0, binary_data)))

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=0|l=1)=k' for instance
        print('p(a{}={}|l={})={}'.format(i, 0, 1, condi_pro(i, 0, 1, binary_data)))

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=1|l=1)=k' for instance
        print('p(a{}={}|l={})={}'.format(i, 1, 1, condi_pro(i, 1, 1, binary_data)))

    print('----------------------------------')
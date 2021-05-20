import csv
import numpy as np


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

#changed here
def document_fre(i: int, a: int , l: int, input):
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

#new here

def Pc(l:int):
    return prior_pro(l)

def Pw(w:int):
    return cnt_a(w,1,1,binary_data)+cnt_a(w,1,0,binary_data)

def Pcw(w,l):
    return document_fre(w, 1, l, binary_data)

def Pc_neg_w(w,l):
    return document_fre(w, 0, l, binary_data)

def IG(word):
    sum1 = -(Pc(0)*np.log2(Pc(0)) + Pc(1)*np.log2(Pc(1)))
    PW = Pw(word)
    PW_neg = 1 - PW
    sum2 = Pcw(word,0)*np.log2(Pcw(word,0)) + Pcw(word,1)*np.log2(Pcw(word,1))
    sum3 = Pc_neg_w(word,0)*np.log2(Pc_neg_w(word,0)) + Pc_neg_w(word,1)*np.log2(Pc_neg_w(word,1))

    return sum1 + PW*sum2 + PW_neg*sum3


# main
if __name__ == '__main__':

    load_file_mat(binary_data)

    print('shape of the matrix: ', np.shape(binary_data))
    print(binary_data)

    print('----------------------------------')  # separator

    # store the vars here to achieve dynamic programming
    l0 = cnt_l(0,binary_data)
    l1 = cnt_l(1,binary_data)

    # print the results of the two prior probabilities
    print('p(l={})={}'.format(0, prior_pro(0)))  # output: 'p(l=0)=k' for instance

    print('p(l={})={}'.format(1, prior_pro(1)))  # output: 'p(l=1)=k' for instance

    print('----------------------------------')

    #changed here
    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=0|l=0)=k' for instance
        print('p(a{}=1|l={})={}'.format(i, 0, document_fre(i, 1, 0, binary_data)))
        print('p(a{}=0|l={})={}'.format(i, 0, document_fre(i, 0, 0, binary_data)))
    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=1|l=0)=k' for instance
        print('p(a{}=1|l={})={}'.format(i, 1, document_fre(i, 1, 1, binary_data)))
        print('p(a{}=0|l={})={}'.format(i, 1, document_fre(i, 0, 1, binary_data)))
    print('----------------------------------')

    #we choose 3 words with maximum IG values by sorting all words and output the feature words and its indexes
    result = []
    for word in range(0,5):
        result.append(IG(word))


    new = sorted(result, reverse=True)  # max->min
    print(result)  # output index only





    # for i in range(0, 5):  # variable i the same as defined in worksheet
    #     # output: 'p(ai=0|l=1)=k' for instance
    #     print('p(a{}={}|l={})={}'.format(i, 0, 1, condi_pro(i, 0, 1, binary_data)))
    #
    # print('----------------------------------')
    #
    # for i in range(0, 5):  # variable i the same as defined in worksheet
    #     # output: 'p(ai=1|l=1)=k' for instance
    #     print('p(a{}={}|l={})={}'.format(i, 1, 1, condi_pro(i, 1, 1, binary_data)))
    #
    # print('----------------------------------')


    #print(type(bin))


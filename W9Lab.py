# import numpy as np
# import random
# file_path = 'predict_data.txt'
#
# result = []
# # cnt = 1
# for ele in open(file_path,'r', encoding="utf8"):
#         result.append(ele)
#
# resultX = []
# for ele in result:
#     resultX.append(ele.strip('\n'))
#
#
#
# resultY = []
# for ele in resultX:
#     resultY.append(ele.split(','))
# # print(resultY)
#
# resultZ = [[0,0] for i in range (0, len(resultY))]
# for i in range (0,len(resultY)):
#     for j in range (0,2):
#         if resultY[i][j] == '1':
#             resultZ[i][j]= 1
#         elif resultY[i][j] == '0':
#             resultZ[i][j] = 0
#
# # print(np.shape(resultZ))
# # print(resultZ)
#
# #100/5 = 20
#
# def valid(input):
#     cnt = 0
#     for i in range(0,len(input)):
#         if input[i][0] == input[i][1]:
#             cnt += 1
#
#     return (float) (cnt)/20
#
# def five_fold(input):
#     sum = 0.0
#     for i in range(0,5):
#         # index = (int)(random.random() * 5) * 20 #bug here!! can generate reptitive indices!!:(
#         # print('begin index of the data partition: ',index)
#         # print(valid(input[index:index+20]))
#         sum += valid(input[i*20:i*20+20])
#
#     return (float) (sum)/5
#
#
# sum = 0.0
# for i in range (0,10):
#     sum += five_fold(resultZ)
#
# avg_stat = (float) (sum)/10
#
# print(avg_stat)


#official answer:
from random import shuffle
import numpy as np

def count_acc(input_list):
    acc_list = []
    for i in input_list:
        right_num = 0
        for ii in i:
            if ii[0] == ii[1]:
                right_num += 1
        acc_list.append(right_num/len(i))

    return acc_list

def random_split_list(range_list_in, s_list_in):
    shuffle(range_list_in)
    N = 5
    m = int(len(range_list_in)/N)
    list_splited = []
    for i in range(0, len(range_list_in), m): #m: step length
        list_splited.append([s_list_in[k]] for k in range_list_in[i:i+m])

    return np.array(count_acc(list_splited))

with open('./predict_data.txt','r',encoding='utf-8') as f1:
    s = f1.read().split()

s_list = [[int(ii) for ii in i] for i in [i.split(',') for i in list(s)] ]
range_list = [i for i in range(0,100)]

list_mean = []
for i in range(10): #10-fold
    list_mean.append(np.mean(random_split_list(range_list,s_list)))

list_mean = np.array(list_mean) #avg array
print(list_mean)
print(np.mean(list_mean))


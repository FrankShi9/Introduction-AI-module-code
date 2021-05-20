# input = 'geeksforgeeks'
# output = set()
# for char in input:
#     output.add(char)
# print(output)


# result_list = []
# unique_set = set(input)
# for ele in input:
#     if ele in unique_set:
#         result_list.append(ele)
#         unique_set.remove(ele)
# print(result_list)

import numpy as np
# import time
#
# time_start=time.time()



# mat = np.zeros((2726,2097352), int)
# r, c = np.shape(mat)
# print(r,c)
# mat [0] [0] = 1
# print(mat)
# print('h\n')
# print('\n')
# print('f\n')

# text = ['h\n','\n','f\n']
# filename = 'test.txt'
# with open(filename, 'w') as file_object:
#     for ele in text:
#         file_object.write(ele)


# print([[1] for i in range (0,2)])
# a = [1,2,2,3,3]
# b = list(set(a))
# print(b)
# b = []
# for ele in a:
#     if ele not in b:
#         b.append(ele)
# print(b)




# as2_file = np.load('train-20ng.npz')
# as2_file = np.load('vali.npz')
# print(as2_file.files)
# as2_data = as2_file['X']
# print(as2_data)

# time_end=time.time()
# print('total cost',time_end-time_start)




# vali_file = np.load('part_result.npz')
# vali_data = as2_file['X']

# '''write file'''
# filename = 'Final.txt'
# np.set_printoptions(threshold=np.inf)
# print(as2_data[:10][:5])
# with open(filename, 'w') as f:
    # print('Final:\n', as2_data, sep='    ', file=f)

''' check cnt of 0s '''
# cnt = 0
# det = False
# for i in range(0,2726):
#
#     for ele in as2_data[i]:
#         if ele == 0:
#             cnt += 1
#         elif ele > 1:
#             det = True
#             # print('Error! We have an Aik > 1!')
#             break
#
#     if det == True:
#         break
#
# if det == False:
#     print('no ele > 1 and we have ',cnt,' 0s')
# else:
#     print('Error! We have an Aik > 1!')



# sigma = np.zeros((2726,1), int)
# sigma[0,0] = 1
# print(sigma)


# print((float)(2)/2.5)
# print(2**2)


# for i in range (0,2):
#     for j in range (0,len(as2_data)):
#         if as2_data[i][j] != vali_data[i][j]:
#             print('index: [',i, '] ', '[', j, '] ', 'value: ', as2_data[i][j], vali_data[i][j])


# import numpy as np
# a = np.arange(50000)
# b = a[::2]
# np.set_printoptions(threshold=10)
# print(b)


# map = {'g':0, 'h':1, 'i':2, 'j':3}
# print(map[0]) #error!!
a = [1,2,3]
print(a[:2])
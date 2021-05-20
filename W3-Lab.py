import numpy as np

input = [12,15,3,10]
#input = [11,5,17,18,23,50]


def removOdd(input:list):
    result = [ele for ele in input if ele % 2 == 0]
    return result
'''
def removOdd(input:list):
    for ele in input:
        if ele % 2 == 1:
            
            #no direct manipulation to the original if using for each
            input.remove(ele) 
            
            #use{ input.remove(15)/input.pop(1)/del input[1]
                  input.remove(3)/input.pop(1)/del input[1]
                 }instead


    return input
'''
print(removOdd(input))

lst = [15,6,7,10,12,20,10,28,10]
#lst = [8,6,8,10,8,20,10,8,8]

def cntOcc(input:list, x)->int:
    cnt = 0
    #for ele in input:
        #if x == ele:
            #cnt += 1
    return input.count(x)
    #return cnt

print(cntOcc(lst,10))



input = str('geeksforgeeks')
'''
def removStrDup(input:str)->set:
    result = set()
    for ele in range(0,len(input)):
        if input[ele:ele+1] not in result:
            result.add(input[ele:ele+1])

    return result;
'''


def removStrDup(input:str)->set:
    result = set()
    for ele in input:
        if ele not in result:
            result.add(ele)

    return result

print(removStrDup(input))

#correct solu:
#method1:
output = set() #random order here:) means the string is scrambled
for char in input:
    output.add(char)
print(output)
#method2:
result_list = []
unique_set = set(input)
for ele in input: #this method is ordered :)
    if ele in unique_set:
        result_list.append(ele)
        unique_set.remove(ele)
print(result_list)

input = str('hi hello hi hello hi')
def cntPat(input:str):
    input = input.split(" ")
    result = {}
    for ele in input: #get each char in the str :)
        if ele not in result.keys():
            result[ele] = 1
        elif ele in result.keys():
            result[ele]+=1

    print(result)

cntPat(input)

a = [[12,7,3],[4,5,6],[7,8,9]]

b = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]

print(np.dot(a,b))

print('----------------------------------------------------')

r1, c1 = np.shape(a)
r2, c2 = np.shape(b)

result = np.zeros([r1,c2],dtype=int)

sum, i, j = 0, 0, 0

while i<<len(a):

    for row in a[i]:

        for col in a[j]:
            sum += row*col
            j+=1

    i+=1



print(result)



#official solution:
A = np.array([[12, 7, 3],[4, 5, 6],[7, 8, 9]]) #?
B = np.array([[5, 8, 1, 2],[6, 7, 3, 0],[4, 5, 9, 1]])

r1, c1 = np.shape(A)
r2, c2 = np.shape(B)

result_mat = np.zeros([r1,c2],dtype=int)

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result_mat[i][j] += A[i][k] * b[k][j]
print(result_mat)


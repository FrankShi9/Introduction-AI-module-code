from math import *
#or as below
import math

#P1
x1 = lambda a,b,c: (-b+sqrt(pow(b,2)-4*a*c))/(2*a)
x2 = lambda a,b,c: (-b-sqrt(pow(b,2)-4*a*c))/(2*a)
print(x1(1,-5.86,8.5408))
print(x2(1,-5.86,8.5408))
'''
x = -9223372036854775808
while x< 9223372036854775808:
    if y(x) == 0:
        break
    x += 1
print(x)
'''

a = 1
b = -5.86
c = 8.5408
d = 'ha'

def quadricRoot(a,b,c):
    x1 = (-b + sqrt(pow(b,2)-4*a*c))/(2*a)
    x2 = (-b - sqrt(pow(b,2)-4*a*c))/(2*a)
    print("x1 = {}, x2 = {}".format(x1,x2))

quadricRoot(a,b,c)

#P2
def fac(n):
    if (n==1):
        return 1
    else:
        return n*fac(n-1)

#print(fac(10))

'''
for i in range (10, 0, -1):
    print(fac(i))
'''
'''
for i in range (10):
    print(i)
'''

for i in range(10,0,-1):
    print(fac(i))

#P3:
sum = 1.0
for i in range (10, 0, -1):
    sum += (1/fac(i))
    #print(sum)

print('sum1:{}'.format(sum))

sum = 1
facR = 1
sumList = [sum]
for i in range (10, 0, -1):
    facR = 1
    for j in range(i,0,-1):
        facR *= j
    sum += (1./facR)
    sumList.append((1/facR))
print('sum2:{}'.format(sum))
print(sumList)
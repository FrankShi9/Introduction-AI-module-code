import math
import sys
print(0b10,0o642,0xf3)
print(-1.8e10)
print(str('ha\nyou win'))
print("""x1
23""")
print(bytes("toto",encoding='utf-8'))

x= (int) (1+math.sin(math.pi/2))
print(x)

a,b = 1, 2
a, b = b, a
print("a: %d, b: %d" %(a,b))
print(type(15.3))

print(round(43.99,1)) #to 1 decimal place

print(type(set({2,3,1})))
print(type(set([2,3,1])))

print(chr(63)) #print a char based on ASCII code

x = "ha"
print(repr(b))
print(repr(x))

print(bytes([71,11,63]))

print(dict([(1,'h'),(2,'c')])) #key first

print(",".join(['a','b','c']))

print("ha ha ha".split(" "))

c = [1.0,2.0,3.0,4.0,5.0]

print([(int) (ele) for ele in c if ele%2==1])

x = 'my name is victor'

print(x[-1])
print(x[:7])
print(x[:-6])
print(x[:-1])

print(1 and 0)
print(1 or 0)
print(not 0)

print(math.sqrt(2))
print(math.log(2,2)) #base of log as the first arg
print(math.floor(15.6),math.ceil(15.0))
print(math.floor(15.9),math.ceil(15.1))

print(abs(-3.99))

print(4**3==pow(4,3))

a = 0

try:
    a -= 1
    if a < 0:
        raise ArithmeticError
except ArithmeticError as e:
    print("<0!",e.args)


print("ha",1,'st winner!')

#s = (int) (input('enter an integer'))
#q = (float) (input('enter a double'))
#print('{:e}\n{:.3f}'.format(s,q))

#sys.stdout

c = [9,8,7,13,0,21,9]

for ele in reversed(c):
    print(ele)

for ele in sorted(c):
    print(ele)

print('---------------------------------------------')
print(c.index(9))

print(c.count(9))

print(c*5)

print(c+[1,2]) #append at the end

d = set({1,3})
c.extend(d)
c.extend({1:3})

print(c)

name = {1:'james',2:'clark'}
print(name[1])
name[1] = 'lbj'
print(name[1])
del name[2]
print(name)
name.clear()
print(name)
name.update({1:'ken',2:'adams'})

for ele in name.keys():
    print(ele,': ')
    print(name[ele])

for ele in name.items():
    print(ele)

print('1: ',name.pop(1))
print(name)

print(name.get(1))
print(name)


with open('test.txt','r', encoding='utf-8') as f:
    for line in f:
        print(f.read())

s = 'haha'
print(s.startswith('h'))
print(s.count('h'))
print(s.partition('h'))
print(s.index('h'))
print(s.find('h'))
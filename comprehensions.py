a = [1,2,3,4,5]
print("----------------------------")
print([ele for ele in a if ele%2==0])
print("----------------------------")
b = [(1,'a'),(2,'b')]
print({k:v for k,v in b})
print("----------------------------")
c = dict({k:v for k,v in b})

d = set(ele for ele in a if ele%2==0)

print(type(c))
print(c)
print("----------------------------")
print(type(d))
print(d)
print("----------------------------")
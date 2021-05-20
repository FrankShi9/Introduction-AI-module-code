def f(n):
    yield n;
    yield n+1;

print(type(f))
print(type(f(5)))
print([ele for ele in f(5)])

gen = f(5) #generator object
print(gen.__next__())
print(next(gen))
#print(gen.__next__())


def merge(l,r):
    llen, rlen, i, j = len(l), len(r), 0, 0
    while i < llen or j < rlen:
        if j == rlen or (i<llen and l[i] < r[j]):
            yield l[i]
            i+=1
        else:
            yield r[j]
            j+=1

g = merge([2,4,7,9,16],[33,24,1,3,5])
while True:
    try:
        print(g.__next__())
    except StopIteration:
        print("Merge sort finished")
        break


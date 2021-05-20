#use lambda to override the compareTo()!!

#basics of lambda:
g = lambda x: x+3
#the above is == to
def f(x):
    return x+1

if __name__ == '__main__':
    print(g(1))
    print(f(1))
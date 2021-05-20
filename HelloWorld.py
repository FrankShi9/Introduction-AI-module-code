#hello world

if __name__ == '__main__':
    print("hanakah")
    sum = 0
    for i in range(10): #i starts from 0
        sum += i
    print('sum', sum)

    while sum>0:
        sum-=1
    print('sum', sum)
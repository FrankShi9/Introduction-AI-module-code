#-------------------------------------------------------------------------------------------------------
input = [ele for ele in '(a+n)*(b-8*m)']

result = []
stack = []
cnt = 0
#print(len(stack))

while(cnt==0 or len(stack)!=0):
    tmp = input.pop()
    if tmp == '^' or tmp == '(':
        stack.append(tmp)
    elif tmp == '+' or tmp == '-' or tmp == '*' or tmp == '/':
        tmp2 = stack[-1]
        while(tmp2 != '+' or tmp2 != '-' or len(stack)!=0):
            result.append(stack.pop())

        stack.append(tmp)

    elif tmp == ')':
        tmp3 = stack[-1]
        while (tmp3 != '(' or len(stack) != 0):
            result.append(stack.pop())
    else:
        result.append(tmp)

    cnt+=1

print(result)

#-----------------------------------------------------------------------------------------------

post = [ele for ele in 'ab*cd*-']
value = [3,2]

while len(post) != 0:
    tmp = post[0]
    if tmp == '+' or tmp == '-' or tmp == '*' or tmp == '/' or tmp == '^':
        oprOne = value.pop()
        oprTwo = value.pop()
        if tmp == '+':
            value.append(oprTwo+oprOne)
        elif tmp == '-':
            value.append(oprTwo-oprOne)
        elif tmp == '*':
            value.append(oprTwo*oprOne)
        elif tmp == '/':
            value.append(oprTwo/oprOne)
        elif tmp == '^':
            value.append(oprTwo**oprOne)
    else:
        value.append(tmp)

#------------------------------------------------------------------------------------------------------------------------
cnt = 0
input = [ele for ele in '2*3+4']
stack1, stack2 = [], []
result = []

while cnt==0 or len(input) != 0:
    tmp = input.pop(0)
    if tmp == '+' or tmp == '-' or tmp == '*' or tmp == '/' or tmp == '^':
        stack1.append(tmp)
    else:
        stack2.append(tmp)

    cnt+=1

while len(stack1) != 0:
    tmp = stack1.pop()
    oprOne = stack2.pop(0)
    oprTwo = stack2.pop(0)
    if tmp == '+':
        stack2.append(oprTwo + oprOne)
    elif tmp == '-':
        stack2.append(oprTwo - oprOne)
    elif tmp == '*':
        stack2.append(oprTwo * oprOne)
    elif tmp == '/':
        stack2.append(oprTwo / oprOne)
    elif tmp == '^':
        stack2.append(oprTwo ** oprOne)
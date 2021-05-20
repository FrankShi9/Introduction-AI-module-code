from functools import singledispatch

def testAge():
    inputU = input('please input your age:')
    age(inputU)


@singledispatch
def age(input):
    print('input is invalid!')

@age.register(int)
def _(input):
    print('i am {} years old'.format(input))


@age.register(str)
def _(input):
    print('i am %s years old' %input)

if __name__ == '__main__':
    #testAge()
    age(23)
    age('23')
    age({23})
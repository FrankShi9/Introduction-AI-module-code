import numpy as np
from matplotlib import pyplot as plt

f = lambda x1, x2: (10*pow(x1,2)+pow(x2,2))/2
fx1 = lambda x1: 10*x1
fx2 = lambda x2: x2
#print(1e-6)

x1, x2, y = [],[],[]

def gradient_descend(learning_rate, precision=1e-06):
    ite = 0
    current, successor = np.random.rand(2), np.random.rand(2)
    while(ite==0 or abs(f(successor[0],successor[1])-f(current[0],current[1])) < precision):
        successor = current - learning_rate*np.gradient(f(current[0],current[1]))
        current = successor
        ite+=1
    return current

def gradient_descend2(learning_rate, precision=1e-06):
    ite = 0
    current = np.random.rand(2)
    successor = np.random.rand(2)

    x1.append(current[0])
    x2.append(current[1])
    y.append(f(current[0], current[1]))

    while(ite==0 or (abs(f(successor[0],successor[1])-f(current[0],current[1])) > precision)):

        gra = np.random.rand(2)
        gra[0] = fx1(current[0])
        gra[1] = fx2(current[1])
        successor = current - learning_rate*gra
        current = successor

        # data store
        x1.append(current[0])
        x2.append(current[1])
        y.append(f(current[0],current[1]))
        #print(current)

        ite+=1

    return current

def plotJob():
        # 2D
        plt.figure()
        ax = plt.subplot(111)
        ax.plot(x1,x2)
        plt.show()

        # 3D
        plt.figure()
        ax = plt.subplot(111, projection='3d')
        ax.plot(xs=x1, ys=x2, zs=y)
        plt.show()

if __name__ == '__main__':
    print(gradient_descend2(0.01))
    #print(x1)
    plotJob()
    #current, successor = np.random.rand(2, 1), np.random.rand(2, 1)
    #print(f(successor[0][0],successor[1][0])-f(current[0][0],current[1][0]))
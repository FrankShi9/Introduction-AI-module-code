import random
from random import shuffle
import pandas
import numpy as np
import matplotlib.pyplot as plt

data_path = 'iris.data'
data = pandas.read_csv(data_path,header=None,index_col=True)


shuffle(data, random.seed(9))

K = []
cluster_1 = []
cluster_2 = []
cluster_3 = []

for i in range(3):
    K.append(data[random.randint(0,150)])

change = True

while change:
    for ele in data:
        dis1 = np.sqrt((ele[0]-K[0][0])**2+(ele[1]-K[0][1])**2+(ele[2]-K[0][2])**2+(ele[3]-K[0][3])**2)
        dis2 = np.sqrt((ele[0]-K[1][0])**2+(ele[1]-K[1][1])**2+(ele[2]-K[1][2])**2+(ele[3]-K[1][3])**2)
        dis3 = np.sqrt((ele[0]-K[2][0])**2+(ele[1]-K[2][1])**2+(ele[2]-K[2][2])**2+(ele[3]-K[2][3])**2)

        if dis1< dis2 and dis1< dis3:
            cluster_1.append(ele)
        elif dis2< dis1 and dis2< dis3:
            cluster_2.append(ele)
        elif dis3 < dis1 and dis3 < dis2:
            cluster_3.append(ele)
        else:
            change = False
            break

        for c1 in cluster_1:
            sum += c1

        K[0] = np.mean(sum)

        for c2 in cluster_2:
            sum += c2

        K[1] = np.mean(sum)

        for c3 in cluster_3:
            sum += c3

        K[2] = np.mean(sum)

# plot 2D
plt.figure()
ax = plt.subplot(111)
ax.plot(cluster_1,cluster_2,cluster_3)
plt.show()
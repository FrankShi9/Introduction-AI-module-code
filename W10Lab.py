import pandas
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np
import random

data_path = 'iris.data'
data = pandas.read_csv(data_path,header=None)

# print(data[4])

# y = data[4]
col = [0,1,2,3]
X = data[col]

y = data[4]
# change str to categorical values
result = []
for ele in y:
    # print(ele)
    if ele.__contains__('Iris-versicolor'):
        result.append(0)
        print('new ele:', 0)
    elif ele.__contains__('Iris-versicolor'):
        result.append(1)
        print('new ele:', 1)
    elif ele.__contains__('Iris-virginica'):
        result.append(2)
        print('new ele:', 2)

print(data.shape)
# print(data.columns)

# print(y.head())
print(result)
# print(X.head())

train, test = train_test_split(X, random_state=0)

n = 0.5 #learning rate
b = 0 #bias
D = np.zeros((150,6), dtype = float) #data ndarray [-2]:y [-1]:updated or not

for r in range(0,150):
    for c in range (0,4):
            D[r][c] = train[r][c]

w = np.zeros((150,1), dtype= float) #weight array one row for each xi in row i

# print(w)

def split(input,per):
    buf = random.randint(0,150)
    return input[buf:buf+(int) (D.shape[0]*per)], input[buf:buf+(int) (D.shape[0]*(1-per) )]

def get_ran(input):
    buf = input.copy()
    # shuffle and pop
    random.shuffle(buf)
    return buf.pop()

def model(input):
    d_copy = np.copy(D)
    w_copy = np.copy(w)
    global n, b
    while d_copy[:][5] == 0.0:
        for ele in d_copy[:][0:4]:
            r, c = 0, 0
            buf = np.sign(np.dot(input[r][c], w_copy[r][0])) + b
            d_copy[r][4] = buf
            if buf <= 0.0:
                w_copy[r][0] += n * buf * input[r][c]
                b += n * buf
                d_copy[r][5] = 1.0
    return
    #MAE??

#official answer
import numpy as np
import pandas as pd
from random import shuffle

def random_split(x,y):
    range_list_in = [i for i in range(0,100)]
    shuffle(range_list_in)

    m = int(len(range_list_in)*7/10) #step length

    train_data_array = np.array([x[k] for k in range_list_in[0:m]])

    test_data_array = np.array([x[k] for k in range_list_in[m:]])

    train_label_array = np.array([y[k] for k in range_list_in[0:m]])

    test_label_array = np.array([y[k] for k in range_list_in[m:]])

    return train_data_array, test_data_array, train_label_array, test_label_array


path = 'binary_data.csv'

data = pd.read_csv(path, header=None) #add a first label row to the data set

x = data[list(range(4))].to_numpy()
y = data[4].to_numpy()

train_data_array, test_data_array, train_label_array, test_label_array = random_split(x,y)

train_label_array[train_label_array == 0] = -1

w = np.zeros([1,4])
b = np.zeros(1)
not_correctly_classified = True
lr = 0.001 #learning rate


# print(w.T)
i = 0
while not_correctly_classified:#is true
    x_train = train_data_array[i]
    y_train = train_label_array[i]
    y_pred = np.sign(np.dot(x_train, w.T)+b) #w transposed
    if y_train*y_pred <= 0:
        w = w + lr * y_train * x_train
        b = b + lr * y_train

    y_vali = np.sign(np.dot(train_data_array, w.T)+b)
    i += 1
    if i == 70: #already 70 iterations
        i -= 70
    if (y_vali.squeeze() == train_label_array).all(): #all satisfy
        not_correctly_classified = False
        print(i)
        y_test_pred = np.sign(np.dot(test_data_array, w.T)+b)
        print((y_test_pred.squeeze() == test_label_array).sum()/30)








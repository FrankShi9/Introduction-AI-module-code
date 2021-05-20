import numpy as np
import matplotlib.pyplot as plt

def function_x(x):
    y = (10 * x[0] ** 2 + x[1] ** 2) / 2
    return y

x = np.random.rand(2)
alpha = 0.05
delta = 0.000001

x_list=[]
x_ax = []
y_ax = []
y_list = []

count = 0
while 1:
    if count == 0:
        x_t = x
        x_list.append(x_t)
        x_ax.append(x_t[0])
        y_ax.append(x_t[1])
    else:
        x_t = x_t_next
    y_diff = np.array([10* x_t[0], x_t[1]])
    x_t_next = x_t - alpha * y_diff
    count += 1
    x_list.append(x_t_next)
    x_ax.append(x_t_next[0])
    y_ax.append(x_t_next[1])
    y_list.append(function_x(x_t))
    if abs(function_x(x_t_next) - function_x(x_t)) < delta or count == 10000:
        y_list.append(function_x(x_t_next))
        break

print(x_list)

# plot 2D
plt.figure()
ax = plt.subplot(111)
ax.plot(x_ax,y_ax)
plt.show()

#plot 3D
plt.figure()
ax = plt.subplot(111, projection='3d')
ax.plot(xs=x_ax,ys=y_ax,zs=y_list)
plt.show()

print(x_ax, y_ax ,y_list)
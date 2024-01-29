import random
import math
import matplotlib.pyplot as plt
import numpy as np

x=0.0
outcome=0
w1, w0, eta = 0.01, 0.01, 0.01
x_record, r_record, entropy_record = [], [], []

def sigmoid(x, w1, w0):
    return 1 / (1 + math.exp(-w1*x-w0))

def func(x):    # y(x)
    if x<1:
        return 0
    elif x>3:
        return 1
    else:
        return 0.5*(x-1)

for iteration in range(30): # generate 30 sample points
    x = random.uniform(-4, 4)
    zeta = random.uniform(0, 1)
    if zeta < func(x):
        outcome = 1
    else:
        outcome = 0
    x_record.append(float(x))
    r_record.append(int(outcome))

epoch=100
for iteration in range(epoch):
    sum1, sum2, sum_en = 0.0, 0.0, 0.0
    for i in range(30):
        y = sigmoid(x_record[i], w1, w0)
        sum1 += (r_record[i]-y)*x_record[i] # dE/dw1
        sum2 += (r_record[i]-y) # dE/dw0
        sum_en -= (r_record[i]*math.log(y) + (1-r_record[i])*math.log(1-y)) # cross entropy
    w1 += eta*sum1
    w0 += eta*sum2
    if iteration%10==0:
        entropy_record.append(sum_en)
        #print(f"iteration = {iteration}, error = {sum_en}")

print(f"w1 = {w1}\nw0 = {w0}")

# 1a
plt.scatter(x_record, r_record)
plt.xlabel('x')
plt.ylabel('r')
plt.show()

# 1b
sigmoid_x = sorted([random.uniform(-4, 4) for _ in range(100)])
sigmoid_y = [sigmoid(sigmoid_x[i], w1, w0) for i in range(100)]
plt.plot(sigmoid_x, sigmoid_y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 1c
entropy_x = [10*i for i in range(10)]
plt.scatter(entropy_x, entropy_record)
plt.xlabel('Iteration')
plt.ylabel('Entropy')
plt.show()
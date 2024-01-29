# Perceptron AND
from math import *
import random
import matplotlib.pyplot as plt

eta=0.1
w1=random.uniform(-0.1,0.1)
w2=random.uniform(-0.1,0.1)
w0=random.uniform(-0.1,0.1)

HIGH=0.9
LOW=0.1

def logistic(w1, w2, w0, x1, x2):
    return 1/(1+exp(-w1*x1 - w2*x2 - w0))

input=[(0.1, 0.1), (0.9, 0.1), (0.1, 0.9), (0.9, 0.9)]  # (x1, x2)
desire=[LOW, LOW, LOW, HIGH]    # desire answers
for i in range(1000):
    for idx in range(4):
        x1 = random.gauss(input[idx][0], 0.1)
        x2 = random.gauss(input[idx][1], 0.1)
        output = logistic(w1, w2, w0, x1, x2)

        w1 -= eta*(output-desire[idx])*x1
        w2 -= eta*(output-desire[idx])*x2
        w0 -= eta*(output-desire[idx])*1
    
    if i%100==0:
        error=0
        for idx in range(4):
            error += (logistic(w1, w2, w0, input[idx][0], input[idx][1]) - desire[idx])**2
        #print(f"iteration = {i}, error = {error}")

print(f"w1 = {w1}, w2 = {w2}, w0 = {w0}")
for i in range(4):
    output = logistic(w1, w2, w0, input[i][0], input[i][1])
    print(f"(x1, x2) = ({input[i][0]}, {input[i][1]}), output = {output}")

X1=[0,0,1,1]
X2=[0,1,0,1]
plt.scatter(X1,X2)
X=[i/10 for i in range(16)]
Y=[(-w0-w1*x)/w2 for x in X]
plt.plot(X,Y)
plt.show()
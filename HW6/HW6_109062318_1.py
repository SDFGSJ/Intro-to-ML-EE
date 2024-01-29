# Perceptron NOT
from math import *
import random

eta=0.1
w=random.uniform(-0.1,0.1)
w0=random.uniform(-0.1,0.1)

HIGH=0.9
LOW=0.1

def logistic(w, w0, x):
    return 1/(1+exp(-w*x - w0))

input=[0.1, 0.9]
desire=[HIGH, LOW]
for i in range(1000):
    for idx in range(2):
        x = random.gauss(input[idx], 0.1)
        output = logistic(w, w0, x)

        w -= eta*(output-desire[idx])*x
        w0 -= eta*(output-desire[idx])*1
    
    if i%100==0:
        error=0
        for idx in range(2):
            error += (logistic(w, w0, input[idx]) - desire[idx])**2
        #print(f"iteration = {i}, error = {error}")

print(f"w = {w}, w0 = {w0}")
for i in range(2):
    output=logistic(w, w0, input[i])
    print(f"x = {input[i]}, output = {output}")

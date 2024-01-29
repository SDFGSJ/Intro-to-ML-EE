from math import *
import random

eta=0.1
w_x=random.uniform(-0.1,0.1)
w_y=random.uniform(-0.1,0.1)
theta=random.uniform(-0.1,0.1)

HIGH=0.99
LOW=0.01

def logistic(w_x, w_y, theta, x, y):
    return 1/(1+exp(-w_x*x - w_y*y - theta))

L=[(0,0), (1,0), (0,1), (1,1)]
HL=[LOW, HIGH, HIGH, HIGH]
for i in range(1000):
    for idx in range(4):
        x = random.gauss(L[idx][0], 0.1)
        y = random.gauss(L[idx][1], 0.1)
        output = logistic(w_x, w_y, theta, x, y)

        w_x -= eta*(output-HL[idx])*x
        w_y -= eta*(output-HL[idx])*y
        theta -= eta*(output-HL[idx])*1
    
    if i%100==0:
        error=0
        for idx in range(4):
            error += (logistic(w_x, w_y, theta, L[idx][0], L[idx][1]) - HL[idx])**2
        print(f"iteration = {i}, error = {error}")

print(f"wx={w_x}, wy={w_y}, theta={theta}")
for i in range(4):
    output=logistic(w_x, w_y, theta, L[i][0], L[i][1])
    print(f"(x, y) = ({L[i][0]}, {L[i][1]}), output = {output}")

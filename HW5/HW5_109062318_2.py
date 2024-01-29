import random
import numpy as np
import math

x1, x2 = 0.0, 0.0
y1, y2 = 0.0, 0.0
count1_error, count2_error = 0, 0

mu1, sigma1 = np.array([0, 0]), 1
mu2, sigma2 = np.array([3, 4]), 3

xc = ((sigma2**2)*mu1 - (sigma1**2)*mu2) / (sigma2 - sigma1)
r_square = ((sigma1**2 * sigma2**2)/(sigma2**2 - sigma1**2))*(np.sum(np.square(mu1+mu2))/(sigma2**2 - sigma1**2) + 4*math.log(sigma2/sigma1))
print("center =", xc)
print("radius =", math.sqrt(r_square))
print("=====")

# class 1 with mean = (0,0), sigma = 1
# (horizontal, vertical) = (x1, x2)
for i in range(1000):
    x1=random.gauss(0,1)
    x2=random.gauss(0,1)

    if (x1 - xc[0])**2 + (x2 - xc[1])**2 > r_square:
        count1_error += 1
print(f"error rate 1 = {count1_error/1000}")
print("=====")

# class 2 with mean = (3,4), sigma = 3
# (horizontal, vertical) = (y1, y2)
count2_error_list = []
for _ in range(10):
    count2_error = 0
    for i in range(1000):
        y1=3.0+random.gauss(0,3)
        y2=4.0+random.gauss(0,3)

        if (y1 - xc[0])**2 + (y2 - xc[1])**2 < r_square:
            count2_error += 1
    #print(f"error rate 2 = {count2_error/1000}")
    count2_error_list.append(count2_error/1000)

tmp=np.array(count2_error_list)
print(count2_error_list)
print(f"mean = {np.mean(tmp)}")
print(f"std = {np.std(tmp)}")
print(f"count 2 error = {np.mean(tmp)} +- {np.std(tmp)}")
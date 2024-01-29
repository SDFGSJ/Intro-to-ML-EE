import random
import numpy as np

experiments=10
samples=10**6

def solve(dimension, b):
    for i in range(experiments):
        # init on every experiments
        minW=np.array([])
        minZ=2**31-1

        for j in range(samples):
            w=np.array([random.uniform(0,1) for _ in range(dimension)]) # w = [w1, w2, ..., wi]
            Z=(w-b).T @ (w-b)   # = sum of squares of w-b

            if Z<minZ:
                minW=w
                minZ=Z
        print(f"experiment {i+1}: w = {minW}, Z has min = {minZ}")

solve(3, np.array([3, 1/2, 1/2]))  # <= ans of 2(a).
solve(5, np.array([3, 1/2, 1/2, 1/2, 1/2]))    # <= ans of 2(c).
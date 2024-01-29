import random
from math import *
import numpy as np

X, Y = [], []
for i in range(5):
    with open(f'dataset{i}.csv','w') as fh:
        fh.write('x,y\n')
        tmp_x, tmp_y = [], []
        for j in range(20):
            x=random.uniform(-2,2)
            y=cos(1.5*x)+random.gauss(0,1)
            fh.write(f'{x},{y}\n')
            tmp_x.append(x)
            tmp_y.append(y)
        X.append(tmp_x)
        Y.append(tmp_y)

def solve(deg):
    COEFS=[]
    for i in range(5):
        # coef: Polynomial coefficients, highest power first.
        # ex. deg(f(x))=2 and coef=[1,2,3] => f(x) = 1x**2 + 2x + 3
        coef=np.polyfit(x=X[i], y=Y[i], deg=deg)
        print(f"g{i+1}(x) coef = {coef}")
        COEFS.append(coef)
    print(f"deg={deg} => average gi(x) = {np.mean(COEFS,axis=0)}")

solve(deg=4)    # [x^4 coef, x^3 coef, x^2 coef, x coef, const]
print()
solve(deg=2)    # [x^2 coef, x coef, const]
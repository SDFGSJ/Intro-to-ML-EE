import math
import matplotlib.pyplot as plt

p=0.9
N=50
def BCE(p,q):
    return p*math.log(q)+(1-p)*math.log(1-q)

X=[q/N for q in range(1,N)] # [0, ..., 1]
#print(X)
Y=[BCE(p,q) for q in X]
#print(Y)
plt.plot(X,Y)
plt.show()
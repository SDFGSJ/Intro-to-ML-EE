import math
import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-5, 0, num=50, endpoint=True)
#print(X)
Y=[math.log(math.exp(-x)+1) for x in X]

plt.scatter(X, Y)
plt.show()
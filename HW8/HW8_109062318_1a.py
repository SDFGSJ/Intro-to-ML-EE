# -*- coding: utf-8 -*-
"""EE ML PCA HW8 1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wCaSEcByPdQMW5_lKniIIcKKHmxt7OxN
"""

# Commented out IPython magic to ensure Python compatibility.
# Python �竉3.5 is required
import sys
assert sys.version_info >= (3, 5)

# Scikit-Learn �竉0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"

# Common imports
import numpy as np
import os

# to make this notebook's output stable across runs
np.random.seed(42)

# To plot pretty figures
# %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

np.random.seed(4)
m = 1000
noise = 0.1

angles = np.random.rand(m) * 2 * np.pi 
X = np.empty((m, 3))
X[:, 0] = (angles/6.28) * np.cos(angles) + noise * np.random.randn(m)
X[:, 1] = (angles/6.28) * np.sin(angles) + noise * np.random.randn(m)
X[:, 2] = noise * np.random.randn(m)

# my code
myX=(angles/6.28)*np.cos(angles)
myY=(angles/6.28)*np.sin(angles)
myZ=0


from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X2D = pca.fit_transform(X)


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

# my code
for idx in range(len(pca.components_)):
    print(f'new vector {idx+1} = {pca.components_[idx]}')
myfig = plt.figure()
myax = myfig.add_subplot(projection='3d')
myax.scatter(myX, myY, myZ)

ax.plot(X2D[:, 0], X2D[:, 1], "k+")
ax.plot(X2D[:, 0], X2D[:, 1], "k.")
ax.plot([0], [0], "ko")
ax.arrow(0, 0, 0, 1, head_width=0.05, length_includes_head=True, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, 1, 0, head_width=0.05, length_includes_head=True, head_length=0.1, fc='k', ec='k')
ax.set_xlabel("$z_1$", fontsize=18)
ax.set_ylabel("$z_2$", fontsize=18, rotation=0)
ax.axis([-2, 2, -2, 2])
ax.grid(True)
plt.show()
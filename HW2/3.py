import numpy as np

x1, y1 = 0, 0.5
x2, y2 = 1, 2.5
x3, y3 = 3, 12.5

X = np.array([[1, x1, x1**2], [1, x2, x2**2], [1, x3, x3**2]])
#print('X shape =',X.shape)
#print('X.T =',X.T,'\nX =',X)

y = np.array([[y1, y2, y3]]).T
#print('y shape =',y.shape)
#print('y =',y)

print('(1) ans =\n',X.T @ X)
print('=====================')
print('(2) ans =\n',np.linalg.inv(X.T @ X) @ X.T @ y)
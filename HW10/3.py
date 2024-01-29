import math

T=[1,10,100]
qa=[0,10,11,12,13]

for t in T:
    bottom=0
    for i in range(1,5):
        bottom+=math.exp(qa[i]/t)
    for i in range(1,5):
        print(f"T={t}: p(a{i})={math.exp(qa[i]/t) / bottom}")

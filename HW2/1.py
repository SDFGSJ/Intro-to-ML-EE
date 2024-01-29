import random
import numpy as np
experiments=10
numNeedles=10**6
piGuess=0.0
tmp=[]

def throwNeedles(numNeedles):
    inCircle=0
    for i in range(1, numNeedles+1):
        l=[random.uniform(-1,1) for i in range(5)]   # [x1, x2, ..., x5]
        x=np.array(l)

        x_square_sum=np.sum(np.square(x))   # x1^2 + ... + x5^2
        
        if x_square_sum<=1:
            inCircle+=1
    return 32*(inCircle/numNeedles)

for i in range(experiments):
    piGuess=throwNeedles(numNeedles)
    tmp.append(piGuess)

ans=np.array(tmp)
print('Mean =',np.mean(ans))
print('Standard deviation =',np.std(ans))
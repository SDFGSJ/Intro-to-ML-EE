import random
numNeedles=10**6
piGuess=0.0

def throwNeedles(numNeedles):
    inBall=0
    for i in range(1, numNeedles+1):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        z=random.uniform(0,1)
        if x*x + y*y + z*z < 1:    # inside the ball
            inBall+=1
    return 1*(inBall/numNeedles)    # volume of 1/8 ball / volume of cube = # in ball / # of needles

piGuess=throwNeedles(numNeedles)
print('Est =',piGuess)
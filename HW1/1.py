import random
numNeedles=10**6
piGuess=0.0

def throwNeedles(numNeedles):
    inCircle=0
    for i in range(1, numNeedles+1):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if y <= x*x:    # y <= x^2 means point y is under the graph x^2
            inCircle+=1
    return 1*(inCircle/numNeedles)  # area(under the graph) / area(square) = # in circle / # of all needles

piGuess=throwNeedles(numNeedles)
print('Est =',piGuess)
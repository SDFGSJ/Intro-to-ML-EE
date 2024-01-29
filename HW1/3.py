import random
w2=2.0
w1=0.5
w0=0.3
num_sample=30

with open('random points.csv','w') as fh:
    fh.write("x,r\n")
    for i in range(0,num_sample):
        x=random.uniform(0,1)
        r=w2*x**2 + w1*x + w0 + random.gauss(0,0.1)
        print('x =', round(x,3), ', r =', round(r,3))
        fh.write(f"{round(x,3)},{round(r,3)}\n")
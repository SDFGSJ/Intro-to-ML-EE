import math
import random
import matplotlib.pyplot as plt

r=2.5
learning_rate=0.01
rounds=50

for i in range(50):
    x,y=[],[]

    theta=random.uniform(0, 2*math.pi)
    w1=r*math.cos(theta)
    w2=r*math.sin(theta)
    for _ in range(rounds):
        x.append(w1)
        y.append(w2)
        new_w1=w1-learning_rate*(4*w1*(w1**2+w2**2)-8*w1)
        new_w2=w2-learning_rate*(4*w2*(w1**2+w2**2)-8*w2)
        w1=new_w1
        w2=new_w2
        
    #print(x)
    #print(y)
    #print(f"start={x[0],y[0]}, end={x[-1],y[-1]}")
    #print(f"end radius = {x[-1]**2 + y[-1]**2}")
    plt.scatter(x, y)


circle1 = plt.Circle((0, 0), r, color='b', fill=False)
circle2 = plt.Circle((0, 0), math.sqrt(2), color='r', fill=False)
plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)
plt.xlabel('w1')
plt.ylabel('w2')
plt.show()
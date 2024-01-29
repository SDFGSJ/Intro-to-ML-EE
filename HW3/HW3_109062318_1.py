import random
import matplotlib.pyplot as plt

yA=[]
yB=[]
yC=[]

priorA=1/3  # P(H=A)
priorB=1/3  # P(H=B)
priorC=1/3  # P(H=C)

Pgreen_A=0.3  # P(green|A)
Pred_A=0.7    # P(red|A)
Pgreen_B=0.7  # P(green|B)
Pred_B=0.3    # P(red|B)
Pgreen_C=0.9  # P(green|C)
Pred_C=0.1    # P(red|C)

# init
P_A_red=0   # P(A|red)
P_A_green=0 # P(A|green)
P_B_red=0   # P(B|red)
P_B_green=0 # P(B|green)
P_C_red=0   # P(C|red)
P_C_green=0 # P(C|green)

iteration=100
for i in range(iteration):
    x=random.uniform(0,1)
    if x>=0 and x<=Pgreen_C:
        P_A_green = Pgreen_A*priorA / (Pgreen_A*priorA + Pgreen_B*priorB + Pgreen_C*priorC)
        P_B_green = Pgreen_B*priorB / (Pgreen_A*priorA + Pgreen_B*priorB + Pgreen_C*priorC)
        P_C_green = Pgreen_C*priorC / (Pgreen_A*priorA + Pgreen_B*priorB + Pgreen_C*priorC)

        priorA=P_A_green
        priorB=P_B_green
        priorC=P_C_green
    else:
        P_A_red = Pred_A*priorA / (Pred_A*priorA + Pred_B*priorB + Pred_C*priorC)
        P_B_red = Pred_B*priorB / (Pred_A*priorA + Pred_B*priorB + Pred_C*priorC)
        P_C_red = Pred_C*priorC / (Pred_A*priorA + Pred_B*priorB + Pred_C*priorC)

        priorA=P_A_red
        priorB=P_B_red
        priorC=P_C_red
    
    yA.append(priorA)
    yB.append(priorB)
    yC.append(priorC)

X=[i+1 for i in range(iteration)]
plt.plot(X, yA, label='A')
plt.plot(X, yB, label='B')
plt.plot(X, yC, label='C')
plt.xlabel('Num of iterations')
plt.ylabel('Probability')
plt.legend(loc='center right')
plt.show()
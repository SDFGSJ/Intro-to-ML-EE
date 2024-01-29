m=[['.' for i in range(10)] for j in range(10)]
#print(m)
for row in m:
    print(row)
path=[1,2,3,1,1,2,2,3]
def myplot(start, path):
    print(start)
    posx=start[0]
    posy=start[1]
    m[posx][posy]='X'
    for p in path:
        if p==1:
            posx-=1
        elif p==2:
            posy+=1
        else:
            posy-=1
        print((posx,posy))
        m[posx][posy]='X'


myplot(start=(9,0), path=path)
for row in m:
    print(row)
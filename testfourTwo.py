import math
import random
def h(x):
    return x**2
def computerArea(n,xrange):
    m=0
    yrange=h(xrange)
    for i in range(0,n):
        x=random.uniform(0,xrange)
        y=random.uniform(0,yrange)
        z=h(x)
        if y<z:
            m+=1

    return yrange*xrange*m/n
print(math.floor(computerArea(1000000,2)*1000000)/1000000) 



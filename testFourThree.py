import math
import random
def h(x):
    return 2*math.sin(x)*math.exp(-0.05*x)
def computrerMax(n):
    maxpoint=0
    maxValue=h(0)
    for i in range(n):
        x=random.uniform(-2,2)
        if h(x)>maxValue:
            maxValue=h(x)
            maxpoint=x
    return maxpoint,maxValue
point,value=computrerMax(1000)
print("MAXpoint:",point)
print("maxValue",value)

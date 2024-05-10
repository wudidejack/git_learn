import random
import math
def computerPI(n,R):
    m=0
    for i in range (0,n):
        x=random.uniform(-R,R)
        y=random.uniform(-R,R)
        z=x**2+y**2
        if z<=R**2:
            m+=1
    return 4*m/n

r=2
N=1
ending=[]
while(math.floor(computerPI(N,r)*1000000)/1000000 !=3.141592):
    ending.append(computerPI(N,r))
    N*=10
with open('data.txt','w') as d:
    d.write(N)
print(ending)

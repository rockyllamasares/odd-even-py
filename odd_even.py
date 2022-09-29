from math import *

a = int(input("Start of Range: "))
b = int(input("End of Range: "))
e , o = 0 , 0,
for i in range(a,b+1):
    if(i%2)!=0:
        o = o+i
    else:
        e = e+i
        print("The sum of all odd: ",o)
        print("The sum of all even: ",e)

def Fact(n):
    s=1
    for x in range (1,n+1):
        s*=x
    return s
from math import *
a=int(input("a="))
n=int(input("n="))
def Exp1(a,n):
    s=0
    for x in range(2,n+1):
        s=pow(x,n)/Fact(n)
        s+=x
    return s

print( Exp1(a,n))































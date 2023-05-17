# 1
# n= int(input("n="))
# k=1 
# s=0
# while k<=n:
#     s+=1/k
#     k+=1
# print(s)
#b
# from math import *
# n= int(input("n="))
# k=1 
# s=0
# while k<=n:
#     s+=1/pow(k,5)
#     k+=1
# print(s)
#2
# n= int(input("n="))
# x= float(input("x="))
# s=0
# k=1
# p=1
# while n<=k:
#     s+=x**k/p
#     p*=k
#     k+=1
# print(s)
#b
# from math import*
# n= int(input("n="))
# x= float(input("x="))
# s=0
# p=1
# k=1
# while k<=n:
#     s+=(1/p+sqrt(fabs(x),2))
#     p*=k
#     k+=1
# print(s)
# 3
# n= int(input("n="))
# a0=1
# s=0
# k=1
# while k<=n:
#     a1=n*a0+1/n
#     a2=a1
#     k+=1
# print("a n=",a2)   
#7
# n=103
# s=103
# while n>1:
#     n-=2
#     s=n+1/s
# s=1/s
# print(s)
# 8
# x=float(input("x=")) 
# s=x*x
# n=256
# while (n>=2):
#     s=x*x+n/s
#     n/=2 
# p=x/s
# print(p) 
#1
# a=int(input("a="))
# b=int(input("b="))
# k=0
# while a>=b:
    
#     k+=1
#     a-=b
# print(a)
#2
# a=int(input("a="))
# b=int(input("b="))
# k=0
# while a>=b:
    
#     k+=1
#     a-=b
# print(a)
# 3
# a=int(input("a="))
# b=int(input("b="))
# k=0
# while a>=b:
    
#     k+=1
#     a-=b
# print("qoldiq=",a)
# print("butun=",k)
# 4
from math import *
n=int(input("n="))
isdaraja= False
daraja=0
p=pow(5,0)
while (n>=p):
    daraja+=1
    p= pow (5,daraja) 
    if (p==n):
        isdaraja=True
        break
    
if (isdaraja):
    k = 1
    while(k <= n):
        if n % k == 0:
            print(k)
        k += 1
x=0 
y=1   
while n>=x:
    s=0
    while y<=x:
        if x%y==0:
            x+=1
            y+=1
    if s==2:    
        print(x,end=" ")



# 6
# n=int(input("n="))
# k=0
# p=0
# while n<=k:
#     p*=n
#     k-=-2
    


















































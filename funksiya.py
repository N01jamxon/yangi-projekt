# a=int(input("a="))
# b=int(input("b="))
# funksiya=int(input("funksiya="))
# from math import *

# def hisoblash(a,b,funksiya):
    
#     if (funksiya==1):
#         s=pow(a,b)

#     if (funksiya==2):
#         s=sqrt(a*b)
        
#     if (funksiya==3):
#         s=fabs(a-b)
#     return s

# print("natija = ",hisoblash(a, b, funksiya))
# from math import *
# n=int(input("n="))
# a=int(input("a="))

# def juftson(num):
#     a = sqrt(num * 100)
#     print("Juft son = ", a)
# def toqson(nam):
#     a = nam*10
#     print("Toq son = ", a)
# def musbatson(musbat):
#     if musbat % 2 == 0:
#         juftson(musbat)
#     else:
#         toqson(musbat)


# def manfiyson(manfiy):
#     print("Bu son manfiy son ekan")

# def musbatmanfiy(number):
#     if number>0:
#         son=musbatson(number)
        
#     else:
#         manfiyson(number)
      

# musbatmanfiy(n)
# musbatmanfiy(a)
# 1
# a=int(input("a="))
# b=int(input("b="))

# def ishora(son):
#     if (son>0):
#         a=1
#     if (son<0):
#         a=-1

#     if (son==0):
#         a=0
#     return a
# ishora(a)
# ishora(b)
# print(ishora(a)+ishora(b))

# 2
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))

# def ildiztopish(a, b, c):
#     d=b*b-4*a*c
#     if (d>0):
#         return 2
#     if (d<0):
#         return "ildizdizga ega emas"
#     if (d==0):
#         return 1
# natija=ildiztopish(a,b,c)  
# print("natija=",natija) 

# 3
# r=int(input("r="))
# p=3.14
# def doirayuzasi(r,p):
#     s=p*r*r
#     if r>0:
#         s=p*r*r
    
#     return s
# S=doirayuzasi(r,p)
# print("yuza=", S)

# 4
# from math import *
# n=int(input("n="))

# def daraja(n):
#     s=1
#     if n!=0:
#         s=pow(2,n)
#     return s  
# m=daraja(n)
# print("darajasi",m)

# 7
# from math import *
# a=int(input("a="))
# n=int(input("n="))
# def daraja(a,b):
#     s=0
#     if b!=0:
#         s=pow(a,n)
#     return s
# m=daraja(a,n)
# print("daraja",m)

#1 
# from math import *
# a=float(input("a="))
# def PowerA3(a):
#     s=0
#     # if a!=0:
#     s=pow(a,3)
#     return s
# m=PowerA3(a,)
# print("daraja",m)
#2
# from math import *
# a=float(input("a="))
# def PowerA234(a):
#     s=0
#     if a!=0:
#         s=pow(a,2)
#         print("ikkinchisi=",s)
#     if a!=0:
#         s=pow(a,3) 
#         print("uchinchisi=",s)
#     if a!=0:
#         s=pow(a,4)
#         print("tortinchisi=",s)       
#     return s
# m=PowerA234(a,)

# 3
# from math import *
# a=float(input("a="))
# b=float(input("b="))
# def mean(a, b):
#     s=0
#     if a>0 and b>0:
#         s=sqrt((a*b))
#         print("geometrigi",s)
#     else:
#         print("mumkin emas")
#     if  a!=0 and b!=0:   
#         s=(a+b)/2
#         print("arifmetigi=",s)
#     return s
    
   
# m=mean(a,b)
# print(m)
# 4
# from math import *
# a=float(input("a="))
# def  uchburchak(a):
#     s=0
#     if a>0:
#         s=3*a
#         print("peremetri=",s)
#     if a>0:
#         s=a*sqrt(3)/4
#         print("yuzasi=",s)
#     return s
# uchburchak(a)
#  5
# n=int(input("n="))
# m=int(input("m="))
# def ekub(n,m):

#     while (n>=m):
#         q=n%m
#         if q==0:
#             ekubson =m 
#             break
#         else:
#             n==m
#             m==q
#     return ekubson
# num = ekub(n,m)
# print("ekub",num)        

# 5
# from math import *
# x1=int(input("x1="))
# x2=int(input("x2="))
# y1=int(input("y1="))
# y2=int(input("y2="))

# def pectps(x1,x2,y1,y2):
#     a=fabs(x1-x2)
#     b=fabs(y1-y2)
#     s=a*b
#     p=(a+b)*2
#     return s, p

# m=pectps(x1,x2,y1,y2)
# print("natija=",m)

# 18
# r=int(input("r="))
# p=3.14

# def Doira(r,p):
#     s=p*r*r
#     return s
# m=  Doira(r,p) 
# print("doira yuzasi=",m)
# 17
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# def kavadrattenglama(a,b,c):
#     d=b*b-4*a*c
#     if (d>0):
#         return ("ildizi=2")
#     if (d<0):
#         return("yechimga ega emas")
#     if (d==0):
#         return("bitta yechim")
#     return d    
# n=kavadrattenglama(a,b,c)
# print(n)
# 16

# a=int(input("a="))
# b=int(input("b="))

# def ishora(son):
#     if (son>0):
#         a=1
#     if (son<0):
#         a=-1

#     if (son==0):
#         a=0
#     return a
# ishora(a)
# ishora(b)
# print(ishora(a)+ishora(b))
#19

# r1=int(input("r1="))
# r2=int(input("r2="))
# p=3.14
# def Rings(r1,r2,p):
#     s1=p*r1*r1
#     s2=p*r2*r2
#     if s1>s2:
#         n=s1-s2
#         return n
#     if s2>s1:
#         n=s2-s1
#         return n
# m=Rings(r1,r2,p)
# print(m)
# a=int(input("a="))
# b=int(input("b="))
# def perimetr(a,b):
#     c=sqrt(a*a+b*b)
#     p=a+b+c
#     return p
# n=perimetr(a,b)
# print("p===",n)
#22
# from math import *
# a=int(input("a="))
# b=int(input("b="))
# op=int(input("op="))
# def cals(a,b,op):
#     if (op==1):
#         s=fabs(a-b)
#     if (op==2):
#         s=a*b
#     if (op==3):
#         s=a/b
#     return s
# m=cals(a,b,op)
# print("natija =",m)
# 23
# x=int(input("x="))
# y=int(input("y="))
# def chorak(x,y):
#     if x>0 and y>0:
#         return 1
#     if y>0 and x<0:
#         return 2
#     if y<0 and x<0:
#         return 3
#     if x>0 and y<0:
#         return 4
# m=chorak(x,y)    
# print("choragi=",m)

# 24
# n=int(input("n="))
# def even(n):
   
#     if n%2==0:
#         print("juft")
#         return ("true")
#     else:
#         print("toq")
#         return ("false")
# m= even(n)  
# print("natija=",m)

# 25
# from math import *
# a=int(input("a="))
# def IsSquare(a):
    
#     if a==pow(n,2):
#         return ("true")
#     else:
#         return ("fale")
# m=IsSquare(a)
# print("natija",m)
# 6
# n=int(input("n="))
# def digitCoutSum(son):
#     raqamSoni=0
#     sum=0
#     while (son!=0):
#         raqamSoni+=1
#         son=int(son/10)
#     print("raqamlar soni=",raqamSoni)
#     print("raqamlar sum",sum)
# digitCoutSum(n)

# 7

# def digitcout(number):
#     coutNum/=0

# a=int(input("a="))
# b=int(input("b="))

# def almashtir(d,c):
#     a,b=d,c
#     return c,d
# n=almashtir(a,b)
# print(n)

# 25
# k = int(input("k = "))
# def isSquare(k):
#     bor = False
#     for x in range(1, int(k / 2)):
#         if x ** 2 == k:
#             bor = True
#             break
#     return bor, x

# print(isSquare(k))
# 26
# k = int(input("k = "))
# def isSquare(k):
#     bor = False
#     for x in range(1, int(k / 2)):
#         if 5 ** x == k:
#             bor = True
#             break
#     return bor, x
# print(isSquare(k))

# 27
# k = int(input("k = "))
# n = int(input("n="))
# def isSquare(k):
#     bor = False
#     for x in range(1, int(k / 2)):
#         if x ** k == n:
#             bor = True
#             break
#     return bor, x
# print(isSquare(k,n))    
# 28
# n=int(input("n="))
# def IsPrime(son):
#     tub=True
#     s=0
#     for x in range(2,son):
#         if son%x==0   : 
#             tub=False
#             break
#         return tub
# print(IsPrime(n) )


# 29
# n=float(input("n="))
# def digcout(n):
   
#    s=int(n)
#    return s
# print( digcout(n))

#30

# k=float(input("k="))
# def digcout(k):
#     s=k-int(k)
#     return s
# print( digcout(k))

#31











#32

# n=float(input("n="))
# p=3.14
# def degtorad(n):
#     s=n*p/180
#     return s
# print(degtorad(n))

#33

# n=float(input("n="))
# p=3.14
# def degtorad(n):
#     s=n*180/p
#     return s
# print(degtorad(n))

# 34

# n=int(input("n="))

# def Fact(n):
#     s=1
#     for x in range (1,n+1):
#         s*=x
#     return s
    
# print(Fact(n))

# 37
# from math import *
# a=int(input("a="))
# b=int(input("b="))
# def power1(a,b):
#     s=pow(a,b)
#     return s
# print(power1(a,b))

# 38
# n=int(input("n="))
# a=int(input("a="))
# def power1(a,n):
#     s=1

# 40

# def Fact(n):
#     s=1
#     for x in range (1,n+1):
#         s*=x
#     return s
# from math import *
# a=int(input("a="))
# n=int(input("n="))
# def Exp1(a,n):
#     s=0
#     for x in range(2,n+1):
#         s=pow(a,x)/Fact(x)
#         s+=x
#     return s

# print( Exp1(a,n))

# 41
# def Fact(n):
#     s=1
#     for x in range (1,n+1):
#         s*=x
#     return s
# from math import *
# a=int(input("a="))
# n=int(input("n="))
# def sin1(a,n):
#     s=0
#     for x in range(2,n+1):
#         s=pow(-1,x)*pow(a,(2*x+1))/Fact(2*x+1)
#         s+=s
#     return s

# print( sin1(a,n))

# 42
# def Fact(n):
#     s=1
#     for x in range (1,n+1):
#         s*=x
#     return s
# from math import *
# a=int(input("a="))
# n=int(input("n="))
# def cos1(a,n):
#     s=0
#     for x in range(2,n+1):
#         s=pow(-1,x)*pow(a,2*x)/Fact(2*x)
#         s+=s
#     return s

# print( cos1(a,n))

# 43

# def Fact(n):
#     s=1
#     for x in range (1,n+1):
#         s*=x
#     return s
# from math import *
# a=int(input("a="))
# n=int(input("n="))
# def Ln1(a,n):
#     s=0
#     for x in range(2,n+1):
#         s=pow(-1,x)*pow(a,(x+1))/(x+1)
#         s+=s
#     return s

# print( Ln1(a,n))

# 44

# def Fact(n):
#     s=1
#     for x in range (1,n+1):
#         s*=x
#     return s
# from math import *
# a=int(input("a="))
# n=int(input("n="))
# def Arctg1(a,n):
#     s=0
#     for x in range(2,n+1):
#         s=pow(-1,x)*pow(a,(2*x+1))/(2*x+1)
#         s+=s
#     return s

# print( Arctg1(a,n))

# 45
# def Fact(n):
#     s=1
#     for x in range (1,n+1):
#         s*=x
#     return s
# from math import *
# a=int(input("a="))
# n=int(input("n="))
# b=int(input("b="))
# def cos1(a,n,b):
#     s=0
#     for x in range(2,n+1):
#         s=(b-x+1)*pow(a,x)/Fact(x)
#         s+=s
#     return s

# print( cos1(a,n,b))

# 46

def Fact(n):
    s=1
    for x in range (1,n+1):
        s*=x
    return s


def ekub(firstNum, secondNum):

    while(firstNum >= secondNum):
        q = firstNum % secondNum
        if q == 0:
            ekubSon = secondNum
            break
        else:
            firstNum = secondNum
            secondNum = q
    return ekubSon
from math import *
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
def Frac1(a,b,c,d):
    Fact(a,b)
    Fact(c,d)
    s=Fact(a,b)/ Fact(c,d)
    return s 
print(Frac1(a,b,c,d))





























































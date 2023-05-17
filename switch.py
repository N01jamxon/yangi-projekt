# n=int(input("n="))
# a=int(input("a="))
# b=int(input("b="))
# pmax=(a+b)*2
# for x in range (2,n+1):
#     a=int(input("a="))
#     b=int(input("b="))
#     if (pmax<(a+b)*2):
#         pmax=(a+b)*2
# print(pmax)        

# minmax1
# n=int(input("n="))
# a=int(input("a="))
# max=a
# min=a
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (a>max):
#         max=a
#     if (a<min):
#         min=a
# print(min)
# print(max)
# minmax2
# n=int(input("n="))
# a=int(input("a="))
# b=int(input("b="))
# smin=a*b
# for x in range(2,n+1):
#     a=int(input("a="))
#     b=int(input("b="))
#     if (smin>a*b):
#         smin=a*b
# print(smin)
# min max 3
# n=int(input("n="))
# a=int(input("a="))
# b=int(input("b="))
# pmax=(a+b)*2
# for x in range(2,n+1):
#     a=int(input("a="))
#     b=int(input("b="))
#     if (pmax<(a+b)*2):
#         pmax=(a+b)*2
# print(pmax)
# min max 4
# n=int(input("n="))
# a=int(input("a="))
# qmax=1
# qmin=1
# min=a
# max=a
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (max<a):
#         max=a
#         qmax=x
#     if (min>a):
#         min=a
#         qmin=x  
# print("kichigi",min)
# print("orni",qmin)  
# min max 5
# n=int(input("n="))

# v=int(input("v="))
# m=int(input("m="))
# rmax=m/v
# for x in range(2,n+1):
    
#     v=int(input("v="))
#     m=int(input("m="))
#     if (rmax<m/v):
#         rmax=m/v
# print(rmax)
# min max 6
# n=int(input("n="))
# a=int(input("a="))
# qmax=1
# qmin=1
# min=a
# max=a
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (max<=a):
#         max=a
#         qmax=x
#     if (min>a):
#         min=a
#         qmin=x  
        
# print("kichigi",min)
# print("orni",qmin)  
# print("kattasi",max)
# print( "orni",qmax)
# min max 7
# n=int(input("n="))
# a=int(input("a="))
# qmax=1
# qmin=1
# min=a
# max=a
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (max<=a):
#         max=a
#         qmax=x
#     if (min>a):
#         min=a
#         qmin=x  
# print("kattasi",max)
# print( "orni",qmax)       
# print("kichigi",min)
# print("orni",qmin)  

# minmax 8
# n=int(input("n="))
# a=int(input("a="))
# qmax=1
# qmin=1
# min=a
# max=a
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (min>a):
#         min1=a
#         qmin=x
#     if (min>=a):
#         min=a
#         qmin=x  
# print(min1)
# print(qmin)
#min max 10
# n=int(input("n="))
# a=int(input("a="))
# max=a
# min=a 
# b=1
# c=1
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (max<a):
#         max=a
#         b=x
#     if (min>a):
#         min=a
#         c=x
# if max:
#     print(max)
# elif min:
#     print(min)
# minmax 12
# n=int(input("n="))
# q = 0
# musbat = False
# for x in range(1, n + 1):
#     a = int(input("a = "))
#     q += 1
#     if a > 0:
#        musbat = True
#        min = a
#        break


# for x in range(q + 1, n + 1):
#     a = int(input("a = "))

#     if a > 0:
#         if (min > a):
#             min = a

# if musbat:
#     print("Min = ", min)
# else:
#     print("0")
# min max 13
# n=int(input("n="))
# q=0
# musbat=False
# for x in range(1,n+1):
#     a=int(input("a="))
#     if a%2==1:
#         q+=1
#         max=a
#         if max<a:
#             max=a
# if q==0:
#     print("0")
# else:
#     print(max) 
# print(max)
# minmax 16

# n=int(input("n="))

# a=int(input("a="))
# s=1
# min=a
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (min>a):
#         min=a
#         s=x
# print("min",min)
# print("soni",s)

# minmax 17
# n=int(input("n="))
# a=int(input("a="))
# s=1
# max=a
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (max<=a):
#         max=a
#         s=x
# print("max",max)
# print("soni",s)

#minmax18
# n=int(input("n="))
# a=int(input("a="))
# d=1
# max=a
# s=1
# max=a
# for x in range(2,n+1):
#     a=int(input("a="))
#     if (max<=a):
#         max=a
#         s=x
#     if (max<a):
#         max=a
#         d=x
# print("max1",max)
# print("soni1",d)
# print("orasi",s-d)
    
# print("max",max)
# print("soni",s)

# min max 
n=int(input("n="))
a=int(input("a="))

max=a
maxsoni=0
min=a
minsoni=0
for x in range(2,n+1):
    a=int(input("a="))
    if (max<a):
        max=a
       
        maxsoni=x
    if (min>a):
        min=a
       
        minsoni=x
print(minsoni)        
print(maxsoni)















# sonlar=[1,4,7,9,3,5,7]
# s=1
# for x in range(0,len(sonlar)):
#     s*=sonlar[x]
# print("yigindisi",s)

# 1
# n=int(input("n="))
# toqsonlar=[]

# for x in range (0,n+1):

#     if x%2==1 :
#        toqsonlar=[x]
#        print(toqsonlar)
    
# 2
# from math import *
# n=int(input("n="))
# s=0
# s=list()
# for x in range (0,n+1):
#     s.append(pow(2, x))
# print(s)

# 3
# n=int(input("n="))
# a=int(input("a="))
# d=int(input("d="))
# arifmetik=[]
# 
# for x in range (0,n):
#     
#     
#     s.append(k)
# print(s)

# 4
# n=int(input("n="))
# a=int(input("a="))
# d=int(input("d="))
# s=list()
# k=0
# for x in range (0,n+1):
#     k=a*d
#     a=k
#     s.append(k)
# print(s)

# 7
# from math import *
# masiv=[2,5,8,11,14]

# for x in range(len(masiv)-1,-1,-1):
#    masiv=[x]
#    print(masiv) 
   
# 8
# teskari=[1,6,8,3,7,4,6,2]
# for x in range(1,len(teskari)):
#     if x%2==1:
#         teskari=[x]
        
#     print(teskari)

# kamayish=[1,2,3,4,5,6,7,8,9]
# from math import *
# for x in range(len(kamayish)-1,-1,-1):
#     if x%2==0:
#         kamayish=x
#         print(kamayish)
# 10
# kamayish=[1,2,3,4,5,6,7,8,9]
# from math import *
# for x in range(len(kamayish)-1,-1,-1):
#     if x%2==0:
#         kamayish=x
#         print( "jufti",kamayish)
#     elif x%2==1:
#         kamayish=x
#         print("toq",kamayish)

# 11
# h=[8,9,6,4,7,6,3,2,1,5,85,24]
# k=int(input("k="))
# from math import *
# for x in range(0,len(h)):
#     if (len(h)<=x*k):
#         break
#     print(h[x])


# 51
# a=[9,6,8,3,7,4,8]
# b=[6,9,3,4,8,2,1]
# for x in range (1,len(a)):
#     a[x],b[x]=b[x],a[x]
#     print("a=",a[x] )
#     print("b=",b[x])

# 52
# a=[6,9,5,7,2]
# b=[]
# for x in range(1,len(a)):
#     if a[x]<5:
#         b.append(a[x]*2)
#     else:
#         b.append(a[x]/2)
# print(b)  


# 53
# a=[5,6,9,8,3,4]
# b=[8,6,9,4,7,3]
# c=[ ]
# for x in range(1,len(a)-1):
#     if a[x]>b[x]:
#         c.append(a[x])
#     else:
#         c.append(b[x])
# print(c)

# 54
#n=[8,6,9,5,4,7,3,1,2,5,6]
# a=[]
# for x in range(1,len(n)-1):
#     if n[x]%2==0:
#         a.append(n[x])
# print(a)

# 55
#n=[8,6,9,5,4,7,3,1,2,5,6]
# a=[]
# for x in range(1,len(n)-1):
#     if n[x]%2==1:
#         a.append(n[x])
# print(a)
# 56

# # 57
# n=[1,2,3,4,5,6,7,8,9]
# a=[]
# for x in range(1,len(n),2):
#     a.append(n[x])
   
# for x in range(2,len(n),2):
#     a.append(n[x])
# print(a)

# 58
# a=[9,5,6,8,1,3]
# b=[ ]
# for x in range(0,len(a)):
#     b.append(a[x])
# print(b)

# 59
# a=[8,21,4,6,9,14,7]
# b=[]
# for x in range(0,len(a)):
#     b.append(int(a[x]/len(a)))
# print(b)
# 60
# massiv=[1,6,9,8,3,6,7]
# massivb=list()
# s=0
# for x in range(0,len(massiv)):
#     for y in range(x,len(massiv)):
#         s+=massiv[y]

#     massivb.append(s)
#     s=0
# print("massivb=",massivb)



# 61
# a=[9,8,2,6,7,6]
# b=[ ]
# s=0
# for x in range(len(a)):
#     s+=x
#     print(s)
#     b.append(s/len(a))
# 62
# massiv=[1,2,3,4,5,6,7]
# toqindex=-1
# for x in range(0,len(massiv)):
#     if massiv[x]%2==1:
#         toqindex=x
#         toqson=massiv[x]
# if (toqindex!=-1):
#     for x in range( 0,len(massiv)):
#         if massiv[x] % 2==1:
#             massiv[x]=massiv[x]+toqson

# print(massiv)

# 90
# n=[6,4,98,13,7,4,5]
# k=int(input("k="))
# for x in range(1,len(n)):
#     if k==x :
#         del n[x]
# print(n)
# 91
# n=[6,9,7,8,1,5,6,4,3,5,8]
# k=int(input("k="))
# m=int(input("m="))
# for x in range (1,len(n),-1):
#     for y in range (k,n+1):
#         del n[y]
# print(n)

# 92
# n=[1,5,8,9,6,7,3,4]
# for x in range(1,len(n)+1):
#     if x%2==1:
#         n.remove(x)
#     else:
#         print(x)   


# 93
# n=[1,5,8,9,6,7,3,4]
# m=[ ]
# for x in range(0,len(n)-1,2):
#     n.remove(n[x])
# 94

# 112
# n=[ 8,5,6,7,9,1,2,10,3,4]
# for x in range(0,len(n)):
#     for y in range (x,len(n)):
#         if n [y]<n[x]:
#             n[y],n[x]=n[x],n[y]
          
# print(n )        

n=[6,8,9,2,4,76,3]
m=[ ]
m.sort(n)
print(m)
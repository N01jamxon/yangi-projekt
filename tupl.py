# 20
# n=(6,3,5,4,8,2,1,5)
# k=int(input("k="))
# m=int(input("m="))
# f=list(n)
# s=0
# print(f)

# for x in range(k,m):
#     s+=f[x]
# print (s)    


#21
# n=(6,3,5,4,8,2,1,5)
# k=int(input("k="))
# m=int(input("m="))
# f=list(n)
# s=0
# h=0
# print(f)

# for x in range(k,m):
#     s+=f[x]
#     h+=1
# print (s/h)    

# 22
# n=(6,3,5,4,8,2,1,5)
# k=int(input("k="))
# m=int(input("m="))
# f=list(n)
# s=0
# h=0


# for x in range(k,m):

#     s+=f[x]
# print(s)
# for x in range(0,len(f)) :
#     h+=f[x]
# print(h)



# print (h-s) 

# 23
# n=(1,2,3,4,5,6,7,8,9)
# k=int(input("k="))
# m=int(input("m="))
# f=list(n)
# s=0
# h=0
# t=0

# for x in range(k,m):

#     s+=f[x]
#     t+=1
# print(s)
# for x in range(0,len(f)) :
#     h+=f[x]
# print(h)



# print ((h-s)/(len(f)-t)) 

# 24
n=(1,2,3,4,5,6,7,8,9)
f=list(n)
ha=True
d=f[n+1]-f[n]
for x in range(0,len(f),-1):
    if d==f[x+1]-f[x]:
        ha=True
    print(d)




























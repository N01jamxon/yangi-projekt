# local max
# n=[5,9,6,7,8,3,4]
# localmax=0
# for x in range(1,len(n)-1):
#     if n[x]>n[(x-1)] and n[x]>n[(x+1)]:
#         print(n[x])
#         localmax+=1

        
# print("localmax=",localmax)

# 51
# a=[5,6,9,8,3,4]
# b=[8,6,9,4,7,3]
# c=[ ]
# for x in range(1,len(a)-1):
#     if a[x]>b[x]:
#         c.append(a[x])
#     else:
#         c.append(b[x])
# print(c)

# 55
n=[8,6,9,5,4,7,3,1,2,5,6]
a=[]
for x in range(1,len(n)-1):
    if n[x]%2==1:
        a.append(n[x])
print(a)






















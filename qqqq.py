# s=(input("n="))

# for x in range(0,len(s)+1):
#     for y in range(1,x+1):
#         print(y,end=" ")
#     print()   
    
# s=int(input("n="))
# m=s//2+s
# for x in range(10,s):
#     for z in range(10,m+1):
#         print(" ",end=" ")
#     for y in range(11,x+1):
#         print(y , end=" ")
#     for y in range(x+1,10,-1):
#         print(y, end=" ")
    
#     m-=1
#     print()
s=int(input("n="))
d="*"
m=s//2+s
for x in range(0,s):
    for z in range(0,m+1):
        print(" ",end=" ")
    for y in range(1,x+1):
        print(d , end=" ")
    for y in range(x+1,0,-1):
        print(d, end=" ")
    
    m-=1
    print()
m=s//2+s
for x in range(s,0,-1):
    for z in range(0,m+1):
        print(" ",end=" ")
    for y in range(1,x+1,-1):
        print(d , end=" ")
    for y in range(x+1,0,-1):
        print(d, end=" ")
    
    m-=1
    print()   









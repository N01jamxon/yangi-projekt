
# 1

# n=int(input("n="))
# s=0
# for x in range(1,n+1):
#     if n%x==0:
#         s =s+ x
#         print(x,end=" ")
# print("s=",s)
# 4
# n=int(input("n="))
# for x in range(1,n+1):
#     s=0
#     for y in range(1,x):
#         if x%y==0:
#             s=s+y
#     if s==x:
#         print(x, end=" ")
# 
# n=int(input("n="))
# for x in range(1,n+1):
#     if x%3==0 and x%5!=0 :
#         print("x=,",x,end=" ")

#
n=float(input("n="))
x=0
y=0
z=0
for a in range(1,n+1):
    for b in range (1,n+1):
        for c in range (1,n+1):
            if c*c==a*a+b*b or b*b==a*a+c*c or a*a==c*c+b*b:
                print(a,b,c, ) 































































































































# begin 13
# r1=float(input("r1="))
# r2=float(input("r2="))
# r1>r2
# p=3.14
# s1=p*r1
# s2=p*r2
# s3=p*(r1-r2)
# print("s1=",s1)
# print("s2=",s2)
# print("s3=",s3)
# begin 18
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# d=b-c
# e=c-a
# print("kopaytmasi",d*e)
#23
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# a, b, c = b, c, a
# print("a=",a)
# print("b=",b)
# print("c=",c)
#34
# x=float(input("x="))
# a=float(input("a="))
# y=float(input("y="))
# b=float(input("b="))
# if x==y:
#     d=a/b
# print("d=",d)
# integer
# x=int(input("x="))
# d=int(x/10)
# e=x%10

# print("yangi",e*10+d)
# integer 13
# x=int(input("x="))
# a=int(x/100)
# b=x%100
# print("yangisi",b*10+a)
# integer 16
# x=int(input("x="))
# a=int(x/100)
# d=x%100
# b=int(d/10)
# c=d%10
# print("yangisi",a*100+c*10+b)
# integer 18
# x=int(input("x="))
# a=int(x/1000)
# b=x%1000
# print("butun",a)
# print("kasr",b)
# integer 23
# n=float(input("n="))
# soat=int(n/3600)
# minut=int((n%3600)/60)
# sekunt=((n%3600)%60)
# print("soat",soat)
# print("minut", minut)
# print("sekunt",sekunt)
# integer 29
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# s1=a*b/2
# s2=c*c
# n=s1/s2
# s3=s1-s2*n
# print("n=",n)
# print("s3",s3)
# boolean17
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# n= not(a<0 and b<0 and c<0)
# print("n=",n)
# boolean 17
# a=float(input("a="))
# n= a%2==1
# m=int(a/100)
# d=a%100
# e=int(d/10)
# f=d%10
# print("3 xonali",n)
#boolean 28
# x=float(input("x="))
# y=float(input("y="))
# n=(x>0 and y>0)or(x<0 and y<0)
# print("n=",n)
# boolean33
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# n=(a+b>c and a+c>b and c+b>a)
# print("n=",n)
# boolean 37
# x1=float(input("x="))
# y1=float(input("y="))
# x2=float(input("x="))
# y2=float(input("y="))
# n= ( x2==x1+1 and y2==y1+1) or (x2==x1 and y2==y1+1)or(x2==x1-1 and y2==y1+1)or(x2==x1-1 and y2==y1)or(x2==x1-1 and y2==y1-1)or(x2==x1 and y2==y1-1)or(x2==x1+1 and y2==y1-1)or(x2==x1+1 and y2==y1)
# print("n=",n)
# if10
# a=int(input("a="))
# b=int(input("b="))
# if a!=b:
#     d=a+b
# else:
#     d=0    
#     print("a va b",a,b)
# print("d=",d)
# if 16
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if max==a and min==b:
#     d=a+c
# if max==a and min==c:
#     d=a+b
# if max==b and min==c:
#     d==b+a
# print("d=",d)
# if25
# x=float(input("x="))
# if x<-2 or x>2:
#     d=2*x
# else:
#     d=-3*x
# print("d=",d)
#case 10

# direction = input("Direction = ")
# command = int(input("Command = "))

# if direction == 's':
#     print("Shimol")
# if direction == 'j':
#     print("Janub")
# if direction == 'q':
#     print("Sharq")
# if command == 0:
#     print("Harakatni davom ettir ")
# if command == 1:
#     print("Chapga buril ")
# case 15
# m=int(input("m="))
# n=int(input("n="))
# a= m
# b= n
# if b==6:
#     print("olti")
# if b==7:
#     print("yetti")
# if b==8:
#     print("sakkiz")
# if b==9:
#     print("toqqiz")
# if b==10:
#     print("on")
# if b==11:
#     print("valet")  
# if b==12:
#     print("dama")
# if b==13:
#     print("qirol")   
# if b==14:
#     print("tuz")           
# if a==1:
#     print("gisht")
# if a==2:
#     print("olma")
# if a==3:
#     print("chillak")
# if a==4:
#     print("qarga")
#misol
# from math import*
# x=float(input("x="))
# a=1.5
# b=3.14
# j=0.65
# s=x*x*x*(sin/cos)*(sin/cos)(x+b)*(x+b)+a/sqrt(x+b)
# q= (b*x*x-a)/a*x
# print("s=",s)
# print("q=",q)
# from math import*
# m=2
# c=-1
# t=1.02
# b=0.17
# f=sqrt(m*(sin/cos)*t+fabs(c*sin*t))
# z=m*cos(b*t*sin*t)+c
# print("f=",f)
# print("z=",z)
# from math import*
# a=3.02
# b=17.15
# x=-4.28
# t=5
# y=b*(sin/cos)*(sin/cos)*x-a/sin*sin(x/a)
# s=b*sin(a*t*t*cos*2*t)-1






















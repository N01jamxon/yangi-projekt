# satr=input("satr=")
# satr1=input("satr1=")


# for x in range(0,len(satr)):
#     for y in range(0,len(satr1)):
#         if satr[x]==satr1[y]:
#             bor=True
#         else:
#             bor=False
# print(bor)

# 32
# s1=input("s1=")
# s2=input("s2=")
# soni=len(s2)
# s=0
# y=0
# bor= False
# nechtaligi=0
# for x in range(0,len(s1)):
#     if s1[x]==s2[y]:
#         s+=1
#         y+=1
#     else:
#         s=0
#         y=0
#     if s==soni:
#         y=0
#         bor=True
#         nechtaligi+=1
#         print("bor")

# if not bor:
#     print("yoq")
# print("netija =",nechtaligi)

33
# s1=input("s1=")
# s2=input("s2=")
# soni=len(s2)
# d=input("d=")
# s=0
# y=0
# bor= False

# for x in range(0,len(s1)):
#     if s1[x]==s2[y]:
#         s+=1
#         y+=1
#     else:
#         s=0
#         y=0
#     if s==soni:
#         y=0
#         bor=True
       
#         print("bor")
#         s1.append(s,d==d,s)

# if not bor:
#     print("yoq")
# print(s1)
# 34
# satr = "salom python";
# satr2 = "python"

# a = satr.find(satr2)
# satr3 = satr[0:a - 1]
# print(satr3)
# # 35
# satr = "salom python python";
# satr2 = "python"

# a = satr.find(satr2)
# satr3 = satr[0:a-1]
# print(satr3) 
# 37
# s1=" javohir qalesan yaxwimi"
# s2="yaxwimi"
# s3="darmet"
# d=" "
# a=s1.find(s2)
# d=s1[0:a-1]+s3

# print(d)

# 39
# s="javoq nma gap kin"
# s1=" "
# n = s.find(" ")
# n1 = s.find(" ", n +1)
# s1=s[n:n1]
# print(s1)

# 40
# s="javoq nma gap kin bolyappi "
# s1=" "
# n = s.find(" ")
# n1 = s.find(" ", len(s))
# s1=s[n:n1]
# print(s1)

# s=input("s=")
# s2=input("s2=")
# d=s.lower()
# n=d.count("a")
# print(n)

# s=input("s=")
# s2=input("s2=")
# f=s2.lower()
# d=s.lower()
# n=d.count(f)
# print(n)

# s="men 2004 yilman va '''/?"
# raqamlarson=0
# belgilarsoni=0
# harflarsoni=0
# for x in s:
#     if x.isdecimal()==True :

#         raqamlarson+=1
#     if x.isalpha()==True :
#         harflarsoni+=1

#     if  x.isalnum()==False  :
#         belgilarsoni+=1

# print("raqamlar=", raqamlarson)
# print("belgilar=", belgilarsoni)
# print("hrflar=", harflarsoni)

# 41
# s=input("s=")
# belgi=0
# sozlar=0
# for x in s:
#     if  s.isalnum()==False  :
#         if x==" ":
#             belgi+=1
# sozlar=belgi+1
# print("sozlar soni=", sozlar)
        
# 42
# satr = "java pythonp c++ c# pghrydgp jbnshsuywgj"

# massiv = satr.split(" ")
# print(massiv)
# soni = 0
# for x in range(0, len(massiv)):
#     for y in range(x + 1, len(massiv)):
#         if massiv[x][0] == massiv[y][0] and massiv[x][-1] == massiv[y][-1]:
#             print(massiv[x], massiv[y], soni)
#             soni += 1

# print("soni = ", soni)

# 43
# d="ASAL AYIQ YALADI ASAL ARI TALADI"
# s=d.split(" ")
# f=0
# for x in range(0,len(s)):
#     for y in range(0,len(s[x])):
#         if s[x][y]=="A":
#             f+=1
#             break
# print(f)
# 44
d="ASALA  AYIQ YALADAI ASAL ARI TALADI"
s=d.split(" ")
f=0
a=0
for x in range(0,len(s)):
    for y in range(0,len(s[x])):
        if s[x][y]=="A":
            f+=1
        if f==3 :
            a+=1
            
print(a)
            












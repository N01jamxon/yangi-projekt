
# matrix={ 
#     "0" : 15,
#     "1" : 20,
#     "2" : 30,
#     "3" : 20,
# }

# print(matrix)

# d=dict()
# s=0
# for x in matrix.values():
#     s+=x
# print(s)


# matrix={ 
#     6 : 15,
#     1 : 20,
#     2 : 30,
#     3 : 20,
# }

# # print(matrix)

# d=dict()
# s=0
# for x in matrix.keys():
#     s+=x
# print(s)


# matrix={ 
#     6 : 15,
#     1 : 20,
#     2 : 30,
#     3 : 20,
# }

# # print(matrix)

# d=dict()
# s=0
# for x in matrix.values():
#     if x%2==0:
#         s+=x
# print(s)

# matrix={ 
#     6 : 15,
#     1 : 20,
#     2 : 30,
#     3 : 20,
# }

# # print(matrix)

# d=dict()
# min=3
# for x in matrix.keys():
#     if min>x:
#         min=x
#         print(min)
# matrix ["eng kichik ki"]=min      
# print(matrix)
import json
import requests
sorov=requests.get("https://api.covid19india.org/state_district_wise.json")
print(sorov.json)





























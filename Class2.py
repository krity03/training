# try catch
# try:
#     a=4
#     b=5
#     print(isinstance(a, int))
#     raise Exception()
# except:
#     print("There was an exception")
# finally:
#     print("This runs anyways")


# 
# data = [1,2,3,4,5, 'Hello']
# try:
#     for i in data:
#         if(isinstance(i, str)):
#             print("The value is integer")
#         else:
#             raise Exception()
# except:
#     print("There is string in the list")

# Class
# class MyClass:
#     x=6

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"
    
# p1 = Person("Bob", 109)

# print(p1.name)
# print(p1)

# a = min(1,2,3)
# b = max(1,2,3)
# print(a)
# print(b)

# Libraries
# import math
# print(math.sqrt(84))

# 
# import datetime
# print(datetime.datetime.now())

# 
# import json

# jsondata = '{"brand" : "ford" , "name" : "ram"}'

# a = json.loads(jsondata)
# print(a['brand'])
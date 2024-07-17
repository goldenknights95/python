# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:55:02 2024

@author: rajau
"""

dict1={
       "animal":"dog","breed":"german sheford","age":12
       }
print(dict1)
print("item in dict1:\n")
x=dict1.items()
print(x)

print("keys point in dict1:\n")
y=dict1.keys()
print(y)
print("values in dict1:\n")
z=dict1.values()
print(z)

dict1["age"]=14
print(dict1)

dict1.pop("breed")
print(dict1)
del dict1


# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:48:18 2024

@author: dkte
"""
"""updating tuples"""
print("for updating and editing tuples")

x =(1,2,3,65,2,50)
y=list(x)
print(y)
y[3]=100
z=tuple(y)
print(z)

"""
Unpacking of tuples
"""
print("for unpacking of tuple")
x1=(1,2,34,4,3)
print(x1)
(a,b,c,d,e)=x1;
print(a)
print(b)

#astarisk(*)
print("for Astarisk")
x2=(1,2,3,4,5,6)
(a1,b1,*c1)=x2;

print(a1)
print(b1)
print(c1)
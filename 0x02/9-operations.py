#!/usr/bin/python3
""" a file containing set operations in python"""


a = {1, 2,2 , 3, 3, 3 }
b = {3,4, 5, 5}

print(a.intersection(b))

print(a.union(b))

print(a.difference(b))

b.add(7)

print(b)

print(a&b)
print(a|b)

#a.clear()

print(a.issubset(b))

a.update(b)
print(a)

b.add(a)

print(b)
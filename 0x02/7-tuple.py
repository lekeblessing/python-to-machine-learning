#!/usr/bin/python3
"""a file that explaons tuple in python"""


fruits = ("orange", "guava", "mango")
print(type (fruits))
print(fruits[-1])
print(len(fruits))
# fruits[2] = "apple"

fruits.append("apple")
print(fruits)

name, age, level = ("John Peter", 25, 12)
print(name)
print(age)
print(level)
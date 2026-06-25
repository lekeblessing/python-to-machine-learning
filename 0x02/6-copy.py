#!/usr/bin/python3
"""a file that contains how to copy list in python"""


num = [1,2,3,4,5,6,7]
matrix = [[2,3,4], [5,6,7], [8,9,0]]
copy_num = num.copy()

num[6] = 10
print(num)
print(copy_num)
print(num[::-1])

print(matrix[2][2])
#!/usr/bin/python3
""" a file that contains dictionary operations in python"""


food = {
    "african":"rice",
    "asian": "pasta",
    "european": "bread"
}

print(food)
food.pop("asian")

print(food)
food.popitem()
print(food)
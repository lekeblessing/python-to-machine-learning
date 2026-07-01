#!/usr/bin/python3
""" a file that contains keys in python"""


user = dict(
    userName = "xyz",
    email = "xyz@abc",
    password = "admin"
)
print(user.keys())
print(user.values())


collection = dict.fromkeys(["location","size", "type"])
print(collection)
#!/usr/bin/python3
""" a file that contains dictionary in python"""


student = {
    "name": "James",
    "age": 27,
    #"email":"abc@xyz.com",
    "siblings": ["Aisha", "Nuhu"]
}
print(type (student))
print(student["name"], student["age"])
print(student.get("email"))

car = dict()
print(type(car))
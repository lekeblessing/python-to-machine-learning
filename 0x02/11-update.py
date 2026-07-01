#!/usr/bin/python3
"""a file  that contains update dictionary in python"""


car = dict(
    model = "Camry",
    make =  "Toyota",
    mileage = 45000,
    price = 3000,
    colour = "Grey"
)
print(car)
car.update({"price":3200})
print(car)

car["price"] =3400
print(car)
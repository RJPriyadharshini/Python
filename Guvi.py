"""Shape	Area	Perimeter
Circle	A = π × r2	Circumference = 2πr"""

# OOPS CONCEPT
"""Create a python program called circle with constructor which will take a list an argument
From the given list create two class methods area and perimeter which will belong to calculate area and perimeter"""


class Circle:
    pi = 3.141

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = Circle.pi * radius * radius
        return area

    def perimeter(self):
        circumference = 2 * Circle.pi * self.radius
        return circumference


list = [10, 501, 22, 37, 100, 999, 87, 351]
for radius in list:
    circle_obj = Circle(radius)
    print(f"Radius: {radius}")
    print(f"Area: {circle_obj.area()}")
    print(f"Perimeter: {circle_obj.perimeter()}")
    print("------")













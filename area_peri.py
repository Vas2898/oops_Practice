import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimetre(self):
        return 2 * math.pi * self.radius

radius = float(input("Enter radius : "))

circle = Circle(radius)

area = circle.calculate_area()
peri = circle.calculate_perimetre()

print(area)
print(peri) 

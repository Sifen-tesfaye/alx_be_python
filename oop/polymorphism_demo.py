import math
#Base class
class Shape:
    def area(self):
       return 0
#Rectangle subclass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
#Circle subclass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
                
#demonstration of polymorphism
shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(f"Area: {shape.area()}")


        

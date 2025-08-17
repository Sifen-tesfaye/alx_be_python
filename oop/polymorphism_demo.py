import math
#Base class
class shape:
    def area(self):
        raise NotImplementedError("Subclasses must override area()")
#Derived class - Rectangle
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
#Derived class - Circle
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
if __name__ == "__main__":
    shapes = [Rectangle(4, 5), Circle(3)]
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area()}")

        

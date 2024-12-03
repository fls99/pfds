from abc import ABC, abstractmethod


class Quadrilateral(ABC):
    def __init__(self, a, b, h):
        self.a = int(a)
        self.b = int(b)
        self.h = int(h)

    @abstractmethod
    def area(self):
        pass

class Rectangle(Quadrilateral):
    def __init__(self, a, b, h):
        super().__init__(a, b, h)
    
    def area(self):
        return self.a * self.b

class Parallelogram(Quadrilateral):
    def __init__(self, a, b, h):
        super().__init__(a, b, h)
    
    def area(self):
        return self.b * self.h

class Trapezium(Quadrilateral):
    def __init__(self, a, b, h):
        super().__init__(a, b, h)
    
    def area(self):
        return ((self.a + self.b)*self.h)/2

quads = input().split(sep=",")
areas = []
for quad in quads:
    print(quad)
    quad_specs = quad.strip().split(sep=" ")
    
    if quad_specs[0] == "rectangle":
        rect = Rectangle(a=quad_specs[1], b=quad_specs[2], h=quad_specs[3])
        areas.append(int(rect.area()))
    elif quad_specs[0] == "parallelogram":
        para = Parallelogram(a=quad_specs[1], b=quad_specs[2], h=quad_specs[3])
        areas.append(int(para.area()))
    elif quad_specs[0] == "trapezium":
        trap = Trapezium(a=quad_specs[1], b=quad_specs[2], h=quad_specs[3])
        areas.append(int(trap.area()))

print(areas)


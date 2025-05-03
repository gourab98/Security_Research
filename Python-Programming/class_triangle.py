class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5* self.base * self.height
    def __add__(self, other):
        return self.area() + other.area()

triangle1 = Triangle(10,5)
triangle2 = Triangle(6,8)

print("The area of Triangle 1 is:", triangle1.area())
print("The area of Triangle 2 is:", triangle2.area())
print("The area od both triangle is:",triangle1 + triangle2)
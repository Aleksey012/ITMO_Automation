class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def square(self):
       return self.h * self.w
    def perimetr(self):
        return self.h + self.w * 2

obj1 = Rectangle(200, 100)
obj2 = Rectangle(20, 50)
obj3 = Rectangle(35, 11)

print(obj1.square(), obj1.perimetr())
print(obj2.square(), obj2.perimetr())
print(obj3.square(), obj3.perimetr())

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def additional(self):
        return print(self.a + self.b)
    def multiplication(self):
        return print(self.a * self.b)
    def division(self):
        return print(self.a / self.b)

    def subtraction(self):
        return print(self.a - self.b)











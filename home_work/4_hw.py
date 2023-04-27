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




class Bar:
    def __init__(self, text, tip='knopka', loc=('')):
        self.text = text
        self.tip = tip
        self.loc = loc

    def push(self):
        return print('Клик по кнопке')

k1 = Bar('Text Box')
k2 = Bar('Check Box')
k3 = Bar('Radio Button')
k4 = Bar('Web Tables')
k5 = Bar('Buttons')
k6 = Bar('Links')
k7 = Bar('Broken Links - Images')
k8 = Bar('Upload and Download')
k9 = Bar('Dynamic Properties')

print(k1.text)
print(k2.text)
print(k3.text)
print(k4.text)
print(k5.text)
print(k6.text)
print(k7.text)
print(k8.text)
print(k9.text)

k1.push()
k2.push()
k3.push()
k4.push()
k5.push()
k6.push()
k7.push()
k8.push()
k9.push()


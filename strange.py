class MyClass:
    x = 123

    def setX(self, value):
        x = value

a = MyClass()
print(a.x)

b = MyClass()
print(b.x)

a.x = 456
b.x = 789

print(MyClass.x, a.x, b.x)

a.setX(10)
b.setX(20)

print(MyClass.x, a.x, b.x)

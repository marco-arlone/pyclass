class MyClass:
    x = 123

a = MyClass()
print(a.x)

b = MyClass()
print(b.x)

a.x = 456
b.x = 789

print(MyClass.x)
print(a.x)
print(b.x)

# -----------------------------------------------------------------------------
#   MyClass
# -----------------------------------------------------------------------------
class MyClass:

    classVar = 0

    def __init__(self, arg):
        MyClass.classVar += 1
        self.instVar = arg

    def __del__(self):
        MyClass.classVar -= 1

    def __str__(self):
        return f'{self.__class__.__name__}: classVar={MyClass.classVar} instVar={self.instVar}'
    
    def ClassMethod():
        print(f'ClassMethod classVar={MyClass.classVar}')

    def InstMethod(self):
        print(f'InstMethod: classVar={MyClass.classVar} instVar={self.instVar}')

# -----------------------------------------------------------------------------

a = MyClass(10)
print(a)

b = MyClass(20)
print(b)

c = MyClass(30)
print(c)

MyClass.ClassMethod()

a.InstMethod()

del c
del b

MyClass.ClassMethod()

a.InstMethod()

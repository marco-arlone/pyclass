class MyClass:

    def __init(self):
        pass

    def Method(self):
        pass

    def ClassInfo(self):
        print(f'Module: {self.__module__}')
        print(f'Class: {self.__class__}')

    def MethodInfo(self):
        print(f'Module: {self.Method.__module__}')
        print(f'Class: {self.Method.__class__}')
        print(f'Name: {self.Method.__name__}')

obj = MyClass()

obj.ClassInfo()
obj.MethodInfo()

print(dir(obj))
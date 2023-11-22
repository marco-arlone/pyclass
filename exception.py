from enum import Enum, unique

# -----------------------------------------------------------------------------
#   MyClassExc
# -----------------------------------------------------------------------------
class MyClassExc(Exception):

    @unique
    class Code(Enum):
        NoError = 0
        ValueTooHigh = 1
        ValueTooLow = 2
        InvalidOperation = 3

    __dictMsg = {
        Code.NoError: "No error",
        Code.ValueTooHigh: "Value too high",
        Code.ValueTooLow: "Value too low",
        Code.InvalidOperation: "Invalid operation for this value",
    }

    def __init__(self, code):
        self.__code = code

    def __get_code(self):
        return self.__code
    
    code = property(__get_code)

    def __str__(self):
        s = MyClassExc.__dictMsg[self.__code]
        return f'Error {self.__code.value}: {s}'

# -----------------------------------------------------------------------------
#   MyClass
# -----------------------------------------------------------------------------
class MyClass:

    def __init__(self, a=0):
        self.__set_a(a)

    def __set_a(self, a):
        if a < 0:
            raise MyClassExc(MyClassExc.Code.ValueTooLow)
        elif a > 10:
            raise MyClassExc(MyClassExc.Code.ValueTooHigh)
        else:
            self.__a = a

    def __get_a(self):
        return self.__a
    
    a = property(__get_a, __set_a)

    def Increment(self):
        self.__set_a(self.__a + 1)

    def Reciprocal(self):
        try:
            return 1 / self.__a
        except ZeroDivisionError as e:
            raise MyClassExc(MyClassExc.Code.InvalidOperation)

# -----------------------------------------------------------------------------

print('- Create an instance with initializer too high')
try:
    obj = MyClass(100)
except MyClassExc as e:
    print(e)

print('- Set property too low')
try:
    obj = MyClass()
    obj.a = -3
except MyClassExc as e:
    print(e)

print('- Increment value until it crashes')
try:
    obj = MyClass(5)
    for i in range(10):
        obj.Increment()
except MyClassExc as e:
    print(e)

print('- 0 reciprocal ')
try:
    obj = MyClass()
    print(obj.Reciprocal())
except MyClassExc as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

print('- Division by zero ')
try:
    obj = MyClass(100 / 0)
except MyClassExc as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

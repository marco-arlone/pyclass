import math

# Class Vect3
class Vect3:

    # Constructor
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    # Informal string rapresentation
    def __str__(self):
        return f'[{self.__x}, {self.__y}, {self.__z}]'

    # Official string rapresentation
    def __repr__(self):
        return f'{self.__class__.__name__}({self.__x}, {self.__y}, {self.__z})'

    # x getter
    def __get_x(self):
        return self.__x

    # x setter
    def __set_x(self, x):
        self.__x = x

    # x property
    x = property(__get_x, __set_x)

    # y getter
    def __get_y(self):
        return self.__y

    # y setter
    def __set_y(self, y):
        self.__y = y

    # y property
    y = property(__get_y, __set_y)

    # z getter
    def __get_z(self):
        return self.__z

    # z getter
    def __set_z(self, z):
        self.__z = z

    # z property
    z = property(__get_z, __set_z)

    # Absolute value
    def abs(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    # Overloading + operator
    def __add__(self, o):
        return Vect3(self.__x+o.__x, self.__y+o.__y, self.__z+o.__z)

    # Overloading - operator
    def __sub__(self, o):
        return Vect3(self.__x-o.__x, self.__y-o.__y, self.__z-o.__z)

    # Overloading * operator
    def __mul__(self, o):
        return self.__x * o.__x + self.__y * o.__y + self.__z * o.__z

    # Overloading == operator
    def __eq__(self, o):
        return self.__x == o.__x and self.__y == o.__y and self.__z == o.__z

    # Overloading != operator
    def __ne__(self, o):
        return self.__x != o.__x or self.__y != o.__y or self.__z != o.__z

# ----------------------------------------------------------
              
a = Vect3(1, 2, 3)
b = Vect3(z=6, y=5, x=4)

print(a, b)
print(str(a), str(b))
print(repr(a), repr(b))

print(a.abs())

print(a + b)
print(a - b)
print(a * b)

print(a == a)
print(a == b)

c = Vect3()
c.x = 10
c.y = 20
c.z = 30
print(c.x, c.y, c.z)

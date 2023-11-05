import math

# Class Vect3
class Vect3:

    # Constructor
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    # x setter/getter
    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        self.__x = x

    x = property(__get_x, __set_x)

    # y setter/getter
    def __get_y(self):
        return self.__y

    def __set_y(self, y):
        self.__y = y

    y = property(__get_y, __set_y)

    # z setter/getter
    def __get_z(self):
        return self.__z

    def __set_z(self, z):
        self.__z = z

    z = property(__get_z, __set_z)

    # String
    def __str__(self):
        return f'{self.__class__.__name__}({self.__x}, {self.__y}, {self.__z})'

    # absolute value
    def abs(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2 + self.__x ** 2)

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
    def __eq__(self, o):
        return self.__x != o.__x or self.__y != o.__y or self.__z != o.__z

# ----------------------------------------------------------
              
a = Vect3(1, 2, 3)
b = Vect3(4, 5, 6)

print(a, b)

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

import math

# -----------------------------------------------------------------------------
#   Shape
# -----------------------------------------------------------------------------
class Shape:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'{self.__class__.__name__}: x={self.__x} y={self.__y}'

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        self.__x = x

    x = property(__get_x, __set_x)

    def __get_y(self):
        return self.__y

    def __set_y(self, y):
        self.__y = y

    y = property(__get_y, __set_y)

    def Move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def Area(self):
        return None

    def __get_perimeter(self):
        return None
    
    perimeter = property(__get_perimeter)

# -----------------------------------------------------------------------------
#   Square
# -----------------------------------------------------------------------------
class Square(Shape):

    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.__side = side

    def __str__(self):
        return f'{self.__class__.__name__}: x={self.x} y={self.y}, side={self.__side}'

    def __get_side(self):
        return self.__side

    def __set_side(self, side):
        self.__side = side

    side = property(__get_side, __set_side)

    def Area(self):
        return self.__side ** 2

    def __get_perimeter(self):
        return self.__side * 4
    
    perimeter = property(__get_perimeter)

# -----------------------------------------------------------------------------
#   Circle
# -----------------------------------------------------------------------------
class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius

    def __str__(self):
        return f'{self.__class__.__name__}: x={self.x} y={self.y}, radius={self.__radius}'

    def __get_radius(self):
        return self.__radius

    def __set_radius(self, radius):
        self.__radius = radius

    radius = property(__get_radius, __set_radius)

    def Area(self):
        return  math.pi * self.__radius ** 2

    def __get_perimeter(self):
        return 2 * math.pi * self.__radius
    
    perimeter = property(__get_perimeter)

# -----------------------------------------------------------------------------

s1 = Shape(10, 20)
print(s1)
print(s1.Area())
print(s1.perimeter)

sq1 = Square(30, 40, 10)
print(sq1)
print(sq1.Area())
print(sq1.perimeter)

circ1 = Circle(50, 60, 10)
print(circ1)
print(circ1.Area())
print(circ1.perimeter)


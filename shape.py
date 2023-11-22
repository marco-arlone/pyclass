import math

# -----------------------------------------------------------------------------
#   Shape
# -----------------------------------------------------------------------------
class Shape:

    # Contructor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # Human readable rapresentation
    def __str__(self):
        return f'{self.__class__.__name__}: x={self.__x} y={self.__y}'

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

    # Move by an offset
    def Move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Draw method
    def Draw(self):
        pass

# -----------------------------------------------------------------------------
#   Square
# -----------------------------------------------------------------------------
class Square(Shape):

    # Constructor
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.__side = side

    # Human readable rapresentation
    def __str__(self):
        return f'{self.__class__.__name__}: x={self.x} y={self.y}, side={self.__side}'

    # side getter
    def __get_side(self):
        return self.__side

    # side setter
    def __set_side(self, side):
        self.__side = side

    # side property
    side = property(__get_side, __set_side)

    # Draw method
    def Draw(self):
        print(f'Draw Square -> {self}')

# -----------------------------------------------------------------------------
#   Circle
# -----------------------------------------------------------------------------
class Circle(Shape):

    # Contructor
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius

    # Human readable rapresentation
    def __str__(self):
        return f'{self.__class__.__name__}: x={self.x} y={self.y}, radius={self.__radius}'

    # radius getter
    def __get_radius(self):
        return self.__radius

    # radius setter
    def __set_radius(self, radius):
        self.__radius = radius

    # radius property
    radius = property(__get_radius, __set_radius)

    # Draw method
    def Draw(self):
        print(f'Draw Circle -> {self}')

# -----------------------------------------------------------------------------

l = []

l.append(Shape(10, 20))
l.append(Square(30, 40, 10))
l.append(Circle(50, 60, 10))
l.append(Square(70, 80, 20))
l.append(Circle(90, 100, 20))

print('- PRINT')
for s in l:
    print(s)

print('- MOVE 1, 3')
for s in l:
    s.Move(1, 3)

print('- PRINT')
for s in l:
    print(s)

print('- DRAW')
for s in l:
    s.Draw()

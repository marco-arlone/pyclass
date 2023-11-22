# -----------------------------------------------------------------------------
#   Base
# -----------------------------------------------------------------------------
class Base:

    def __init__(self, a):
        self.__a = a

    def __str__(self):
        return f'Base: a={self.__a}'

# -----------------------------------------------------------------------------
#   Derived
# -----------------------------------------------------------------------------
class Derived(Base):

    def __init__(self, a, b):
        super().__init__(a)
        self.__b = b

    def __str__(self):
        return f'Derived: a={self._Base__a} b={self.__b}'

# -----------------------------------------------------------------------------

x = Base(10)
print(x)

y = Derived(20, 30)
print(y)

class classSG1:

    def __init__(self, varRO, varRW):
        self.__varRO = varRO
        self.__varRW = varRW

    def __str__(self):
        return f'{self.__class__.__name__} varRO={self.__varRO} varRW={self.__varRW}'

    @property
    def varRO(self):
        return self.__varRO

    @property
    def varRW(self):
        return self.__varRW

    @varRW.setter
    def varRW(self, v):
        self.__varRW = v

obj = classSG1(123, 456)
print(obj)

print(obj.varRO)
print(obj.varRW)

obj.varRW = 789
print(obj.varRW)

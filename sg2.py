class classSG2:

    def __init__(self, varRO, varRW):
        self.__varRO = varRO
        self.__set_varRW(varRW)

    def __str__(self):
        return f'{self.__class__.__name__} varRO={self.__varRO} varRW={self.__varRW}'

    def __get_varRO(self):
        return self.__varRO

    def __get_varRW(self):
        return self.__varRW

    def __set_varRW(self, v):
        self.__varRW = v

    varRW = property(__get_varRW, __set_varRW)
    varRO = property(__get_varRO)

obj = classSG2(123, 456)
print(obj)

print(obj.varRO)
print(obj.varRW)

obj.varRW = 789
print(obj.varRW)

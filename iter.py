class MyIter:

    def __init__(self):
        self.__a = [10, 20, 30, 40, 50]
        self.__b = [60, 70, 80]

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i >= 0 and self.i < len(self.__a):
            x = self.__a[self.i]
            self.i += 1
        elif self.i >= len(self.__a) and self.i < len(self.__a) + len(self.__b):
            x = self.__b[self.i - len(self.__a)]
            self.i += 1
        else:
            raise StopIteration
        return x
    
    def __getitem__(self, i):
        if i >= 0 and i < len(self.__a):
            x = self.__a[i]
        elif i >= len(self.__a) and i < len(self.__a) + len(self.__b):
            x = self.__b[i - len(self.__a)]
        else:
            x = None
        return x
        
obj = MyIter()

print('--Begin--')
for i in obj:
    print(i)
print('--End--')

print(obj[2], obj[4], obj[10])
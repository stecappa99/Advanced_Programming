class Stack:
    def __init__(self, size):
        self.__size__ = size
        self.__top__ = 0
        self.__container__ = [0] * size

    def pop(self):
        self.__top__ -= 1
        return self.__container__(self.__top__)

    def push(self, e):
        self.__top__ += 1
        self.__container__[self.__top__ - 1] = e

    def __str__(self):
        return "Tуре :- " + type(self).__name__

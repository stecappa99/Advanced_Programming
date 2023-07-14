class Stack:
    def __init__(self, size):
        self.__size__ = size
        self.__top__ = 0
        self.__container__ = [0] * size

    def pop(self):
        self.__top__ -= 1
        return self.__container__[self.__top__]

    def push(self, e):
        self.__top__ += 1
        self.__container__[self.__top__ - 1] = e

    def __str__(self):
        return "\nTуре :- " + type(self).__name__ + ",\t\t\t" + str(self.__top__) +" / " +\
            str(self.__size__) + "\t\t\tcontainer :- [" + ", ".join(map(str, self.__container__[:self.__top__])) + "]"

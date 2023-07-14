from Stack import Stack
from EmptyStack import EmptyStack
from FullStack import FullStack
from ApplySpell import *

if __name__ == "__main__":
    print("")
    s = Stack(5)
    print(s)
    for elem in [25, 5, 7, 16, 1681]:
        s.push(elem)
        print(s)

    for _ in range(s.__size__):
        s.pop()
        print(s)

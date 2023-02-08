
class Counter(type):
    _count = 0

    def __new__(cls, classname, supers, classdict):
        classdict["__init__"] = cls.inc_count
        return type.__new__(cls, classname, supers, classdict)

    def inc_count(cls):
        Counter._count += 1
        print("count")


class Person(metaclass=Counter):
    def __init__(self):
        print("init")


if __name__ == "__main__":
    p1 = Person()
    p2 = Person()
    p3 = Person()
    p4 = Person()
    p5 = Person()
    p6 = Person()
    p7 = Person()
    p8 = Person()
    p9 = Person()
    print(Counter._count)


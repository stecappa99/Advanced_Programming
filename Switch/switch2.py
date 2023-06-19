import types


class Switch:
    def match(self, val):
        default_func = None
        for k, attr in type(self).__dict__.items():
            if type(attr) == types.FunctionType and "case_condition" in attr.__dict__:
                if attr.case_condition == "default":
                    default_func = attr.__get__(self)
                elif isinstance(attr.case_condition, (list, tuple, dict)):
                    if val in attr.case_condition:
                        return attr.__get__(self)
                elif val == attr.case_condition:
                    return attr.__get__(self)
        return default_func


def case(val):
    def inner(func):
        func.case_condition = val
        return func
    return inner


class N(Switch):
    @case(1)
    def jan(self): return "january"

    @case(2)
    def feb(self): return "feb"

    @case(3)
    def mar(self): return "march"

    @case("default")
    def d(self): return "default"

    def month(self, n): return self.match(n)()


class S(Switch):

    @case([12, 1, 2])
    def winter(self, n): return "{} comes in {}".format(N().month(n), "winter")

    @case([3, 5, 4])
    def spring(self, n): return "{} comes in {}".format(N().month(n), "spring")

    @case([8, 7, 6])
    def summer(self, n): return "{} comes in {}".format(N().month(n), "summer")

    @case([9, 10, 11])
    def fall(self, n): return "{} comes in {}".format(N().month(n), "fall")

    def season(self, n): return self.match(n)(n)


if "__main__" == __name__:
    # x = N()
    # print(x.month(1))
    # print(x.month(2))
    # print(x.month(3))
    # print(x.month(4))

    y = S()
    print(y.season(1))
    print(y.season(5))
    print(y.season(8))
    print(y.season(9))

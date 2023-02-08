import traceback

import sympy

def memoization(F):
    def wrapper(* args):
        if args not in wrapper.inner_cache.keys():
            wrapper.inner_cache[args] = F(*args)
        return wrapper.inner_cache[args]
    wrapper.inner_cache = dict()
    return wrapper


def logging(method):
    def inner(*args):
        with open("log.txt", "w") as f:
            f.writelines([a.__str__() for a in args])
        return method(*args)
    return inner


def stack_trace(method: classmethod):
    def inner(*args):
        traceback.print_stack()
        return method(*args)

    return inner


class MyMath:

    @memoization
    @logging
    @stack_trace
    def fib(self, n):
        return n if n < 2 else self.fib(n-1) + self.fib(n-2)

    @memoization
    @logging
    @stack_trace
    def fact(self, n):
        return 1 if n <= 1 else n * self.fact(n-1)


if __name__ == "__main__":
    m = MyMath()
    m.fib(3)
    m.fact(5)

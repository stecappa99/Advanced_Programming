import time


def logged(func):
    def inner(*args):
        print("Parameters are: {}".format(args))
        result = func(*args)
        print("Result is: {}".format(result))
        return result

    return inner


def timer(func):
    def inner(*args):
        st = time.time()
        result = func(*args)
        print("Method executes for {:.12f} sec".format(time.time() - st))
        return result

    return inner


class A:

    @logged
    def a(self, n):
        n += 1
        return n

    @timer
    def b(self, n):
        for i in range(n):
          x = i**n
        return x


if "__main__" == __name__:
    v = A()
    print(v.a(1))
    print(v.a(2))
    print(v.a(3))
    print(v.a(4))
    print(v.b(1000))

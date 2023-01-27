import functools


def sum_under_thousand():
    return sum(list(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(1, 1001))))


def sum_of_figures(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_figures(int(num/10))


def fib(a):
    return a if a <= 1 else fib(a-1) + fib(a-2)


if __name__ == "__main__":
    print(sum_under_thousand())
    print(sum_of_figures(2**1000))

# sin(x) can be approximate by the Taylor's series:
# sin(x) = x - (x^3/3!) + (x^5/5!) - (x^7/7!)...
# Let's write a library to implement sin(x, n) by using the Taylor's series (where n is the level of approximation, i.e., 1 only one item, 2 two items, 3 three items and so on).
# Let's compare your function with the one implemented in the math module at the growing of the approximation level.

# Hint. Use a generator for the factorial and a comprehension for the series.

import math

def gen_sign():
    x = 1
    while True:
        yield x
        x = -x


def gen_fact():
    fact = 1
    x = 1
    while True:
        yield fact
        x = x + 2
        fact = fact * (x-1) * x


def sin_taylor_series(x, n):
    fact = gen_fact()
    sign = gen_sign()
    return sum([next(sign)*(x**val)/(next(fact)) for val in range(1, (n*2)+1, 2)])


if __name__ == "__main__":
    print(sin_taylor_series(1, 100))
    print(math.sin(1))
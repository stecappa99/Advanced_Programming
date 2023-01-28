# Consider the number 6. The divisors of 6 are: 1, 2, 3 and 6.
# Every number from 1 up to and including 6 can be written as a sum of distinct divisors of 6: 1=1, 2=2, 3=1+2, 4=1+3, 5=2+3, 6=6.
# A number n is called a practical number if every number from 1 up to and including n can be expressed as a sum of distinct divisors of n.
# A pair of consecutive prime numbers with a difference of six is called a sexy pair (since "sex" is the Latin word for "six"). The first sexy pair is (23, 29).
# We may occasionally find a triple-pair, which means three consecutive sexy prime pairs, such that the second member of each pair is the first member of the next pair.
# We shall call a number n such that:
# (n-9, n-3), (n-3,n+3), (n+3, n+9) form a triple-pair, and
# the numbers n-8, n-4, n, n+4 and n+8 are all practical,
# an engineers' paradise.
# Find the sum of the first four engineers' paradises.
from itertools import combinations, chain


def prime_number(n):
    return len([x for x in range(2, int(n / 2)) if n % x == 0]) == 0


def gen_sexy_pair(start):
    n = start
    while True:
        if prime_number(n) and prime_number(n + 6):
            yield n, n + 6
        n = n + 1


def gen_triple_sexy():
    sexy_pair = gen_sexy_pair(0)
    ls = [next(sexy_pair), next(sexy_pair), next(sexy_pair)]
    while True:
        if ls[0][1] == ls[1][0] and ls[1][1] == ls[2][0]:
            yield ls
        ls = ls[1:]
        ls.append(next(sexy_pair))


def power_set(ls):
    return list(chain.from_iterable(combinations(ls, x) for x in range(1, len(ls)+1)))


def pratical_number(n):
    div = [x for x in range(1, n+1) if n % x == 0]
    sub_div = power_set(div)
    sub_div = list(map(lambda x: sum(x), sub_div))
    return n == len({x for x in range(1, n + 1) if x in sub_div})


if __name__ == "__main__":
    triple = gen_triple_sexy()
    eng_par = list()
    while len(eng_par) < 4:
        ls = next(triple)
        n = ls[0][0] - 9
        if len([x for x in range(-8, +9, 4) if pratical_number(n+x)]) == 5:
            eng_par.append(n)
    print(sum(eng_par))

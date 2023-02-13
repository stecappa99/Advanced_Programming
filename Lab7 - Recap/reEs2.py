import itertools


def prime(n):
    return not any([x for x in range(2, int(n**.5) + 1) if n % x == 0])


def under_primes(n):
    return [x for x in range(2, n) if prime(x)]


def goldbach(n):
    if not n % 2:
        b = under_primes(n)
        if any(b):
            a = itertools.combinations_with_replacement(b, 2)
            comb = list(itertools.chain(a))
            sup = list(map(lambda x: x[0] + x[1], comb))
            if n in sup:
                return comb[sup.index(n)]
    return None


def goldbach_list(n, m):
    return {k: goldbach(k) for k in range(n if not n % 2 else n+1, m + 1, 2)}


if __name__ == "__main__":
    for i in range(2, 30, 2):
        g = goldbach(i)
        if g is not None:
            print(f"{i} = {g}")

    print(goldbach_list(2, 30))
    

rows = lambda l, n, m: [[l[j+i*m] for j in range(m)] for i in range(n)]
def identity(size):
#return [[0 if a != b else 1 for a in range(size)] for b in range(size)]
    return rows([1 if x==y else 0 for x in range(size) for y in range(size)], size, size)


def square(n):
#return [[(n*b)+a+1 for a in range(n)] for b in range(n)]
    return rows([x for x in range(1, (n*n) + 1)], n, n)


def traspose_matr(matr):
    l = [matr[j][i] for i in range(len(matr)) for j in range(len(matr[0]))]
    return rows(l, len(matr[0]), len(matr))


def multiply(m1, m2):
    elem = lambda A, B, i, j: sum([A[i][k] * B[k][j] for k in range(len(A[0]))])
    return rows([elem(m1, m2, i, j) for i in range(len(m1)) for j in range(len(m2[0]))], len(m1), len(m2[0]))


if __name__ == "__main__":
    matrix = identity(4)
    print(matrix)
    print(square(5))
    print(traspose_matr([[1, 2], [3, 4]]))
    print(multiply(identity(4), square(4)))

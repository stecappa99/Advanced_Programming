
def toC(n): return n
def toK(n): return n + 273.15
def toF(n): return (n * (9/5)) + 32
def toR(n): return (n + 273.15) *(9/5)
def toN(n): return n * 33/100
def toD(n): return (100 - n) * (3/2)
def toRe(n): return n * 4/5
def toRo(n): return (n * 21/40) + 7.5

def fromC(n): return n
def fromK(n): return n - 273.15
def fromF(n): return (n - 32) * 5/9
def fromR(n): return (n - 491.67) * 5/9
def fromD(n): return (100 - n) * 2/3
def fromN(n): return n * 100/33
def fromRe(n): return n * 5/4
def fromRo(n): return (n - 7.5) * 40/21

allTo = { "C": toC, "K": toK, "F": toF, "R": toR, "D": toD, "N": toN, "Re": toRe, "Ro": toRo }
allFrom = { "C": fromC, "K": fromK, "F": fromF, "R": fromR, "D": fromD, "N": fromN, "Re": fromRe, "Ro": fromRo }

def table(pure_number, scale):
    grades = allTo[scale](pure_number)
    return [a(grades) for a in allFrom.values()]


if __name__ == "__main__" :
    print(table(0, "C"))
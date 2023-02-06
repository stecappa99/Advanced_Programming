class PascalTriangle:

    def __init__(self, value_max):
        self._max = value_max

    def __iter__(self):
        self._last = [1]
        return self

    def __next__(self):
        ls = self._last
        if self._max < len(ls) + 1:
            raise StopIteration
        support = [0, *self._last, 0]
        self._last = [support[i] + support[i + 1] for i in range(len(support) - 1)]
        return ls


if __name__ == "__main__":
    p = PascalTriangle(11)
    for i in p:
        print(i)

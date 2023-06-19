
class IteratorsCollection:

    def __init__(self, *it):
        self.iter = []
        self.index = 0
        for i in it:
            self.iter.extend(i)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.iter):
            raise StopIteration
        else:
            x = self.iter[self.index]
            self.index += 1
            return x


if "__main__" == __name__:
    i = IteratorsCollection(range(10), ["TEST"] * 10)
    print(*i)
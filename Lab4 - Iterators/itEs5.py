
class Product:

    def __init__(self, it):
        self.it = it
        self.result = 1
        self.index = 0
    def __iter__(self):
        self.result = 1
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.it):
            raise StopIteration
        else:
            self.result *= self.it[self.index]
            self.index += 1
            return self.result

def ProductGenerator(it):
    i, x, result = it, 0, 1
    while x < len(i):
        result *= i[x]
        yield result
        x += 1


if __name__ == "__main__":
    x = ProductGenerator(range(1, 100))
    for i in x:
        print(i)


class sortedDict(dict):

    def __init__(self, startingValues):
        for k, v in startingValues.items():
            self[k] = v

    def __setitem__(self, key, value):
        support = sorted(self.keys())
        pairs = []
        for k in support:
            if k > key:
                pairs.append(self.popitem())
        super().__setitem__(key, value)
        for k, v in pairs:
            super().__setitem__(k, v)


if __name__ == "__main__":
    d = sortedDict({2: "Two", 1: "One"})
    print(d)
    d[5] = "Five"
    d[3] = "Three"
    print(d)



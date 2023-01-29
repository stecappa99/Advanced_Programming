
class ShapeIterator:
    def __init__(self, ls, compare_op):
        self._index = 0
        self._ls = ls
        self._cmp = compare_op

    def __iter__(self):
        self._index = 0
        for shape in self._ls:
            shape.less_than = self._cmp.__get__(shape, type(shape))
        self._ls.sort()
        return self

    def __next__(self):
        while True:
            if self._index == len(self._ls):
                raise StopIteration
            res = self._ls[self._index]
            self._index = self._index + 1
            return res

    def set_compare(self, compare_op):
        self._cmp = compare_op

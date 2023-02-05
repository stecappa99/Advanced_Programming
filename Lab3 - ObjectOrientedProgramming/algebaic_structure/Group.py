import functools
import itertools

class Group:

    def __init__(self, s, op, i):
        self._set = s
        self._op = op
        self._identity = i

    def check_closure(self):
        return
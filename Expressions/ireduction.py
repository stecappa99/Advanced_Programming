operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
    "^": lambda x, y: x ** y,
}


class tree:

    def __init__(self, val, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r
        self.is_leaf = l is None and r is None

    def calculate_leaf_operation(self):
        if not self.is_leaf:
            if self.left.is_leaf and self.right.is_leaf:
                self.val = operations[self.val](self.left.val, self.right.val)
                self.left = None
                self.right = None
                self.is_leaf = True
            else:
                self.left.calculate_leaf_operation()
                self.right.calculate_leaf_operation()

    def __str__(self):
        return str(self.val) if self.is_leaf else "(" + self.left.__str__() + " " + str(self.val) + " " + self.right.__str__() + ")"


class calculator:
    def __init__(self, expr):
        _, self.builded_tree = self.build_tree(expr)
        self.tree = self.builded_tree

    def build_tree(self, expr):
        c = expr[0]
        if c.isdigit():
            return expr[1:], tree(int(c))
        else:
            expr, l = self.build_tree(expr[1:])
            expr, r = self.build_tree(expr)
            return expr, tree(c, l, r)

    def __iter__(self):
        self.tree = self.builded_tree
        return self

    def __next__(self):
        if self.tree.is_leaf:
            raise StopIteration
        else:
            self.tree.calculate_leaf_operation()

    def __str__(self):
        return self.tree.__str__()

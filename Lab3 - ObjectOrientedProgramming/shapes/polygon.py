import math


def create_polygon(n_edges, name):
    class polygon:
        def __init__(self, par_length):
            self._length = par_length

        def calculate_area(self):
            return .25*n_edges*self._length**2*math.tan(math.pi/n_edges)**-1

        def calculate_perimeter(self):
            return self._length * n_edges

        def __str__(self):
            return f"I'm a {name} and my area is {self.calculate_area()}"

        def __lt__(self, other):
            return self.less_than(other)

        def less_than(self, other): pass

    return polygon

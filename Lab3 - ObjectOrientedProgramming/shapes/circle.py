import math


class Circle:

    def __init__(self, par_radius):
        self._radius = par_radius

    def calculate_area(self):
        return (self._radius**2) * math.pi

    def calculate_perimeter(self):
        return self._radius * 2 * math.pi

    def __str__(self):
        return f"I'm a circle and my area is {self.calculate_area()}"

    def __lt__(self, other):
        return self.less_than(other)

    def less_than(self, other): pass

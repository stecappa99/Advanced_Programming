from shapes.ShapeIterator import ShapeIterator
from shapes.triangle import triangle
from shapes.square import square
from shapes.rectangle import rectangle
from shapes.pentagon import pentagon
from shapes.hectagon import hectagon
from shapes.circle import Circle as circle


if __name__ == "__main__":
    ls = [shape(7) for shape in [triangle, square, rectangle, circle, pentagon, hectagon]]
    s_i = ShapeIterator(ls, lambda a, b: a.calculate_area() > b.calculate_area())

    for shape in s_i:
        print(shape)

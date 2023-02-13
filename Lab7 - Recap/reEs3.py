
class Matrix:

    def __init__(self, list_of_list):
        self._list_of_list = list_of_list

    def get_row_num(self):
        return len(self._list_of_list)

    def get_col_num(self):
        assert all([len(x) == len(self._list_of_list[0]) for x in self._list_of_list]), "Lunghezze delle colonne non valide"
        return len(self._list_of_list[0])

    def is_compatible(self, other):
        assert isinstance(other, Matrix), "Type not valid"
        return other.get_row_num() == self.get_row_num() and other.get_col_num() == self.get_col_num()

    def __eq__(self, other):
        return False if not self.is_compatible(other) or not all(map(lambda x, y: x == y, self._list_of_list, other._list_of_list)) else True

    def __add__(self, other):
        assert self.is_compatible(other), "Matrici non compatibili"
        return Matrix(list(map(lambda x, y: list(map(lambda z, w: z + w, x, y)), self._list_of_list, other._list_of_list)))

    def __copy__(self):
        return Matrix(self._list_of_list)

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix([[i * other for i in j] for j in self._list_of_list])
        elif isinstance(other, Matrix):
            return Matrix([[i * other for i in j] for j in self._list_of_list])

    def transposition(self):
        return Matrix([[self._list_of_list[i][j] for i in range(self.get_row_num())] for j in range(self.get_col_num())])

    def __str__(self):
        s = ""
        for i in self._list_of_list:
            for j in i:
                s += f"{j}\t"
            s += "\n"
        return s


if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = m1.__copy__()
    print(m1 == m2)
    print(m1 + m2)
    print(m1 * 3)
    print(m1.transposition())

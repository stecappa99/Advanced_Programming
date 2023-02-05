class Associativity:
    def __set__(self, instance, value):
        assert all([value(value(a, b), c) == value(a, value(b, c)) for a in instance._set for b in instance._set for c in instance._set]), "Associativity not respected"
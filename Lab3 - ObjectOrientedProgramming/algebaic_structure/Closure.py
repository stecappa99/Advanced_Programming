class Closure:
    def __set__(self, instance, value):
        assert all([value(e1, e2) in instance._set for e1 in instance._set for e2 in instance._set]), \
            "Closure not respected"
        instance._op = value

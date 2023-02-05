class Invertibility:
    def __set__(self, instance, value):
        assert any([value(inv, x) == instance._i])
class Identity:
    def __set__(self, instance, value):
        assert all([instance._op(elem, value) == elem and instance._op(value, elem) == elem for elem in instance._set]), "Identity value not valid as Identity"
        instance._i = value
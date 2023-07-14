import types

from EmptyStack import EmptyStack
from FullStack import FullStack
from Stack import Stack


def chageStack(st):
    if st.__top__ == 0:
        st.__class__ = EmptyStack
    elif st.__top__ == st.__size__:
        st.__class__ = FullStack
    else:
        st.__class__ = Stack


changeClassFunctions = {
    "Stack": chageStack,
    "FullStack": chageStack,
    "EmptyStack": chageStack
}


class ApplySpell(type):
    def __new__(cls, classname, supers, classdict):

        new_dict = {}
        for k, v in classdict.items():
            #print(k, type(v), callable(v))
            new_dict[k] = change_class(classname, v) if callable(v) else v


        #new_dict = {k: v if callable(v) else change_class(classname, v) for k, v in classdict.items()}

        return type.__new__(cls, classname, supers, new_dict)


def change_class(cls, f):
    def wrapper(self, *args, **kargs):
        res = f(self, *args, **kargs)
        changeClassFunctions[cls](self)
        return res

    return wrapper


EmptyStack = ApplySpell(EmptyStack.__name__, EmptyStack.__bases__, EmptyStack.__dict__)
FullStack = ApplySpell(FullStack.__name__, FullStack.__bases__, FullStack.__dict__)
Stack = ApplySpell(Stack.__name__, Stack.__bases__, Stack.__dict__)


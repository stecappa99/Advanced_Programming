get_last = lambda x: x[len(x) - 1]


def build_animals():
    with open("animals.txt") as f:
        lines = f.readlines()
    support = {a.strip(): [an.strip() for an in lines if get_last(a.strip()) == an[0]] for a in lines}
    ams = {}
    for k, v in support.items():
        ams[k] = wrapper([k], support)
    return ams


def wrapper(animal, d):
    res = []

    def build_list(a):
        c = get_last(a)
        dl = [x for x in d[c] if x not in a]
        if len(dl) == 0:
            res.append(a)
        else:
            sl = [a.copy() for _ in range(len(dl))] if len(dl) > 1 else [a]
            for i in range(len(dl)):
                sl[i].append(dl[i])
                build_list(sl[i])

    build_list(animal)
    return res


animals = build_animals()


def genchain(animal, fx=max):
    return fx(animals[animal], key=lambda x: len(x))

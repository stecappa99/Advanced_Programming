get_last = lambda x: x[len(x) - 1]


def build_animals():
    with open("animals.txt") as f:
        lines = f.readlines()
    support = {a.strip(): [an.strip() for an in lines if get_last(a.strip()) == an[0]] for a in lines}
    ams = {}
    for k, v in support.items():
        ams[k] = build_list([k], support)
    return ams

def wrapper(animal, d):
    res = []
    def build_list(animal, d):
        c = get_last(animal)
        dl = [x for x in d[c] if x not in animal]
        if len(dl) == 0:
            res.append(animal)
        else:
            sl = [animal.copy() for _ in range(len(dl))] if len(dl) > 1 else [animal]
            res = []
            for i in range(len(dl)):
                sl[i].append(dl[i])
                x = build_list(sl[i], d)
    buil_list(animal, d)
    return res


animals = build_animals()


def genchain(animal, fx=max):
    return fx(animals[animal], key=lambda x: len(x)) if len(animals[animal]) > 0 else []

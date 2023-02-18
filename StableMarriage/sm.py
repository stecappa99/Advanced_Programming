

def sm(guy_pref: dict, gal_pref: dict):
    couples = {}

    def find_couples(gs):
        if not len(gs):
            return couples
        else:
            g = gs.pop(0)
            gal = guy_pref[g].pop(0)
            gal, i = gal, gal_pref[gal].index(g)
            if gal not in couples:
                print("Couple")
                couples[gal] = (i, g)
            elif couples[gal][0] > i:
                gs.append(couples[gal][1])
                couples[gal] = (i, g)
            else:
                gs.append(g)
            return find_couples(gs)

    return [(k, v[1]) for k, v in find_couples([k for k in guy_pref.keys()]).items()]

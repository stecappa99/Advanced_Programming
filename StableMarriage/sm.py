

def sm(guy_pref, gal_pref):
    couples = {}
    sup = {k: {v[i]: i for i in range(len(v))} for k, v in gal_pref.items()}

    def find_couples(gs):
        if not len(gs):
            return couples
        else:
            g = gs.pop()
            gal = guy_pref[g].pop(0)
            if gal not in couples:
                print(f"Couple created {gal} & {g}")
                couples[gal] = g
            elif sup[gal][g] < sup[gal][couples[gal]]:
                print(f"Couple broke {gal} & {couples[gal]}")
                gs.insert(0, couples[gal])
                print(f"Couple created {gal} & {g}")
                couples[gal] = g
            else:
                gs.insert(0, g)
            return find_couples(gs)
        
    return [(k, v) for k, v in find_couples([k for k in guy_pref.keys()]).items()]



def sm(guy_pref, gal_pref):
    couples = {}

    def find_couples(gs):
        if not len(gs):
            return couples
        else:
            g = gs.pop(0)
            gal = guy_pref[g].pop(0)
            if gal not in couples:
                print(f"Couple created {gal} & {g}")
                couples[gal] = g
            elif check_couple(gal_pref[gal], couples[gal], g):
                print(f"Couple broke {gal} & {couples[gal]}")
                gs.append(couples[gal])
                print(f"Couple created {gal} & {g}")
                couples[gal] = g
            else:
                gs.append(g)
            return find_couples(gs)
        
    def check_couple(gal_ls, prec, current):
        if gal_ls[0] == current:
            return True
        elif gal_ls[0] == prec:
            return False
        else:
            return check_couple(gal_ls[1:], prec, current)

    return [(k, v[1]) for k, v in find_couples([k for k in guy_pref.keys()]).items()]

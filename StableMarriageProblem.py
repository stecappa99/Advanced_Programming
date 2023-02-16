
guy_pref = {
    "A" : ["E", "F", "G"],
    "B" : ["G", "E", "F"],
    "C" : ["F", "G", "E"]
}

gal_pref = {
    "E" : ["A", "C", "B"],
    "F" : ["B", "C", "A"],
    "G" : ["C", "A", "B"]
}



def sm(guys, gals):
    return [(k, v) for k, v in _ricur(guys.keys(), {}, 0)]
    
    
def _ricur(guys, couples, i):
    if not len(guys):
        return couples
    else:
        return _ricur(guys[1:], {g, i for g in guys if g}, (i + 1) % len(gal_pref))
        
        
            
from sm import sm

guy_pref = {
    "1": ["2", "1", "3", "4"],
    "2": ["4", "1", "2", "3"],
    "3": ["1", "3", "2", "4"],
    "4": ["2", "3", "1", "4"]
}

gal_pref = {
    "1": ["1", "3", "2", "4"],
    "2": ["3", "4", "1", "2"],
    "3": ["4", "2", "3", "1"],
    "4": ["3", "2", "1", "4"]
}

men = {
    '1': ['C', 'B', 'E', 'A', 'D'],
    '2': ['A', 'B', 'E', 'C', 'D'],
    '3': ['D', 'C', 'B', 'A', 'E'],
    '4': ['A', 'C', 'D', 'B', 'E'],
    '5': ['A', 'B', 'D', 'E', 'C']
}

women = {
    'A': ['3', '5', '2', '1', '4'],
    'B': ['5', '2', '1', '4', '3'],
    'C': ['4', '3', '5', '1', '2'],
    'D': ['1', '2', '3', '4', '5'],
    'E': ['2', '3', '4', '1', '5']
}

men2 = {
    'A': ['Y', 'X', 'Z'],
    'B': ['Z', 'Y', 'X'],
    'C': ['X', 'Z', 'Y']
}

women2 = {
    'X': ['B', 'A', 'C'],
    'Y': ['C', 'B', 'A'],
    'Z': ['A', 'C', 'B']
}

men3 = {
    '0': ['7', '5', '6', '4'],
    '1': ['5', '4', '6', '7'],
    '2': ['4', '5', '6', '7'],
    '3': ['4', '5', '6', '7']
}

women3 = {
    '4': ['0', '1', '2', '3'],
    '5': ['0', '1', '2', '3'],
    '6': ['0', '1', '2', '3'],
    '7': ['0', '1', '2', '3']
}

men4 = {
    "Adam": ["Beth", "Amy", "Diane", "Ellen", "Cara"],
    "Bill": ["Diane", "Beth", "Amy", "Cara", "Ellen"],
    "Carl": ["Beth", "Ellen", "Cara", "Diane", "Amy"],
    "Dani": ["Amy", "Diane", "Cara", "Beth", "Ellen"],
    "Eric": ["Beth", "Diane", "Amy", "Ellen", "Cara"]
}

women4 = {
    "Amy": ["Eric", "Adam", "Bill", "Dani", "Carl"],
    "Beth": ["Carl", "Bill", "Dani", "Adam", "Eric"],
    "Cara": ["Bill", "Carl", "Dani", "Eric", "Adam"],
    "Diane": ["Adam", "Eric", "Dani", "Carl", "Bill"],
    "Ellen": ["Dani", "Bill", "Eric", "Carl", "Adam"]
}

if __name__ == "__main__":
    print(sm(guy_pref, gal_pref))
    print()
    print(sm(men, women))
    print()
    print(sm(men2, women2))
    print()
    print(sm(men3, women3))
    print()
    print(sm(men4, women4))

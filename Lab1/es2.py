def get_highest_atomic_number(metals):
    return sorted(metals, key=lambda x: x[0], reverse=True)[0][0]


if __name__ == "__main__":
    alkaline_earth_metals = \
        [
            (56, "barium"),
            (4, "beryllium"),
            (20, "calcium"),
            (12, "magnesium"),
            (88, "radium"),
            (38, "strontium")
        ]
    print(get_highest_atomic_number(alkaline_earth_metals))
    print(sorted(alkaline_earth_metals, key=lambda x: x[0]))
    alkaline_dict = {key: value for value, key in alkaline_earth_metals}
    print(alkaline_dict)
    noble_gases = {"helium": 2, "neon": 10, "argon": 18, "krypton": 36, "xenon": 54, "radon": 86}
    merged = dict()
    merged.update(alkaline_dict)
    merged.update(noble_gases)
    print([(a, b) for a, b in sorted(merged.items(), key=lambda x: x[0])])
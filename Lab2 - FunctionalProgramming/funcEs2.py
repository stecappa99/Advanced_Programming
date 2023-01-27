import re


def freqs(filename, n):
    with open(filename, "rt") as f:
        testo = f.read().lower()
    return sorted([a for a in count_freq(re.findall("\\w+", testo)) if a[1] > n], key=lambda x: x[1])


def count_freq(ls):
    return {(a, ls.count(a)) for a in ls}


if __name__ == "__main__":
    print(freqs("../testo.txt", 20))

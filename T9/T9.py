import re
import functools

t9_dict = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


concat = lambda x, ls, sep: {x + sep + z for y in ls for z in y}


def import_dictionary(filename):
    with open(filename) as fn:
        lines = sorted(fn.readlines(), key=lambda x: len(x), reverse=True)
    return {k: [v.strip() for v in lines if len(v.strip()) == k] for k in range(1, len(lines[0]))}


def translate(line, dict):
    words = re.findall("\\d+", line)
    new = list(map(lambda x: [t_i for t in get_translations(get_letters(x), "") for t_i in t if t_i in dict[len(x)]], words))
    print(*new, sep="\n")
    translated = get_translations(new, " ")
    print(*translated, sep="\n")


def get_letters(w):
    ls = [[x for x in t9_dict[c]] for c in w]
    return ls


def get_translations(ls, sep):
    if len(ls) == 1:
        return ls
    else:
        return [concat(x, get_translations(ls[1:], sep), sep) for x in ls[0]]


if __name__ == "__main__":
    d = import_dictionary("dictionary.txt")
    with open("t9_texts.txt") as f:
         ls = f.readlines()

    for i in ls:
        translate(i, d)

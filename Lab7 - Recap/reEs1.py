import re


def trim(s):
    assert isinstance(s, str), "Incorrect format"
    return re.sub(r"\s+", " ", s.strip())


def get_5_char(n):
    n = str(123)
    return " " * (5 - len(n)) + n + " "

def get_lines(line):
    sup = re.fullmatch(r"\w{2,}", line)
    res = ""
    while sup is not None:
        if sup.start() > 33:
            res = line[(sup.start() - 33):sup.end()]
        sup = re.match(r"\w{2,}", line)
    return res

if __name__ == "__main__":
    with open("testo.txt", "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        result = get_5_char(i+1)
        get_lines(lines[i])

from itertools import groupby
from functools import reduce

_words = open("words.txt", "r").readlines()
gen_key = lambda x: reduce(lambda z, y: z + y, list(sorted(x.strip())))


def _build_words_dictionary():
    return {k: list(v) for k, v in groupby(_words, key=gen_key)}


_words_dict = _build_words_dictionary()


def anagram(word):
    return reduce(lambda x, y: x.strip() + ", " + y.strip(), filter(lambda x: x != word, _words_dict[gen_key(word)]))


def anagrams():
    print(_words_dict)
    return reduce(lambda x, y: x + "\n" + y, [val[0] + ":-" + anagram(val[0]) for _, val in _words_dict])


import itertools
import re


class extendedString(str):

    def __init__(self, initial):
        self = initial

    def is_palindrome(self):
        support = re.findall("\\w", self.upper())
        s = support[-(len(support) // 2):]
        s.reverse()
        return support[:len(support) // 2] == s

    def __sub__(self, other):
        assert isinstance(other, extendedString), "Type not match"
        return str.join("", [c for c in self if c not in other])

    def is_anagram(self, d):
        assert isinstance(d, dict), "Type not match"
        support = re.findall("\\w", self.upper())
        anagrams = itertools.permutations(support)
        for i in anagrams:
            if i in d.values():
                return True
        return False


if __name__ == "__main__":
    s = extendedString("Rise to vote, sir.")
    print(s.is_palindrome())
    print(s - extendedString("s"))
    s1 = extendedString("abc")
    s.is_anagram({1: "abc"})

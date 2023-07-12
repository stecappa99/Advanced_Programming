from wordle import read_words, wordle


def print_wordlet(wordlet):
    for w in wordlet:
        print(w)
    print('\n')


if __name__ == "__main__":
    wi = read_words('wordlist-wordle.txt')
    print_wordlet(wordle('model', 'melon', wi))
    print_wordlet(wordle('slice', 'mount', wi))
    print_wordlet(wordle('crane', 'vowel', wi))
    print_wordlet(wordle('drive', 'sooty', wi))
    print_wordlet(wordle('yacht', 'sassy', wi))
    print_wordlet(wordle('happy', 'roots', wi))
    print_wordlet(wordle('lines', 'hatch', wi))

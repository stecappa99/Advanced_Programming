colors = {
    "Green": "\u001b[32;1m",
    "Yellow": "\u001b[33;1m",
    "White": "\u001b[37;1m"
}


def read_words(fn):
    with open(fn, "r") as f:
        return [word.strip() for word in f.readlines() if len(word.strip()) == 5 and str.isalpha(word.strip())]
        # words = {}
        # for w in [word.strip() for word in f.readlines() if len(word.strip()) == 5 and str.isalpha(word.strip())]:
        #     for i in range(len(w)):
        #         if (i, w[i]) in words:
        #             words[(i, w[i])].add(w)
        #         else:
        #             words[(i, w[i])] = {w}
        # print(words)
        # return words


def wordle(guess, wordle, dictionary):
    possibly_in = [{chr(x) for x in range(ord('a'), ord('z'))}] * 5
    guesses = []

    def play(g, p_i, d):
        if g == wordle:
            guesses.append(''.join([colors["Green"] + c for c in g]))
            return guesses
        else:
            colored = [''] * 5
            yellow_chars = set()
            for i in range(len(wordle)):
                if wordle[i] == g[i]:
                    p_i[i] = {g[i]}
                    color = "Green"
                else:
                    if g[i] not in wordle:
                        p_i = [p_i[j].difference({g[i]}) if len(p_i[j]) > 1 else p_i[j] for j in range(len(p_i))]
                        color = "White"
                    else:
                        p_i[i] = p_i[i].difference({g[i]})
                        yellow_chars.add(g[i])
                        color = "Yellow"

                colored[i] = colors[color] + g[i]

            guesses.append(''.join(colored))
            next_words = [d_i for d_i in d
                          if all([d_i[k] in p_i[k] for k in range(len(d_i))])
                          and
                          len({d_i[k] for k in range(len(d_i))}.intersection(yellow_chars)) >= len(yellow_chars)]
            #print(next_words)
            return play(next_words[0], p_i, next_words)

    return play(guess, possibly_in, dictionary)

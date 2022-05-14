def gen_repeat_pattern_words(alphabet, index, nb, w):
    len_nb = sum(nb)
    if len_nb == len(w):
        yield w
    else:
        for l in alphabet:
            if l not in w:
                w+= nb[index]*l
                index+=1
                yield from gen_repeat_pattern_words(alphabet, index, nb, w)
                w     = w[:len(w) - nb[index-1]]
                index = index - 1

def gen_pattern_words(alphabet, pattern, w):
    """ * : any letter but once """
    if len(w) == len(pattern):
        yield w
    else:
        index = len(w)
        if(pattern[index] == "*"):
            for l in alphabet:
                w+=l
                yield from gen_pattern_words(alphabet, pattern, w)
                w = w[:len(w) - 1]
        elif pattern[index] in alphabet:
            w+=pattern[index]
            yield from gen_pattern_words(alphabet, pattern, w)
            w = w[:len(w) - 1]


def gen_words(alphabet, k, w):
    if len(w) == k:
        yield w
    else:
        for l in alphabet:
            w+=l
            yield from gen_words(alphabet, k, w)
            w = w[:len(w) - 1]

w = gen_words(["a", "b", "c"], 3, "")
pattern = ['*', 'a', 'a', '*']
p = gen_pattern_words(["a", "b", "c"], pattern, "")

nb = [2, 4, 3]
n = gen_repeat_pattern_words(["a", "b", "d", "e", "f"], 0, nb, "")
for x in n:
    print(x)
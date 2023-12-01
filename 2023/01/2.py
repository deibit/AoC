words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def detect(w):
    if w[0].isdigit():
        return (w[0], w[1:])
    for k in words.keys():
        if w.startswith(k):
            return (words[k], w[1:])
    return (None, w[1:])


def accum(w):
    n = []
    while w:
        num, rest = detect(w)
        w = rest
        if num:
            n.append(num)
    return int("".join([n[0], n[-1]]))


with open("input.txt") as f:
    s = 0
    for line in f.readlines():
        p = accum(line)
        s += p
    print(s)


"""
I'm not happy with this solution. 

Another strategy would be to search the second number backwards when we found the first one.

With this algo the search is exaustive.
"""

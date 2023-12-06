import math


def linear(filename):
    vector = []
    with open(filename) as f:
        for line in f:
            vector.extend([c for c in line.strip()])
    return vector


def get_dim(v):
    return round(math.sqrt(len(v)))


def extract_number(v, pos):
    r = []

    while pos >= 0 and v[pos].isdigit():
        pos -= 1

    pos += 1

    while pos < len(v) and v[pos].isdigit():
        r.append(v[pos])
        pos += 1

    return r


def positions(x, wide):
    return [
        pos
        for pos in [
            x - 1,
            x + 1,
            x - wide,
            x - wide + 1,
            x - wide - 1,
            x + wide,
            x + wide + 1,
            x + wide - 1,
        ]
        if pos >= 0 and pos < (wide * wide)
    ]


def print_grid(g):
    d = get_dim(g)
    for x in range(0, len(g), d):
        print("".join(g[x : x + d]))


def two2one(d, x, y):
    return x + (y * d)


def one2two(d, x):
    return (x % d, x // d)


l = linear("input.txt")
# print_grid(l)
d = get_dim(l)

# DEBUG
# for pos in positions(two2one(d, 5, 5), d):
#     print(f"{pos} -> {one2two(d, pos)} = {l[pos]}")
#
#     if l[pos].isdigit():
#         extract_number(l, pos)


r = []
for pos in range(0, len(l)):
    if not l[pos].isdigit() and not l[pos] == ".":
        box = positions(pos, d)
        subr = []
        for other in box:
            if l[other].isdigit():
                n = extract_number(l, other)
                if n:
                    subr.append(int("".join(n)))
        r.extend(list(set(subr)))

print(sum(r))

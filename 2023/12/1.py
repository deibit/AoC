from itertools import combinations

lines = open("input.txt").readlines()

rows = []
for line in lines:
    springs, records = line.split()
    records = [int(n) for n in records.split(",")]
    rows.append(
        (
            springs,  #   ??..##
            records,  #   [1,2,3]
            sum(records),  #   sum([1,2,3])
            sum([1 for c in springs if c == "#"]),  #   number of #
            sum([1 for c in springs if c == "?"]),  #   number of ?
        )
    )


def split(springs):
    return [i for i in springs.split(".") if i]


def check(springs, records):
    s = [len(i) for i in split(springs.replace("?", "."))]
    return s == records


def replace(springs: str) -> list[int]:
    pos = []
    for i in range(len(springs)):
        if springs[i] == "?":
            pos.append(i)
    return pos


def hashit(springs: str, pos: list) -> str:
    l = list(springs)
    for p in pos:
        l[p] = "#"
    return "".join(l)


good_ones = 0
for row in rows:
    c = combinations(replace(row[0]), abs(row[2] - row[3]))
    for comb in c:
        r = hashit(row[0], list(comb))
        if check(r, row[1]):
            good_ones += 1

print(good_ones)

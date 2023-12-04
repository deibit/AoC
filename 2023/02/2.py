from functools import reduce


def parse(line):
    g, c = line.split(":")
    g = int(g.replace("Game ", ""))
    c = [e.strip() for e in c.split(";")]
    r = []

    for cc in c:
        d = {}
        for ccc in cc.split(","):
            ccc = ccc.strip()
            v, c = ccc.split(" ")
            d[c] = int(v)
            r.append(d)

    return (g, r)


def mvg(e: list[dict]):
    d = {"red": 0, "green": 0, "blue": 0}
    for dd in e:
        for k in dd.keys():
            if d[k] == 0:
                d[k] = dd[k]
                continue
            if d[k] < dd[k]:
                d[k] = dd[k]
    return d


results = []
with open("input.txt") as f:
    s = 0
    for line in f:
        g, d = parse(line)
        d = mvg(d)
        r = reduce(lambda x, y: x * y, [x for x in d.values() if x])
        results.append(r)
print(sum(results))

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


def check(e: list[dict]):
    d = {"red": 12, "green": 13, "blue": 14}
    for dd in e:
        for k in dd.keys():
            if d[k] < dd[k]:
                return False
    return True


with open("input.txt") as f:
    s = 0
    for line in f:
        g, d = parse(line)
        if check(d):
            s += g
print(s)

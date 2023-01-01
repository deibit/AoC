def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


parse = lambda x: int(x.split("=")[1].replace(",", "").replace(":", ""))


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def expand(m, q):
    x = m[0][0]
    y = m[0][1]
    f = m[1]
    r = []

    if (y - f) > q > (y + f):
        return False

    for xx, yy in zip(range(1, f + 2), range(y - f, y + 1)):
        if yy == q:
            for xxx in range(x - xx + 1, x + xx):
                r.append((xxx, yy))

    for xx, yy in zip(range(f, -1, -1), range(y + 1, y + f + 1)):
        if yy == q:
            for xxx in range(x + xx - 1, x - xx, -1):
                r.append((xxx, yy))
    return r


M = []
# Q = 10
Q = 2000000
FILE = "input"
S = []
B = []

data = get_data(FILE)
for d in data:
    s = d.split()
    S.append((parse(s[2]), parse(s[3])))
    B.append((parse(s[8]), parse(s[9])))
    M.append((S[-1], manhattan(S[-1], B[-1])))

N = []
for s in M:
    if r := expand(s, Q):
        if len(r) > 0:
            N.extend(r)
signal = set()
for n in N:
    if n[1] == Q:
        signal.add(n)

beacons = set()
for b in B:
    if b[1] == Q:
        beacons.add(b)

sensors = set()
for s in S:
    if s[1] == Q:
        sensors.add(s)

print(len(signal.difference(beacons).difference(sensors)))

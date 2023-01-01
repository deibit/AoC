def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


parse = lambda x: int(x.split("=")[1].replace(",", "").replace(":", ""))


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def expand(m, p=False):
    x = m[0][0]
    y = m[0][1]
    f = m[1]
    r = []

    for xx, yy in zip(range(1, f + 2), range(y - f, y + 1)):
        if p:
            print(f"---- {yy} -----")
        for xxx in range(x - xx + 1, x + xx):
            r.append((xxx, yy))
            if p:
                print(xxx)

    if p:
        print("--- PARTE 2 ---")

    for xx, yy in zip(range(f, -1, -1), range(y + 1, y + f + 1)):
        if p:
            print(f"---- {yy} -----")
        for xxx in range(x + xx - 1, x - xx, -1):
            r.append((xxx, yy))
            if p:
                print(xxx)

    return r


M = []
FILE = "test"
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
    if r := expand(s):
        if len(r) > 0:
            N.extend(r)

grid = [["." for _ in range(28 + 1)] for _ in range(22 + 1)]

ibeacon = (2, 10)
isensor = (8, 7)
iman = manhattan(isensor, ibeacon)
icover = (isensor, iman)
result = expand(icover, True)
print(f"sensor: {isensor} beacon: {ibeacon} manhattan: {iman}")

for point in N:
    if point[1] < 0 or point[1] > 22 or point[0] < -2 or point[0] > 25:
        continue
    grid[point[1]][point[0] + 2] = "\u001b[38;5;8m#\u001b[0m"

for point in S:
    grid[point[1]][point[0] + 2] = "\u001b[32mS\u001b[0m"

for point in B:
    grid[point[1]][point[0] + 2] = "\u001b[31mB\u001b[0m"


print("               1    1    2    2")
print("     0    5    0    5    0    5")
for y, r in enumerate(grid, start=0):
    print(f"{y:<3}{''.join(r)}")

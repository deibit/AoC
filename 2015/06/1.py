from utils.f import readinput, readtest

entries = readinput(__file__).split("\n")
# entries = readtest(__file__).split("\n")

entries = [n.strip() for n in entries if n]


def getpoints(entry):
    t = entry[0].split(",")
    x1, y1 = int(t[0]), int(t[1])
    t = entry[2].split(",")
    x2, y2 = int(t[0]), int(t[1])

    points = []

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            points.append((x, y))

    return points


ROW = 1000
lights = [False for _ in range(ROW * ROW)]

for entry in entries:
    entry = entry.split(" ")
    orders = entry[:2]
    points = getpoints(entry[-3:])

    for point in points:
        pos = ROW * point[1] + point[0]
        if orders[0] == "toggle":
            lights[pos] = not lights[pos]
        elif orders[1] == "on":
            lights[pos] = True
        elif orders[1] == "off":
            lights[pos] = False

print(sum([1 for i in lights if i]))


# for pos, c in enumerate(lights):
#     if c:
#         print("*", end="")
#     else:
#         print(".", end="")
#     if pos + 1 % ROW == 0:
#         print("\n")

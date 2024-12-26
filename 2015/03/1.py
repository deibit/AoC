from utils.f import readinput

entries = readinput(__file__)

visits = []
x, y = 0, 0
for entry in entries:
    if entry == "^":
        y += 1
    elif entry == "v":
        y -= 1
    elif entry == "<":
        x -= 1
    elif entry == ">":
        x += 1
    visits.append((x, y))

print(len(set(visits)))

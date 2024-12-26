from utils.f import readinput

entries = readinput(__file__)

santa = [(0, 0)]
robot = [(0, 0)]

for pos, entry in enumerate(entries):
    x, y = 0, 0
    if entry == "^":
        y += 1
    elif entry == "v":
        y -= 1
    elif entry == "<":
        x -= 1
    elif entry == ">":
        x += 1

    if pos % 2 == 0:
        santa.append((x + santa[-1][0], y + santa[-1][1]))
    else:
        robot.append((x + robot[-1][0], y + robot[-1][1]))

santa.extend(robot)
print(len(set(santa)))

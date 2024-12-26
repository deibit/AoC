from utils.f import readinput

entries = readinput(__file__)

floor = 0
for pos, e in enumerate(entries):
    floor += 1 if e == "(" else -1
    if floor == -1:
        print(pos + 1)
        break

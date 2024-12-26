from utils.f import readinput

entries = readinput(__file__).split("\n")


entries = [
    sorted((int(l), int(w), int(h))) for l, w, h in [t.split("x") for t in entries]
]

entries = [(x + x + y + y) + (x * y * z) for x, y, z in entries]

print(sum(entries))

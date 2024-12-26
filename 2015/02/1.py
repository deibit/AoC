from utils.f import readinput

entries = readinput(__file__).split("\n")


entries = [
    (int(l) * int(w), int(w) * int(h), int(h) * int(l))
    for l, w, h in [t.split("x") for t in entries]
]

entries = [2 * sum(entry) + min(entry) for entry in entries]

print(sum(entries))

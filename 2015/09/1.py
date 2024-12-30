import pprint
from itertools import permutations

from utils.f import readinput, readtest

entries = readinput(__file__).split("\n")
# entries = readtest(__file__).split("\n")
# entries: list[str] = [e for e in entries if e]

cities = {}

for e in entries:
    org, _, dst, _, distance = map(str.strip, e.split(" "))
    distance = int(distance)
    if org not in cities:
        cities[org] = {}
    if dst not in cities:
        cities[dst] = {}
    # Yes, this is suboptimal as distances are recorded more than necessary
    cities[org][dst] = distance
    cities[dst][org] = distance

k = cities.keys()
paths = []

for perm in permutations(k):
    s = 0
    for i in range(0, len(perm) - 1):
        s += cities[perm[i]][perm[i + 1]]
    paths.append(s)

print(f"Part 1: {sorted(paths)[0]}")
print(f"Part 2: {sorted(paths)[-1]}")

"""

My solution involve some brute force which I assume is not the optimal way to go.

Currently it is just a reverse mapping. BT from the lowest location (or 0) up until a valid seed is found.

Some strategies could be to merge overlapping seed ranges. But I'm too lazy today to do it and test it.

"""


import re


def get_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines() if not line == "\n"]


class Map:
    def __init__(self, name, maps=[]):
        self.name = name
        self.maps = maps

    def __str__(self):
        return f"{self.name}: {self.maps}"

    def map(self, value):
        for m in self.maps:
            source, dest, delta = m  # change dest <-> source for part 2
            if source <= value <= source + delta:
                result = dest + abs(source - value)
                return result
        return value


lines = get_lines("input.txt")
seeds = [int(n) for n in re.findall(r"\d+", lines[0].split(":")[1])]


lines = lines[1:]
maps = []

current_map = None
for line in lines:
    if "map" in line:
        if current_map:
            maps.append(current_map)
        current_map = Map(name=line.split(":")[0], maps=[])
    else:
        if current_map:
            current_map.maps.append([int(n) for n in re.findall(r"\d+", line)])
maps.append(current_map)
maps.reverse()


def check_seed(value):
    for r in range(0, len(seeds), 2):
        if seeds[r] <= value <= seeds[r] + seeds[r + 1]:
            return True
    return False


location = 0
while True:
    seed = location
    for m in maps:
        seed = m.map(seed)
    if check_seed(seed):
        print(f"found seed {seed} which gives location {location}")
        exit()
    location += 1

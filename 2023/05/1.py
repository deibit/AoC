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
            dest, source, delta = m
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


locations = []
for seed in seeds:
    for m in maps:
        seed = m.map(seed)
    locations.append(seed)

print(min(locations))

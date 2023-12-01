from typing import List


def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


class Valve:
    def __init__(self, name, rate, valves):
        self.name: str = name
        self.rate: int = rate
        self.open: bool = False
        self.valves: List[str] = valves

    def __str__(self):
        return f"{self.name} {self.rate} {self.valves} {self.open}"


def parse(line) -> Valve:
    line = line.split()
    name = line[1]
    rate = int(line[4].split("=")[1].split(";")[0])
    valves = [v.replace(",", "") for v in line[9:] if v]
    return Valve(name=name, rate=rate, valves=valves)


FILE = "test"

minutes = 30
pressure = 0
valves = []
data = get_data(FILE)
for line in data:
    valves.append(parse(line))

for v in valves:
    print(v)

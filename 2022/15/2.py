from dataclasses import dataclass


def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


parse = lambda x: int(x.split("=")[1].replace(",", "").replace(":", ""))


def manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


@dataclass
class Sensor:
    x: int
    y: int
    m: int

    def __init__(self, x, y, m=-1):
        self.x = x
        self.y = y
        self.m = m


@dataclass
class Point:
    x: int
    y: int


def contour(sensor: Sensor, limit_inf, limit_sup):
    x = sensor.x
    y = sensor.y
    f = sensor.m + 1
    candidates = []

    for xx, yy in zip(range(1, f + 2), range(y - f, y + 1)):
        X = x - xx + 1
        if (X >= limit_inf and yy >= limit_inf) and (
            X <= limit_sup and yy <= limit_sup
        ):
            candidates.append(Point(X, yy))

        X = x + xx - 1
        if (X >= limit_inf and yy >= limit_inf) and (
            X <= limit_sup and yy <= limit_sup
        ):
            candidates.append(Point(X, yy))

    for xx, yy in zip(range(f, -1, -1), range(y + 1, y + f + 1)):
        X = x - xx + 1
        if (X >= limit_inf and yy >= limit_inf) and (
            X <= limit_sup and yy <= limit_sup
        ):
            candidates.append(Point(X, yy))

        X = x + xx - 1
        if (X >= limit_inf and yy >= limit_inf) and (
            X <= limit_sup and yy <= limit_sup
        ):
            candidates.append(Point(X, yy))

    return candidates


FILE = "input"
S = []
B = []
Q1 = 0
# Q2 = 20
Q2 = 4_000_000

data = get_data(FILE)
for d in data:
    s = d.split()
    sensor = Sensor(x=parse(s[2]), y=parse(s[3]))
    b = Point(x=parse(s[8]), y=parse(s[9]))
    m = manhattan(sensor, b)
    sensor.m = m
    B.append(b)
    S.append(sensor)

for sensor in S:
    candidates = contour(sensor, Q1, Q2)
    for candidate in candidates:
        if all([manhattan(candidate, s) > s.m for s in S]):
            print(f"{candidate} found. Freq: {candidate.x*4000000+candidate.y}")
            exit()

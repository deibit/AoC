from dataclasses import dataclass


def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


FILE = "input"
data = get_data(FILE)


@dataclass
class Point:
    x: int
    y: int

    def __hash__(p):
        return p.x + p.y


# Process input to list of solids
lines = []
for d in data:
    lines.append(
        [
            Point(int(x), int(y))
            for x, y in [i.strip().split(",") for i in d.split("->")]
        ]
    )


def get_next(start: Point, end: Point):
    dst_x = abs(end.x - start.x)
    dst_y = abs(end.y - start.y)

    if dst_y == 0:
        return [Point(min(start.x, end.x) + x, start.y) for x in range(dst_x + 1)]

    if dst_x == 0:
        return [Point(start.x, min(start.y, end.y) + y) for y in range(dst_y + 1)]


grid = set()
for line in lines:
    start = line[0]
    for end in line[1:]:
        points = get_next(start, end)
        grid.update([point for point in points])
        start = end

FLOOR = max([p.y for p in grid]) + 2


def drop_salt():
    global grid
    p = Point(500, 0)
    while p.y < FLOOR - 1:
        if not Point(p.x, p.y + 1) in grid:
            p.y += 1
            continue
        else:
            if not Point(p.x - 1, p.y + 1) in grid:
                p.x -= 1
                p.y += 1
                continue
            elif not Point(p.x + 1, p.y + 1) in grid:
                p.x += 1
                p.y += 1
                continue
        return p
    return p


def view_grid():
    MAX_POINT = max([p.x for p in grid])
    MIN_POINT = min([p.x for p in grid])
    AIR = "."
    ROCK = "#"
    grid_view = [
        [AIR for _ in range(MAX_POINT - MIN_POINT + 1)] for _ in range(FLOOR + 1)
    ]
    for point in grid:
        grid_view[point.y][point.x - MIN_POINT] = ROCK

    for row in grid_view:
        print("".join(row))


c = 0
while True:
    if p := drop_salt():
        grid.add(p)
        c += 1
        if p == Point(500, 0):
            break
view_grid()
print(c)

from typing import List, Tuple

from colorama import Fore

FILE = "input.txt"

grid: List[List[str]] = [
    [col for col in row] for row in [row.strip() for row in open(FILE).readlines()]
]
rows = len(grid)
cols = len(grid[0])


class Point:
    def __init__(self, row, col, level=-1):
        self.row = row
        self.col = col
        self.level = level

    def __str__(self):
        return f"{self.row}:{self.col} lvl:{self.level} sym:{grid[self.row][self.col]}"


def grid_get_point(row, col):
    return grid[row][col]


# I'm too lazy to hardcode starting position
def start() -> Point:
    for row in range(0, rows):
        for col in range(0, cols):
            if grid_get_point(row, col) == "S":
                return Point(row, col, 0)
    quit("[start] Error getting starting position")


def check_limits(point: Tuple[int, int]):
    return 0 <= point[0] < rows and 0 <= point[1] < cols


def check_directions(dirs: List[str], point: Point):
    north, south, west, east = [
        (point.row - 1, point.col),
        (point.row + 1, point.col),
        (point.row, point.col - 1),
        (point.row, point.col + 1),
    ]

    feasibles = []

    for dir in dirs:
        match dir:
            case "north":
                if check_limits(north) and grid_get_point(*north) in ["|", "7", "F"]:
                    feasibles.append(Point(*north))
            case "south":
                if check_limits(south) and grid_get_point(*south) in ["|", "L", "J"]:
                    feasibles.append(Point(*south))
            case "west":
                if check_limits(west) and grid_get_point(*west) in ["-", "L", "F"]:
                    feasibles.append(Point(*west))
            case "east":
                if check_limits(east) and grid_get_point(*east) in ["-", "J", "7"]:
                    feasibles.append(Point(*east))
    return feasibles


def surround(point: Point) -> List[Point]:
    if not point:
        return []

    symbol = grid[point.row][point.col]
    feasibles = []

    match symbol:
        case ".":
            return feasibles
        case "|":
            feasibles.extend(check_directions(["north", "south"], point))
        case "-":
            feasibles.extend(check_directions(["west", "east"], point))
        case "L":
            feasibles.extend(check_directions(["north", "east"], point))
        case "J":
            feasibles.extend(check_directions(["north", "west"], point))
        case "7":
            feasibles.extend(check_directions(["south", "west"], point))
        case "F":
            feasibles.extend(check_directions(["south", "east"], point))
        case "S":
            feasibles.extend(
                check_directions(["north", "west", "south", "east"], point)
            )

    feasibles = [new for new in feasibles if not (new.row, new.col) in visited]
    for p in feasibles:
        p.level = point.level + 1
    return feasibles


visited = []
pending = [start()]


while pending:
    next = pending[0]
    pending = pending[1:]

    if (next.row, next.col) in visited:
        print(f"[FOUND END] {next}")
        break

    pending.extend(surround(next))
    visited.append((next.row, next.col))


def check_directions2(point):
    row = point[0]
    col = point[1]
    pointeables = [
        (row - 1, col),
        (row - 1, col - 1),
        (row - 1, col + 1),
        (row + 1, col),
        (row + 1, col - 1),
        (row + 1, col + 1),
        (row, col - 1),
        (row, col + 1),
    ]

    feasibles = []
    for pointeable in pointeables:
        if check_limits(pointeable):
            feasibles.append(pointeable)

    return feasibles


grid.append(["." for _ in range(0, len(grid[0]))])
grid.reverse()
grid.append(["." for _ in range(0, len(grid[0]))])
grid.reverse()
for row in grid:
    row.append(".")
    row.reverse()
    row.append(".")
    row.reverse()
rows = len(grid)
cols = len(grid[0])

print("Searching for free points")
pending = [(0, 0), (0, cols - 1), (rows - 1, cols - 1), (rows - 1, 0)]
frees = pending[:]
visited2 = []

while pending:
    next = pending[0]
    pending = pending[1:]
    new_ones = [
        point
        for point in check_directions2(next)
        if not point in visited and not point in pending and not point in visited2
    ]
    frees.extend(new_ones)
    pending.extend(new_ones)
    visited2.append(next)

print(
    f"Total: {rows} * {cols} = {rows*cols} The loop: {len(visited)} Free ones: {len(frees)} Inside loop: {(rows*cols)-(len(visited)+len(frees))}"
)
print(f"Linea: {len(grid[0])}")


c = 0


def visualization():
    global c
    for row in range(rows):
        s = ""
        for col in range(cols):
            if (row, col) in visited:
                s += Fore.RED + grid[row][col]
            elif (row, col) in frees:
                s += Fore.GREEN + grid[row][col]
            else:
                c += 1
                s += Fore.WHITE + grid[row][col]

        print(s)


visualization()
print(c)

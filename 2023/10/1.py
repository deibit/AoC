from typing import List, Tuple

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

    def symbol(self) -> str:
        return grid[self.row][self.col]

    def __str__(self):
        return f"{self.row}:{self.col} lvl:{self.level} sym:{self.symbol()}"


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

    symbol = point.symbol()
    feasibles = []

    match symbol:
        case ".":
            return feasibles
        case "|":
            return check_directions(["north", "south"], point)
        case "-":
            return check_directions(["west", "east"], point)
        case "L":
            return check_directions(["north", "east"], point)
        case "J":
            return check_directions(["north", "west"], point)
        case "7":
            return check_directions(["south", "west"], point)
        case "F":
            return check_directions(["south", "east"], point)
        case "S":
            return check_directions(["north", "west", "south", "east"], point)
    return feasibles


visited = []
pending: List[Point] = [start()]


def explore(point: Point):
    points = [new for new in surround(point) if not (new.row, new.col) in visited]
    for p in points:
        p.level = point.level + 1
    return points


while pending:
    next = pending[0]
    pending = pending[1:]

    if (next.row, next.col) in visited:
        print(f"[FOUND END] {next}")
        break

    pending.extend(explore(next))
    visited.append((next.row, next.col))

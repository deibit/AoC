def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


FILE = "input"
data = get_data(FILE)

AIR = "."
ROCK = "#"
SALT = "o"

# Process input to list of tuples
lines = []
for d in data:
    lines.append(
        [
            (int(col), int(row))
            for col, row in [i.strip().split(",") for i in d.split("->")]
        ]
    )

# Find max-x and max-y
max_col = max_row = 0
min_col = 500
min_row = 0
for line in lines:
    for t in line:
        if t[0] > max_col:
            max_col = t[0]
        if t[0] < min_col:
            min_col = t[0]
        if t[1] > max_row:
            max_row = t[1]

MAX_COL = max_col - min_col
MAX_ROW = max_row
grid = [[AIR for _ in range(MAX_COL + 1)] for _ in range(MAX_ROW + 1)]


def norm_col(col):
    return col - min_col


def draw_grid():
    global grid
    for i, row in enumerate(grid):
        print(i, "".join(row))


def get_next_points(start, end):
    col = end[0] - start[0]
    row = end[1] - start[1]

    if col < 0:
        return [(start[0] - c, start[1]) for c in range(abs(col) + 1)]
    elif col > 0:
        return [(start[0] + c, start[1]) for c in range(col + 1)]

    if row < 0:
        return [(start[0], start[1] - r) for r in range(abs(row) + 1)]
    elif row > 0:
        return [(start[0], start[1] + r) for r in range(row + 1)]


def draw_coors(line):
    global grid
    start = line[0]
    for end in line[1:]:
        for next_point in get_next_points(start, end):
            c, r = next_point
            grid[r][norm_col(c)] = ROCK
        start = end


def next_move(col, row):
    global grid

    # Watch if the salt is out
    if (row + 1 > MAX_ROW) or (col - 1 < 0) or (col >= MAX_COL):
        return False

    # Fall one step
    if grid[row + 1][col] not in [SALT, ROCK]:
        return (col, row + 1)

    # Cannot fall anymore, try down-left
    if grid[row + 1][col - 1] not in [SALT, ROCK]:
        return (col - 1, row + 1)

    # try down-right
    if grid[row + 1][col + 1] not in [SALT, ROCK]:
        return (col + 1, row + 1)

    return (col, row)


def count_salts():
    s = 0
    for row in grid:
        s += row.count(SALT)
    return s


for l in lines:
    draw_coors(l)

flag = True
while flag:
    salt = (norm_col(500), 0)
    for row in range(max_row + 1):
        grid[salt[1]][salt[0]] = SALT
        move = next_move(*salt)
        if not move:
            grid[salt[1]][salt[0]] = AIR
            flag = False
            break
        else:
            if move == salt:
                grid[salt[1]][salt[0]] = SALT
                salt = (norm_col(500), 0)
                break
            else:
                grid[salt[1]][salt[0]] = AIR
                salt = move
                grid[salt[1]][salt[0]] = SALT
draw_grid()
print(count_salts())

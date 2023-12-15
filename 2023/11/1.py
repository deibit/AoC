FILE = "input.txt"


def load(FILE):
    grid = [
        [col for col in row] for row in [row.strip() for row in open(FILE).readlines()]
    ]
    return (grid, len(grid), len(grid[0]))


grid, ROWS, COLS = load(FILE)

h_expanse = [number for number in range(ROWS) if not "#" in grid[number]]
v_expanse = []
for col in range(COLS):
    if not "#" in [grid[i][col] for i in range(ROWS)]:
        v_expanse.append(col)


galaxies = []
for y in range(ROWS):
    for x in range(COLS):
        if grid[y][x] == "#":
            galaxies.append((y, x))

distances = []


"""
Instead of expanding the grid, just calculate which expansion affects the distance.

Of course, Manhattan distance.

Every two points has its own "expansion_list" of rows/cols affected.

Taking min/max points we can split the list of non-affecting indexes and the rest of the 

indexes multiplies by a factor of one, therefore the len of the resulting list.

"""


def exsub(p, q, h=True):
    if h:
        exp = h_expanse
    else:
        exp = v_expanse

    minin = min(p, q)
    maxin = max(p, q)

    left = 0
    right = len(exp)
    for item in exp:
        if minin > item:
            left += 1
        if maxin < item:
            right -= 1
    return abs(minin - maxin) + len(exp[left:right])


while galaxies:
    galaxy = galaxies.pop()
    p1, p2 = galaxy
    for other_galaxy in galaxies:
        q1, q2 = other_galaxy
        distances.append(exsub(p1, q1) + exsub(p2, q2, h=False))


print(sum(distances))

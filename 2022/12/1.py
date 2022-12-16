def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


grid = [list(x) for x in [y for y in get_data("input")]]
rows = len(grid) - 1
cols = len(grid[0]) - 1


S = None
E = None
START = "S"
END = "E"
for row in range(rows + 1):
    for col in range(cols + 1):
        if grid[row][col] == START:
            S = ("a", row, col)
            grid[row][col] = ord("a") - 96
        elif grid[row][col] == END:
            E = ("{", row, col)
            grid[row][col] = ord("{") - 96
        else:
            grid[row][col] = ord(grid[row][col]) - 96


def is_reachable(a, b):
    global grid
    a = grid[a[0]][a[1]]
    b = grid[b[0]][b[1]]

    if b - a in [0, 1]:
        return True
    elif a - b >= 0:
        return True
    return False


def visitables(row, col):
    global grid
    c = []

    if row == 0:
        c.append(("v", row + 1, col))
    elif row == rows:
        c.append(("^", row - 1, col))
    else:
        c.append(("^", row - 1, col))
        c.append(("v", row + 1, col))

    if col == 0:
        c.append((">", row, col + 1))
    elif col == cols:
        c.append(("<", row, col - 1))
    else:
        c.append(("<", row, col - 1))
        c.append((">", row, col + 1))
    return c


def siblings(_, row, col):
    valids = []
    for s, r, c in visitables(row, col):
        if is_reachable((row, col), (r, c)):
            valids.append((s, r, c))
    return valids


def f():
    q = [[S]]
    v = []
    while q:
        path = q.pop(0)
        node = path[-1]
        if not node in v:
            for child in siblings(*node):
                np = path[:]
                np.append(child)
                q.append(np)
                if child[1:] == E[1:]:
                    return np
        v.append(node)
    return []


l = f()
print(len(l) - 1)

for row in range(rows + 1):
    for col in range(cols + 1):
        grid[row][col] = "."

for s in l:
    grid[s[1]][s[2]] = s[0]

for r in grid:
    print(" ".join(r))

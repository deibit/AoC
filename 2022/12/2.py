def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


grid = [list(x) for x in [y for y in get_data("input")]]
rows = len(grid) - 1
cols = len(grid[0]) - 1


E = []
E_COORS = []
S = None
START = "E"
END = "a"
for row in range(rows + 1):
    for col in range(cols + 1):
        if grid[row][col] == START:
            S = ("{", row, col)
            grid[row][col] = ord("{") - 96
            continue
        if grid[row][col] == END:
            E.append((END, row, col))
            E_COORS.append((row, col))
        grid[row][col] = ord(grid[row][col]) - 96


def is_reachable(b, a):
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
    e = []
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
                if child[1:] in E_COORS:
                    e.append(np)
        v.append(node)
    return e


results = f()


minimal = results[0]
for result in results:
    if len(result) < len(minimal):
        minimal = result


# Visualization

for row in range(rows + 1):
    for col in range(cols + 1):
        grid[row][col] = "."

for s in minimal:
    grid[s[1]][s[2]] = s[0]

for r in grid:
    print(" ".join(r))

print(len(minimal) - 1)

def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")

initial = 8
grid_size = 16
visited = [(initial, initial)]
head = (initial, initial)
tail = (initial, initial)

# Log just work with test, not input
def log():
    global tail, head
    grid = [['.' for ii in range(grid_size)] for i in range(grid_size)]
    grid[tail[1]][tail[0]] = 'T'
    grid[head[1]][head[0]] = 'H'
    print("   0__1__2__3__4__5__6__7__8__9__A__B__C__D__E__F")
    for i in range(0, grid_size):
        print(f"{i:2} {'  '.join(grid[i])}")


def move_tail():
    global head, tail
    hx, hy = head
    tx, ty = tail

    # Ovelapping
    if hx == tx and hy == ty:
        return

    # Close enough
    if (abs(hx - tx) < 2 and abs(hy - ty) < 2):
        return

    # H moves in X
    if (not hx == tx) and hy == ty:
        if hx > tx:
            tail = (tx+1, ty)
        else:
            tail = (tx-1, ty)
        return

    # H moves in Y
    elif hx == tx and (not hy == ty):
        if hy > ty:
            tail = (tx, ty + 1)
        else:
            tail = (tx, ty - 1)
        return

    # Diagonal move
    else:
        nx = 0
        ny = 0
        match (hx - tx, hy - ty):
            case (1, -2) | (2, -1):
                nx = 1
                ny = -1
            case (2, 1) | (1, 2):
                nx = +1
                ny = +1
            case (-1, 2) | (-2, 1):
                nx = -1
                ny = +1
            case (-2, -1) | (-1, -2):
                nx = -1
                ny = -1

        tail = (tx + nx, ty + ny)
        return


def move_head(pos):
    global head, tail
    match pos:
        case "L":
            head = (head[0] - 1, head[1])
        case "R":
            head = (head[0] + 1, head[1])
        case "U":
            head = (head[0], head[1] - 1)
        case "D":
            head = (head[0], head[1] + 1)

for line in get_data("input"):
    pos, steps = line.split(" ")
    for step in range(int(steps)):
        move_head(pos)
        move_tail()
        if not tail in visited:
            visited.append(tail)
print(len(visited))
def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")

grid_size = 512
initial = grid_size//2
visited = [(initial, initial)]
rope = [(initial, initial) for _ in range(10)]

# log just work with test, not input
def log():
    global rope, grid_size
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for order, node in enumerate(rope, start=0):
        grid[node[1]][node[0]] = str(order)
    head = rope[0]
    grid[head[1]][head[0]] = 'H'
    #print("   0__1__2__3__4__5__6__7__8__9__A__B__C__D__E__F")
    for i in range(0, grid_size):
        print(f"{i:2} {' '.join(grid[i])}")
    print()

# trail_tail just work with test, not input
def trail_tail(visited):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for row, col in visited:
        grid[col][row] = '#'
    for i in range(0, grid_size):
        print(f"{i:2} {' '.join(grid[i])}")
    print()

def move_rope():
    global rope

    for pos in range(1, len(rope)):
        head = rope[pos-1]
        hx, hy = head
        tx, ty = rope[pos]

        # Ovelapping
        if hx == tx and hy == ty:
            continue

        # Close enough
        if (abs(hx - tx) < 2 and abs(hy - ty) < 2):
            continue

        # H moves in X
        if (not hx == tx) and hy == ty:
            if hx > tx:
                rope[pos] = (tx+1, ty)
            else:
                rope[pos] = (tx-1, ty)

        # H moves in Y
        elif hx == tx and (not hy == ty):
            if hy > ty:
                rope[pos] = (tx, ty + 1)
            else:
                rope[pos] = (tx, ty - 1)

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
                # add diagonal (pos-1) moves
                case (-2, -2):
                    nx = -1
                    ny = -1
                case (2, 2):
                    nx = 1
                    ny = 1
                case (-2, 2):
                    nx = -1
                    ny = 1
                case (2, -2):
                    nx = 1
                    ny = -1
            rope[pos] = (tx + nx, ty + ny)
    return rope[pos]

def move_head(pos):
    global rope
    head = rope[0]
    match pos:
        case "L":
            rope[0] = (head[0] - 1, head[1])
        case "R":
            rope[0] = (head[0] + 1, head[1])
        case "U":
            rope[0] = (head[0], head[1] - 1)
        case "D":
            rope[0] = (head[0], head[1] + 1)

for line in get_data("input"):
    pos, steps = line.split(" ")
    for step in range(int(steps)):
        move_head(pos)
        tail_pos = move_rope()
        visited.append(tail_pos)
print(len(set(visited)))
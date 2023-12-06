def check(X, Y):
    def c(x, y):
        if x == X:
            x = X-1
        if y == Y:
            y = Y-1

        up, down, left, right = y-1, y+1, x-1, x+1

        if up < 0:
            up = y

        if down >= Y:
            down = y if y < Y else Y-1

        if left < 0:
            left = x

        if right >= X:
            right = x if x < X else X-1

        return (up, down, left, right)
    return c

def around(data, x, y, f):
    up, down, left, right = f(x, y)
    return list(set([data[y][x], data[up][x], data[down][x], data[y][left],
        data[y][right]]))

def around_coords(data, x, y, f):
    up, down, left, right = f(x, y)
    coords = list(set([(y, x),(up, x),(down, x),(y, left),(y, right)]))
    X, Y = len(data[0]), len(data)
    return [c for c in coords if not (c[0] >= Y or c[1] >= X)]


def unnine(data, l):
    return [p for p in l if not data[p[0]][p[1]] == 9]


def seek(d, tv, visited, around, check):
    a = unnine(d, around_coords(d, tv[1], tv[0], check))
    for node in a:
        if not node in visited:
            visited.append(node)
            seek(d, node, visited, around, check)

with open('input', 'r') as f:
    data = f.read()
    data = [list(map(int,list(n))) for n in data.split()]

    X = len(data[0])
    Y = len(data)
    check = check(X, Y)

    points = []

    for y in range(Y):
        for x in range(X):
            minimals = around(data, x, y, check)
            if len(minimals) == 1:
                    continue
            elif min(minimals) == data[y][x]:
                points.append((y,x))

    basins = []
    for point in points:
        basin = []
        seek(data, point, basin, around_coords, check)
        if basin:
            basins.append(basin)

    p = 1
    bl = [len(b) for b in basins]
    bl.sort()
    for n in bl[-3:]:
        p *= n
    print(p)




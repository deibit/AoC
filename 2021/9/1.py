with open('input', 'r') as f:
    data = f.read()
    data = [list(map(int,list(n))) for n in data.split()]

    X = len(data[0])
    Y = len(data)

    points = []

    for y in range(Y):
        for x in range(X):
            up, down, left, right = y-1, y+1, x-1, x+1
            if up < 0:
                up = y
            if down >= Y:
                down = y
            if left < 0:
                left = x
            if right >= X:
                right = x

            minimals = [data[y][x], data[up][x], data[down][x], data[y][left], data[y][right]]

            if len(set(minimals)) == 1:
                    continue
            elif min(minimals) == data[y][x]:
                points.append(data[y][x]+1)

    print(sum(points))

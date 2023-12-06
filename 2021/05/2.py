def transform(line):
    line = line.split('->')
    line = [n.strip() for n in line]
    (x1, y1) = line[0].split(',')
    (x2, y2) = line[1].split(',')
    return [int(x1), int(y1), int(x2), int(y2)]


def chevyshev(a, b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))


def line(coords):
    line = []
    x1, y1, x2, y2 = coords

    if x1 == x2:
        for n in range(min(y1, y2), max(y1, y2) + 1):
            line.append([x1, n])
    elif y1 == y2:
        for n in range(min(x1, x2), max(x1, x2) + 1):
            line.append([n, y1])

    # Diagonal
    else:
        m = chevyshev([x1, y1], [x2, y2])

        if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
            x = range(min(x1, x2), min(x1, x2) + m + 1)
            y = range(min(y1, y2), min(y1, y2) + m + 1)

        elif x1 > x2 and y1 < y2:
            x = range(x1, x1 - m - 1, -1)
            y = range(y1, y1 + m + 1)
        elif x1 < x2 and y1 > y2:
            x = range(x1, x1 + m + 1)
            y = range(y1, y1 - m - 1, -1)

        line = [[n[0], n[1]] for n in zip(x,y)]

    return line


with open('input', 'r') as f:
    data = [transform(n) for n in f.readlines()]

    # We could ask for max-x and max-y to adjust the matrix but...lazyness
    matrix = {}

    for coords in data:
        line_set = line(coords)
        for point in line_set:
            point = ",".join([str(n) for n in point])
            if not matrix.get(point):
                matrix[point] = 1
            else:
                matrix[point] += 1

    print(len([p for p in matrix.values() if p > 1]))


tdata = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

with open('input', 'r') as f:
    #data = [list(map(int, n)) for n in tdata.split()]
    data = [list(map(int, n)) for n in f.read().split()]

    X = len(data[0])
    Y = len(data)

    def check(c):
        y, x = c
        if x < 0 or x >= X:
            return False
        if y < 0 or y >= Y:
            return False
        return True

    def around(x, y):
        all_x = [x, x, x+1, x-1, x+1, x-1, x+1, x-1]
        all_y = [y-1, y+1, y, y, y-1, y-1, y+1, y+1]

        p = [c for c in zip(all_y, all_x) if check(c)]
        return p


    flashes = 0
    flash_cache = []

    def flash(x, y):
        global flash_cache
        global flashes

        if data[y][x] > 9 and not (y, x) in flash_cache:
            flashes += 1
            flash_cache.append((y, x))
            a = around(x, y)

            for p in a:
                data[p[0]][p[1]] += 1
                flash(p[1],p[0])

    for i in range(100):
        flash_cache = []
        for y in range(Y):
            for x in range(X):
                data[y][x] += 1

        for y in range(Y):
            for x in range(X):
                flash(x, y)

        for i in flash_cache:
            data[i[0]][i[1]] = 0

    print(flashes)



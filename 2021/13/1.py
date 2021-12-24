with open('input', 'r') as f:
    coors = []
    folds = []

    for line in f.readlines():
        if '=' in line:
            c, v = line.split()[-1].split('=')
            folds.append((c, int(v)))
        elif ',' in line:
            x, y = line.split(',')
            coors.append((int(x),int(y)))

    def debug():
        X = max([i[0] for i in coors]) + 1
        Y = max([i[1] for i in coors]) + 1
        paper = []
        for _ in range(Y):
            paper.append(['.' for _ in range(X)])
        for coor in coors:
            paper[coor[1]][coor[0]] = '#'
        for l in paper:
            print("".join(l))

    def fold(level, horz):
        global coors
        tmp = []
        order = 0 if horz else 1
        for c in coors:
            F = c[order] - level
            if F < 0:
                tmp.append(c)
            elif F > 0:
                c = list(c)
                c[order] = level - F
                tmp.append(tuple(c))
        coors = list(set(tmp))

    debug()
    for c, (order, value) in enumerate(folds):
        print('----')
        horz = True if order == 'x' else False
        fold(value, horz)
        debug()
        print(len(coors))
        break

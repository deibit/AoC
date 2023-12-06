with open('input', 'r') as f:
    data = list(map(int, f.read().split(',')))

def align(data):
    data.sort()
    s = set(data)
    d = {k: 0 for k in s}

    for k in d.keys():
        l = []
        for pos in data:
            l.append(abs(pos-k))
        d[k] = l

    return d

d = align(data)
l = min([sum(v) for v in d.values()])
print(l)

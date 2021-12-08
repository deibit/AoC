with open('input', 'r') as f:
    data = list(map(int, f.read().split(',')))

def stepper(steps):
    return (steps * (1 + steps)) // 2

def align(data):
    data.sort()
    s = set(data)
    m = max(s)
    d = {k: 0 for k in range(m)}

    for k in d.keys():
        l = []
        for pos in data:
            n = stepper(abs(pos-k))
            l.append(n)
        d[k] = l

    return d

d = align(data)
s = min([sum(v) for v in d.values()])
print(s)

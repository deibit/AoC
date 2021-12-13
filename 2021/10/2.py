# 25137 and its divisors
points = {")": 1, "]": 2, "}": 3, ">": 4}
qp = {")": "(", "]": "[", "}": "{", ">":"<"}
pq = {"(": ")", "[": "]", "{": "}", "<":">"}
p = []

with open('input', 'r') as f:
    data = f.read()
    data = data.split()

    balance = []
    for pos, line in enumerate(data):
        for c in line:
            if c in '[({<':
                balance.append(c)
            else:
                r = balance.pop()
                if not r == qp[c]:
                    p.append(pos)
                    continue

    ndata = [l for (pos, l) in enumerate(data) if not pos in p]

    p = []
    for line in ndata:
        balance = []
        for c in line:
            if c in '[({<':
                balance.append(c)
            elif c in '])}>':
                balance.pop()
        if balance:
            balance.reverse()
            l = [pq[c] for c in balance]
            p.append("".join(l))

    scores = []
    for l in p:
        acc = 0
        for c in l:
            acc *= 5
            acc += points[c]
        scores.append(acc)

    scores.sort()
    print(scores[len(scores)//2])


# 25137 and its divisors
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
qp = {")": "(", "]": "[", "}": "{", ">":"<"}
pq = {"(": ")", "[": "]", "{": "}", "<":">"}
p = []

with open('input', 'r') as f:
    data = f.read()
    data = data.split()

    balance = []
    for line in data:
        for pos, c in enumerate(line):
            if c in '[({<':
                balance.append(c)
            else:
                r = balance.pop()
                if not r == qp[c]:
                    print(f"error, expected {pq[r]} instead found {c} {line}")
                    p.append(points[c])
                    continue
    print(sum(p))


tdata = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

with open("input", "r") as f:
    data = f.read().split("\n")
    # data = tdata.split('\n')
    tp = list(data.pop(0))

    rules = {}

    for line in data:
        if line:
            A, B = line.split("->")
            rules[A.strip()] = B.strip()

    for _ in range(10):
        tmp = []
        for idx in range(len(tp) - 1):
            a = tp[idx]
            c = tp[idx + 1]
            b = rules[f"{a}{c}"]
            if tmp:
                tmp.pop()
            tmp.extend([a, b, c])
        tp = tmp

    def maxmin(l):
        d = {}
        for e in l:
            if d.get(e):
                d[e] += 1
            else:
                d[e] = 1

        M = [d[k] for k in d.keys() if d[k] == max(d.values())][0]
        m = [d[k] for k in d.keys() if d[k] == min(d.values())][0]

        return (M, m)

    M, m = maxmin(tp)
    print(M - m)

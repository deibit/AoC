import json


def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


FILE = "input"
data = get_data(FILE)
l_packets = []
r_packets = []

for line in range(0, len(data), 3):
    l_packets.append(json.loads(data[line]))
    r_packets.append(json.loads(data[line + 1]))


def cmp_elems(a, b):
    if type(a) == int:
        a = [a]
    if type(b) == int:
        b = [b]

    for x, y in zip(a, b):
        if isinstance(x, list) or isinstance(y, list):
            r = cmp_elems(x, y)
        else:
            r = y - x
        if r != 0:
            return r
    return len(b) - len(a)


results = []
for n, (l, r) in enumerate(zip(l_packets, r_packets), 1):
    r = cmp_elems(l, r)
    if r > 0:
        results.append(n)

print(results)
print(sum(results))

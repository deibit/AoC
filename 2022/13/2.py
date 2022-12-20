import json
from functools import cmp_to_key


def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


FILE = "input"
data = get_data(FILE)
packets = [[[2]], [[6]]]

for line in data:
    if line:
        packets.append(json.loads(line))


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


packets.sort(key=cmp_to_key(cmp_elems), reverse=True)
decoder_key = 1
for idx, p in enumerate(packets, 1):
    if p in [[[2]], [[6]]]:
        decoder_key *= idx

print(decoder_key)

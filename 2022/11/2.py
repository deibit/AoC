from functools import cache


def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


data = get_data("input")
monkeys = []

for lines in range(0, len(data), 7):
    d = data[lines : lines + 7]
    b = d[2].split("=")[1].split()[2]
    if b.isnumeric():
        b = int(b)
    else:
        b = None
    monkeys.append(
        {
            "id": d[0][-2],
            "si": [int(i) for i in d[1].split(":")[1].split(",")],
            "op": d[2].split("=")[1].split()[1],
            "b": b,
            "by": int(d[3].split()[-1]),
            "tr": int(d[4].split()[-1]),
            "fl": int(d[5].split()[-1]),
            "ct": 0,
        }
    )


@cache
def throw(wl, by, tr, fl):
    if wl % by == 0:
        return tr
    return fl


@cache
def add(a, b):
    return a + b


@cache
def mul(a, b):
    return a * b


# WORRYLEVELMODULATOR = 23 * 13 * 19 * 17  # test
WORRYLEVELMODULATOR = 13 * 7 * 3 * 19 * 5 * 2 * 11 * 17
for round in range(10000):
    for monkey in monkeys:
        by, tr, fl = monkey["by"], monkey["tr"], monkey["fl"]
        try:
            while 1:
                old = monkey["si"].pop(0)
                new = None
                op = monkey["op"]
                b = monkey["b"]

                if b is None:
                    new = mul(old, old)
                else:
                    if op == "+":
                        new = add(old, b)
                    if op == "*":
                        new = mul(old, b)

                monkey["ct"] += 1
                monkeys[throw(new % WORRYLEVELMODULATOR, by, tr, fl)]["si"].append(
                    new % WORRYLEVELMODULATOR
                )
        except IndexError:
            continue

cts = [m["ct"] for m in monkeys]
cts.sort(reverse=True)
print(cts[0] * cts[1])

def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")

data = get_data("input")
monkeys = []

for lines in range(0, len(data), 7):
    d = data[lines : lines + 7]
    monkeys.append(
        {
            "id": d[0][-2],
            "si": [int(i) for i in d[1].split(":")[1].split(",")],
            "op": d[2].split("=")[1].split(),
            "by": int(d[3].split()[-1]),
            "tr": int(d[4].split()[-1]),
            "fl": int(d[5].split()[-1]),
            "ct": 0
        }
    )

def inspect(ops, wl):
    a, op, b = ops

    if a == 'old':
        a = wl
    else:
        a = int(a)

    if b == 'old':
        b = wl
    else:
        b = int(b)

    match op:
        case '*':
            return a * b
        case '+':
            return a + b

def throw(wl, by, tr, fl):
    if wl % by == 0:
        return tr
    return fl

for _ in range(20):
    for monkey in monkeys:
        try:
            while 1:
                old = monkey["si"].pop(0)
                new = inspect(monkey["op"], old)
                monkey["ct"] += 1
                monkeys[throw(new // 3, monkey["by"], monkey["tr"], monkey["fl"])]["si"].append(new // 3)
        except IndexError:
            continue

cts = [m["ct"] for m in monkeys]
cts.sort()

print(cts[-1] * cts[-2])
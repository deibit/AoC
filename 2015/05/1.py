from utils.f import readinput

entries = readinput(__file__).split()


def check(l):
    b = ["ab", "cd", "pq", "xy"]
    for bb in b:
        if bb in l:
            return True
    return False


def count(l):
    l = list(l)
    c = 0
    for v in "aeiou":
        c += l.count(v)
    return c


def has_pair(l):
    for pos in range(len(l) - 1):
        if l[pos] == l[pos + 1]:
            return True
    return False


c = 0
for line in entries:
    if check(line):
        continue
    if count(line) < 3:
        continue
    if len(set(line)) == len(line):
        continue
    if not has_pair(line):
        continue
    c += 1

print(c)

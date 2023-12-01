with open("input.txt") as f:
    s = 0
    lines = f.readlines()
    for line in lines:
        n = [c for c in line if c.isdigit()]
        c = int("".join([n[0], n[-1]]))
        s += c
print(s)

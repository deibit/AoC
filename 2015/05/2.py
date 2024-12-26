from utils.f import readinput

entries = readinput(__file__).split()


def has_pairs(line):
    for pos in range(len(line) - 1):
        for other in range(pos + 2, len(line) - 1):
            if (line[pos], line[pos + 1]) == (line[other], line[other + 1]):
                return True
    return False


def has_xyx_pattern(line):
    for pos in range(len(line) - 2):
        if line[pos] == line[pos + 2] and line[pos] != line[pos + 1]:
            return True
    return False


c = 0
for line in entries:
    if has_pairs(line) and has_xyx_pattern(line):
        c += 1
print(c)

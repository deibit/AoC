with open('input', 'r') as f:
    lanterns = [int(n) for n in f.readlines()[0].strip().split(',')]

nl = 0
for day in range(80):
    for pos in range(len(lanterns)):
        if lanterns[pos] == 0:
            lanterns[pos] = 6
            nl += 1
        else:
            lanterns[pos] -= 1
    [lanterns.append(8) for _ in range(nl)]
    nl = 0

print(len(lanterns))

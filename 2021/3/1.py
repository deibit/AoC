with open("input", "r") as f:
    diagnostics = [n.strip() for n in f.readlines()]
    width = len(diagnostics[0])

    measures = [{"0": 0, "1": 0} for _ in range(width)]

    for line in diagnostics:
        for pos, e in enumerate(list(line)):
            measures[pos][e] += 1

    gamma = []
    for measure in measures:
        if measure["1"] > measure["0"]:
            gamma.append("1")
        else:
            gamma.append("0")

    gamma = int("".join(gamma), 2)
    epsilon = gamma ^ int("1" * width, 2)

    print(gamma * epsilon)

import re

# First "trap". Watch for negative numbers in your regex
lines = [
    [int(n) for n in re.findall(r"-?\d+", line)]
    for line in open("input.txt").readlines()
]


def diff(line):
    return [line[i + 1] - line[i] for i in range(len(line) - 1)]


def predict(lines):
    lines[-1].append(0)
    for line in range(len(lines) - 2, -1, -1):
        lines[line - 1].append(lines[line][-1] + lines[line - 1][-1])
    return lines[0][-1]


results = []
for current in lines:
    history = []
    # Second trap. If this condition check for sum(current) != 0 it will fail because -n + n == 0
    while sum([abs(n) for n in current]):
        history.append(current)
        current = diff(current)
    history.append(current)
    results.append(predict(history))

print(sum(results))

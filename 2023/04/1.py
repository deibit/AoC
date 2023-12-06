import re

"""
hate to hardcode numbers.

6 will make test, 11 will do sample

"""


def cards(filename):
    acum = 0
    for line in open(filename):
        numbers = re.findall(r"\d+", line)
        numbers = [int(n) for n in numbers]
        r = set(numbers[1:11]).intersection(set(numbers[11:]))
        if len(r) > 0:
            acum += 2 ** (len(r) - 1)
    return acum


print(cards("input.txt"))

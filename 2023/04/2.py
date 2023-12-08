"""
This problem is awesome.

Took me two days thinking in the solution and 5 minutes to implement import

Yes, the Lincoln quote paid it

"""


import re

cards = [0 for _ in range(0, 212)]
accum = 0


def process(filename, sep):
    global prices, cards, accum
    for line in open(filename):
        numbers = re.findall(r"\d+", line)
        numbers = [int(n) for n in numbers]
        r = len(set(numbers[1:sep]).intersection(set(numbers[sep:])))

        idx = numbers[0] - 1
        cards[idx] += 1

        for _ in range(cards[idx]):
            for j in range(idx + 1, idx + r + 1):
                cards[j] += 1


TEST = ("sample.txt", 6)
INPT = ("input.txt", 11)

process(*INPT)
print(cards, sum(cards))

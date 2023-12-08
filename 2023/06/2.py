"""

Well...it appears that part2 is even fewer lines than part1...

"""

import re

lines = open("input.txt").readlines()
time = int("".join([n for n in re.findall(r"\d+", lines[0])]))
distance = int("".join([n for n in re.findall(r"\d+", lines[1])]))

good = 0
for i in range(1, time // 2):
    if i * (time - i) > distance:
        good += 1

print((good * 2) + 1)

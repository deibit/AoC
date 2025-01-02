import re

from utils.f import readinput, readtest

entries = readinput(__file__).split("\n")
TIMES = 50

# entries = readtest(__file__).split("\n")
# entries: list[str] = [e for e in entries if e]
# TIMES = 5


# Take a single digit, group its one ore more repetitions
r = re.compile(r"(\d)\1*")

seq = entries[0]

for _ in range(TIMES):
    seq = "".join([f"{len(g[0])}{g[0][0]}" for g in re.finditer(r, seq)])

print(len(seq))

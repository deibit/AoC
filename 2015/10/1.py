from utils.f import readinput, readtest

entries = readinput(__file__).split("\n")

# entries = readtest(__file__).split("\n")
# entries: list[str] = [e for e in entries if e]
# TIMES = 5

TIMES = 40

seq = entries[0]

for _ in range(TIMES):
    nseq = ""
    i = 0
    while i < len(seq):
        c = seq[i]
        p = 1
        while p + i < len(seq) and seq[i + p] == c:
            p += 1
        nseq += f"{p}{c}"
        i += p
    seq = nseq


print(len(seq))

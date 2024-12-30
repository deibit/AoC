from utils.f import readinput, readtest

entries = readinput(__file__).split("\n")
# entries = readtest(__file__).split("\n")
# entries: list[str] = [e for e in entries if e]

code = 0
recode = 0
for entry in entries:
    code += len(entry)

    c = repr(entry).replace('"', '\\"')
    recode += len(c)

print(recode - code)

from utils.f import readinput, readtest

entries = readinput(__file__).split("\n")
# entries = readtest(__file__).split("\n")
# entries: list[str] = [e for e in entries if e]

memory = 0
code = 0

for entry in entries:
    memory += len(entry.encode("utf-8").decode("unicode_escape")) - 2  # drop the " "
    code += len(entry)

print(f"Resp: {code - memory}")

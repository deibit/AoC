from utils.f import readinput

entries = readinput(__file__)

print(sum([1 if n == "(" else -1 for n in entries]))

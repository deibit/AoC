def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")

register_X = 1
cycles = []

for instruction in get_data('input'):
    match instruction:
        case "noop":
            cycles.append(register_X)
        case _:
            cycles.append(register_X)
            cycles.append(register_X)
            register_X += int(instruction.split(' ')[1])

freqs = [f*cycles[f-1] for f in range(20,230,40)]
print(sum(freqs))
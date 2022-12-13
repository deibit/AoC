def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")

register_X = 1
cycles = 0
screen = ['░' for _ in range(240)]
sprite = []

def draw_pixel():
    global sprite
    idx = cycles - 1
    screen[idx] = sprite[idx%40]

def cycle():
    global cycles
    cycles += 1
    draw_pixel()

def clamp(x):
    if x < 0:
        return 0
    if x > 39:
        return 39
    return x

def reset_sprite():
    global sprite
    sprite = ['░' for _ in range(40)]
    sprite[clamp(register_X - 1)] = '█'
    sprite[clamp(register_X)] = '█'
    sprite[clamp(register_X + 1)] = '█'

reset_sprite()
for instruction in get_data('input'):
    match instruction:
        case "noop":
            cycle()
        case _:
            cycle()
            cycle()
            register_X += int(instruction.split(' ')[1])
            reset_sprite()

for line in range(0, 240, 40):
    print("".join(screen[line:line+40]))
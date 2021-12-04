with open('input', 'r') as f:
    orders = [n.strip() for n in f.readlines()]
    pos = 0
    dep = 0
    aim = 0
    for order in orders:
        cmd, mag = order.split()
        mag = int(mag)
        if cmd == 'forward':
            pos += mag
            dep += (aim * mag)
        elif cmd == 'down':
            aim += mag
        elif cmd == 'up':
            aim -= mag

    print(pos * dep)

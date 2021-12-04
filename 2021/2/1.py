with open('input', 'r') as f:
    orders = [n.strip() for n in f.readlines()]
    pos = 0
    dep = 0
    for order in orders:
        cmd, mag = order.split()
        mag = int(mag)
        if cmd == 'forward':
            pos += mag
        elif cmd == 'down':
            dep += mag
        elif cmd == 'up':
            dep -= mag

    print(pos * dep)

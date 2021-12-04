with open('input', 'r') as f:
    depths = [int(n.strip()) for n in f.readlines()]
    increasings = 0
    for pos, depth in enumerate(depths):
        if pos+1 == len(depths):
            break
        elif depths[pos] < depths[pos+1]:
            increasings += 1

    print(increasings)

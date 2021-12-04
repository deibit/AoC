with open('input', 'r') as f:
    depths = [int(n.strip()) for n in f.readlines()]
    increasings = 0
    for pos, depth in enumerate(depths):
        if pos+3 == len(depths):
            break
        elif (depths[pos] + depths[pos+1] + depths[pos+2]) < (depths[pos+1] + depths[pos+2] + depths[pos+3]):
            increasings += 1

    print(increasings)


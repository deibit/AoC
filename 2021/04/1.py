import sys

def unpunch(board, numbers):
    flat = [e for line in board for e in line]
    return sum([int(n) for n in list(set(flat) - set(numbers))])


def check(board, numbers):
    punch = [[0 for _ in range(5)] for _ in range(5)]

    for x, line in enumerate(board):
        for y, col in enumerate(line):
            if col in numbers:
                punch[x][y] = 1

    for line in punch:
        if all(line):
            return unpunch(board, numbers)

    # thx https://stackoverflow.com/a/6473724/91267
    punch = list(map(list, zip(*punch)))

    for line in punch:
        if all(line):
            return unpunch(board, numbers)

    return False


with open('input', 'r') as f:
    data = [n.strip() for n in f.readlines()]

    numbers = data[0].split(',')
    data = data[2:]
    boards = []

    for idx in range(0, len(data), 6):
        lines = [n.split() for n in data[idx: idx+5]]
        boards.append(lines)

    for slice in range(len(numbers)):
        for board in boards:
            if winning_board := check(board, numbers[0:slice]):
                last_number = int(numbers[0:slice].pop())
                print(winning_board * last_number)
                sys.exit()



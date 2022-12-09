from functools import reduce


def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read().split("\n")


def get_score(row, col, grid, max):

    north, west, south, east = range(4)
    value = grid[row][col]
    flags = [True, True, True, True]
    scores = [0, 0, 0, 0]

    def check(r, c, d):
        v = grid[r][c]
        if v >= value:
            flags[d] = False
        scores[d] += 1

    for i in range(1, max):
        if flags[north] and row - i >= 0:
            check(row - i, col, north)
        if flags[west] and col - i >= 0:
            check(row, col - i, west)
        if flags[south] and row + i < max:
            check(row + i, col, south)
        if flags[east] and col + i < max:
            check(row, col + i, east)
    final_score = 1
    for score in scores:
        final_score *= score
    return final_score


data = get_data("input")
grid = []
for line in data:
    grid.append(list(line))

MAX = len(grid[0])

scores = []
for row in range(MAX):
    for col in range(MAX):
        scores.append(get_score(row, col, grid, max=MAX))
print(max(scores))

import re

lines = open("input.txt").readlines()
times = [int(n) for n in re.findall(r"\d+", lines[0])]
distances = [int(n) for n in re.findall(r"\d+", lines[1])]

tds = zip(times, distances)
# print(*tds)

# There is no need to calculate half of the time/speed relations
goods = []
for td in tds:
    good = 0
    # odd ranges gives even iterations, even gives odd...
    if td[0] % 2:
        for i in range(1, (td[0] // 2) + 1):
            if i * (td[0] - i) > td[1]:
                good += 1
        goods.append(good * 2)
    else:
        for i in range(1, (td[0] // 2)):
            if i * (td[0] - i) > td[1]:
                good += 1
        goods.append((good * 2) + 1)

result = 1
for good in goods:
    result *= good
print(result)

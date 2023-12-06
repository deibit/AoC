def max_bit(values, pos, more):
    measures = {"0": 0, "1": 0}

    for value in values:
        measures[value[pos]] += 1

    if more:
        if measures['0'] > measures['1']:
            return '0'
        return '1'
    else:
        if measures['1'] < measures['0']:
            return '1'
        return '0'


# It worked but what would happened if any of the input entries were equal?
# Probably we should deal with a if pos == len(l[0]): return l[0]
def r(l, pos, m):
    if len(l) == 1:
        return l[0]
    else:
        bit = max_bit(l, pos, m)
        nl = [n for n in l if n[pos] == bit]
        return r(nl, pos+1, m)


with open("input", "r") as f:
    diagnostics = [n.strip() for n in f.readlines()]
    width = len(diagnostics[0])

    o2 = int(r(diagnostics, 0, True), 2)
    co2 = int(r(diagnostics, 0, False) ,2)
    print(o2 * co2)

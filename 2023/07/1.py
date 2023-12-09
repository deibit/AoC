lines = open("input.txt").readlines()

card_types = ["KIND5", "KIND4", "HOUSE", "KIND3", "TWOPA", "ONEPA", "HIGHC"]
order_type = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
order = {k: v for k, v in zip(order_type, range(len(order_type) + 1, 1, -1))}
score = len(lines)


def kind(cards):
    sets = set(cards)
    match len(sets):
        case 5:
            return "HIGHC"
        case 1:
            return "KIND5"
        case 4:
            return "ONEPA"
        case 2:
            if 4 in [cards.count(c) for c in cards]:
                return "KIND4"
            return "HOUSE"
        case 3:
            if 3 in [cards.count(c) for c in cards]:
                return "KIND3"
            return "TWOPA"


def ordering(c1, c2):
    for l, r in zip(c1[0], c2[0]):
        if order[l] == order[r]:
            continue
        if order[l] > order[r]:
            return c1
        return c2


stack = {}

for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    hand_bid = (hand, bid)
    k = kind(hand)

    if k in stack:
        kind_list = stack[k]
        for pos in range(0, len(kind_list)):
            if hand_bid == ordering(hand_bid, kind_list[pos]):
                kind_list.insert(pos, hand_bid)
                break
        if not hand_bid in kind_list:
            kind_list.append(hand_bid)
    else:
        stack[k] = [hand_bid]

accum = 0
for card_type in card_types:
    if card_type in stack:
        for card in stack[card_type]:
            accum += card[1] * score
            score -= 1


print(accum)

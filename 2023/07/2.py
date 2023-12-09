lines = open("input.txt").readlines()

card_types = ["KIND5", "KIND4", "HOUSE", "KIND3", "TWOPA", "ONEPA", "HIGHC"]
order_type = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
order = {k: v for k, v in zip(order_type, range(len(order_type) + 1, 1, -1))}
score = len(lines)
HAND_SIZE = 5


def ascend(hand):
    hand_as_list = list(hand.replace("J", ""))
    jes = HAND_SIZE - len(hand_as_list)

    # Yes, the classic corner case
    if jes == 5:
        return "AAAAA"

    hand_lengths = [(c, hand_as_list.count(c)) for c in set(hand_as_list)]

    selected = hand_lengths[0]
    for hand_length in hand_lengths[1:]:
        if selected and selected[1] < hand_length[1]:
            selected = hand_length

    for _ in range(0, jes):
        hand_as_list.append(selected[0])

    return "".join(hand_as_list)


def kind(cards):
    if "J" in cards:
        cards = ascend(cards)
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

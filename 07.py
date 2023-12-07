from collections import Counter
lines = [li.strip() for li in open('input.txt')]

def type_(hand):
    cntr = Counter(hand)
    jokers = cntr.pop('R', 0)
    if jokers == 5:
        return 7

    counts = sorted(cntr.values())
    counts[-1] += jokers
    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
        case _:
            return 1

def f(lines):
    ranks = []
    for hand, bid in map(lambda x: x.split(), lines):
        ty = type_(hand)
        strength = tuple(map('R23456789TJQKA'.index, hand))
        ranks.append((ty, strength, int(bid)))
    ranks.sort()
    return sum( r * bid for r, (*_, bid) in enumerate(ranks, start=1) )

print(f(lines))
print(f([li.replace('J', 'R') for li in lines]))

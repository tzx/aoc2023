import math
import re
from collections import Counter
lines = [li.strip() for li in open('input.txt')]

res1 = res2 = 0

for l in lines:
    game, rest = l.split(': ')
    game_id = int(re.search(r'\d+', game).group(0))
    configs = rest.split('; ')

    max_cntr = Counter()
    valid = True
    for cfg in configs:
        for item in cfg.split(', '):
            amt, color = item.split(' ')
            amt = int(amt)
            if amt > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                valid = False
            max_cntr[color] = max(max_cntr[color], amt)

    if valid:
        res1 += game_id
    res2 += math.prod(max_cntr.values())

print(res1)
print(res2)

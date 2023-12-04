import re
from collections import defaultdict

lines = [li.strip() for li in open('input.txt')]

res1 = 0
cards = defaultdict(int)
for i, li in enumerate(lines):
    _, rest = li.split(': ')
    win, mine = rest.split(' | ')
    winning = set(re.findall(r'\d+', win))
    mine = re.findall(r'\d+', mine)

    cnt = len([m for m in mine if m in winning])
    if cnt: res1 += 2 ** (cnt - 1)

    # New discovery: defaultdict vs Counter
    # defaultdict puts 0 if missing when querying, Counter does not
    for _ in range(cards[i] + 1):
        for j in range(cnt):
            cards[i + j + 1] += 1

# This allows this to work, which fucked up when I used Counter lol
res2 = sum(v + 1 for k,v in cards.items())
# Alternative which I used when debugging:
# res2 = sum(cards[k] + 1 for k in range(len(lines)))
print(res1)
print(res2)

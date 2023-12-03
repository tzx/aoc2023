import math
import string
import re
from collections import defaultdict

lines = [li.strip() for li in open('input.txt')]

sym = set()
for r, row in enumerate(lines):
    for c, cell in enumerate(row):
        if cell not in string.digits + '.':
            sym.add((r, c))

gears = defaultdict(list)
res1 = 0
for r, row in enumerate(lines):
    for match in re.finditer(r'\d+', row):
        st, end = match.span()
        neighbors = set()
        for c in range(st, end):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    neighbors.add((r + dy, c + dx))

        if len(neighbors & sym) > 0:
            # __getitem__
            res1 += int(match[0])

        for nr, nc in neighbors:
            if nr not in range(len(lines)) or nc not in range(len(lines[0])):
                continue
            if lines[nr][nc] != '*':
                continue
            gears[(nr, nc)].append(int(match[0]))

res2 = sum(v[0] * v[1] for k, v in gears.items() if len(v) == 2)
print(res1)
print(res2)

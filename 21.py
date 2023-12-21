import re
import math
from collections import deque

grid = [list(l.strip()) for l in open('input.txt')]
STEPS = 64
m, n = len(grid), len(grid[0])
Q = deque([])

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 'S':
            grid[r][c] = '.'
            Q.append( (r, c) )

for level in range(1, STEPS + 1):
    to_add = set()
    while Q:
        r, c, *_ = Q.popleft()
        for dr, dc in [ (0,1), (0,-1), (1,0), (-1,0) ]:
            nr, nc = (r + dr) % m, (c + dc) % n
            if nr not in range(m) and nc not in range(n): continue
            if grid[nr][nc] not in '.': continue
            to_add.add( (nr, nc) )

    Q.extend(list(to_add))
print(len(Q))


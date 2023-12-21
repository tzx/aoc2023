import numpy as np
from collections import deque

G = { (r, c): cell for r, row in enumerate(open('input.txt')) for c, cell in enumerate(row.strip()) }
N = max([r for r, _ in G.keys()]) + 1

def possible(steps):
    grid = G.copy()

    Q = deque([])
    for (r, c), v in grid.items():
        if v == 'S':
            Q.append( (r, c) )

    for level in range(1, steps + 1):
        to_add = set()
        while Q:
            r, c = Q.popleft()
            for dr, dc in [ (0,1), (0,-1), (1,0), (-1,0) ]:
                nr, nc = (r + dr), (c + dc)
                mr, mc = nr % N, nc % N
                grid[nr, nc] = grid[mr, mc]
                # if nr not in range(N) and nc not in range(N): continue
                if grid[mr,mc] not in '.S': continue
                to_add.add( (nr, nc) )

        Q.extend(list(to_add))
    return len(Q)

print(possible(64))

# Because input has S in center(square) and it is like +, we reach same "state" after len(grid)
C = N // 2
P = [(0, possible(C)), 
    (1, possible(C + N)), 
    (2, possible(C + 2 * N))]

def n2(points, x):
    coefficients = np.polyfit(*zip(*points), 2)
    result = np.polyval(coefficients, x)
    return result

v = 26501365 // N
print(n2(P, v))

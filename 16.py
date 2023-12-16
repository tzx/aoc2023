from collections import deque

grid = [l.strip() for l in open('input.txt')]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
next_d = { 
        '.': [[(-1, 0)],
              [(1, 0)],
              [(0, -1)],
              [(0, 1)]],
        '/': [[(0, 1)],
              [(0, -1)],
              [(1, 0)],
              [(-1, 0)]],
        '\\': [[(0, -1)],
               [(0, 1)],
               [(-1, 0)],
               [(1, 0)]],
        '-':  [[(0, -1), (0, 1)],
               [(0, -1), (0, 1)],
               [(0, -1)],
               [(0, 1)]],
        '|':  [[(-1, 0)],
               [(1, 0)],
               [(-1, 0), (1, 0)],
               [(-1, 0), (1, 0)]]
}

def bfs(start):
    visited = { start }
    q = deque([start])
    while q:
        r, c, old_d = q.popleft()
        cell = grid[r][c]
        for d in next_d[cell][dirs.index(old_d)]:
            new_r, new_c = r + d[0], c + d[1]
            if new_r not in range(len(grid)) or new_c not in range(len(grid[0])):
                continue
            if (new_r, new_c, d) in visited:
                continue
            new = (new_r, new_c, d)
            visited.add(new)
            q.append(new)
    return len(set((x, y) for x, y, _ in visited))

r1 = bfs((0, 0, (0, 1)))
print(r1)

r2 = 0
for r in range(len(grid)):
    r2 = max( r2, bfs( (r, 0, (0, 1)) ) )
    r2 = max( r2, bfs( (r, len(grid[0]) - 1, (0, -1)) ) )
for c in range(len(grid[0])):
    r2 = max( r2, bfs( (0, c, (1, 0)) ) )
    r2 = max( r2, bfs( (len(grid) - 1, c, (-1, 0)) ) )
print(r2)

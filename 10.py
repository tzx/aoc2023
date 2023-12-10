from collections import deque
grid = [li.strip() for li in open('input.txt')]

res1 = res2 = 0

# North, East, South, West
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# valid[c][i] means for c you can move in dirs[i]
valid = {
    '|' : (True, False, True, False),
    '-' : (False, True, False, True),
    'L' : (True, True, False, False),
    'J' : (True, False, False, True),
    '7' : (False, False, True, True),
    'F' : (False, True, True, False),
    # From inspection on input, we can go south and east, just like example x)
    'S' : (False, True, True, False),
}

visited = set()
q = deque()
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == 'S':
            q.append((i, j, 0))
            visited.add((i, j))

nums = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

while q:
    y, x, l = q.popleft()
    nums[y][x] = l
    pipe = grid[y][x]
    res1 = max(res1, l)
    for i, (dy, dx) in enumerate(dirs):
        ny, nx = y + dy, x + dx
        if (ny, nx) in visited: continue
        if ny not in range(len(grid)) or nx not in range(len(grid[0])): continue
        if grid[ny][nx] == '.': continue
        if not valid[pipe][i]: continue

        visited.add((ny, nx))
        q.append((ny, nx, l + 1))

print(res1)

for i, row in enumerate(grid):
    inside = False
    left_on_south = None
    for j, c in enumerate(row):
        if (i, j) in visited:
            if c == '|':
                inside = not inside
            elif c in 'LFS':
                left_on_south = c == 'L'
            elif c in '7J':
                right_on_south = c == 'J'
                if left_on_south != right_on_south:
                    inside = not inside
                left_on_south = None
        else:
            res2 += inside
print(res2)

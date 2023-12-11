grid = [l.strip() for l in open('input.txt')]
ext_row = []
ext_col = []

for i, li in enumerate(grid):
    if '#' not in li:
        ext_row.append(i)

for j in range(len(grid[0])):
    if all(grid[i][j] == '.' for i in range(len(grid))):
        ext_col.append(j)

def shift(r, c, space):
    r += sum(j < r for j in ext_row) * (space - 1)
    c += sum(i < c for i in ext_col) * (space - 1)
    return r, c

res1 = res2 = 0
p1_grid = [shift(r, c, 2) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '#']

for x1, y1 in p1_grid:
    for x2, y2 in p1_grid:
        res1 += abs(x1 - x2) + abs(y1 - y2)
print(res1 // 2)

p2_grid = [shift(r, c, 1000000) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '#']

for x1, y1 in p2_grid:
    for x2, y2 in p2_grid:
        res2 += abs(x1 - x2) + abs(y1 - y2)
print(res2 // 2)

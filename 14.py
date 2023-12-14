grid = [list(li.strip()) for li in open('input.txt')]

m, n = len(grid), len(grid[0])

def up():
    for c in range(n):
        oi = 0
        for r in range(m):
            if grid[r][c] == '#':
                oi = r + 1
            if grid[r][c] == 'O':
                grid[r][c] = '.'
                grid[oi][c] = 'O'
                oi += 1

def rotate():
    global grid
    grid = [ list(x) for x in zip(*grid) ]
    grid = [row[::-1] for row in grid]

def score():
    return sum(row.count('O') * (m-r) for r, row in enumerate(grid))

def repr():
    return ''.join([ ''.join(row) for row in grid])

def from_str(st):
    return [ list(st[i:i+n]) for i in range(0, len(st), n) ]

up()
print(score())

grid = [list(li.strip()) for li in open('input.txt')]

seen = {repr(): 0}
cycles = 1000000000

def f():
    for i in range(1, cycles):
        for _ in range(4): up(); rotate()
        h = repr()
        if h in seen:
            prev = seen[h]
            period = i - prev
            for rp, idx in seen.items():
                if idx < prev: continue
                if (cycles - idx) % period == 0:
                    global grid
                    grid = from_str(rp)
                    return score()
        seen[h] = i

print(f())

import sys
from functools import cache

sys.setrecursionlimit(1000000)

G = [list(l.strip()) for l in open('input.txt')]
# G = [list(l.strip()) for l in open('sample.txt')]
M, N = len(G), len(G[0])
visited = [[False for _ in range(N)] for _ in range(M)]

pos = []

# @cache
def dfs(r, c, cur, p2 = False):
    if r not in range(len(G)): return
    if c not in range(len(G[0])): return
    if G[r][c] == '#': return
    if visited[r][c]: return

    if r == len(G)-1 and c == len(G[0]) - 2:
        pos.append(cur)
        return

    visited[r][c] = True
    match G[r][c], p2:
        case '>', False:
            dfs(r, c + 1, cur + 1, p2)
        case '<', False:
            dfs(r, c - 1, cur + 1, p2)
        case '^', False:
            dfs(r - 1, c, cur + 1, p2)
        case 'v', False:
            dfs(r + 1, c, cur + 1, p2)
        case _:
            dfs(r + 1, c, cur + 1, p2)
            dfs(r - 1, c, cur + 1, p2)
            dfs(r, c + 1, cur + 1, p2)
            dfs(r, c - 1, cur + 1, p2)

    visited[r][c] = False

dfs(0, 1, 0)
print(max(pos))

pos = []
dfs(0, 1, 0, True)
print(max(pos))

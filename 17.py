from collections import defaultdict
import heapq

grid = [l.strip() for l in open('input.txt')]
M, N = len(grid), len(grid[0])

dirs = [-1j, 1j, -1, 1]

# have to do this instead of tuple because i can't cmp complex numbers
class Node:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost
    def __str__(self):
        return "{} : {}".format(self.node, self.cost)

# NOOOOO: slow as shit even with pypy3
def bellman_ford():
    V = len(G)
    distances = { v: float('inf') for v in G }
    distances[0, 1, 0] = 0

    for _ in range(V - 1):
        for v, edges in G.items():
            for neigh, cost in edges:
                if distances[v] + cost < distances[neigh]:
                    distances[neigh] = distances[v] + cost
    return min(distances[complex(N-1, M-1), d, m] for d in dirs for m in range(max_move + 1))


# graph (i, j), (dirs), (moved) -> node, cost
# (i, j), d, m
#   => i, j + d, d, m + 1 if m < 3
#   => i, j + d', d', 1 for d' in dirs if d' != d
def dijkstra(G, s, min_move, max_move):
    s = (0, s, 0)
    distances = { v: float('inf') for v in G }
    distances[s] = 0
    q = []
    heapq.heappush(q, Node(s, 0))

    while q:
        n = heapq.heappop(q)
        u = n.node
        for v, cost  in G[u]:
            alt = distances[u] + cost
            if alt < distances[v]:
                distances[v] = alt
                heapq.heappush(q, Node(v, alt))
    return min(distances[complex(N-1, M-1), d, m] for d in dirs for m in range(min_move, max_move + 1))

def graph(min_move, max_move):
    G = defaultdict(list)
    for r in range(M):
        for c in range(N):
            cell = complex(c, r)
            for old_d in dirs:
                for m in range(max_move + 1):
                    node = (cell, old_d, m)
                    neighbors = []
                    for d in dirs:
                        if d == -old_d:
                            continue
                        neigh = cell + d
                        nc, nr = int(neigh.real), int(neigh.imag)
                        if not (nr in range(M) and nc in range(N)):
                            continue
                        cost = int(grid[nr][nc])

                        if d == old_d and m < max_move:
                            neighbors.append( ((neigh, d, m + 1), cost) )
                        elif d != old_d and m >= min_move:
                            neighbors.append( ((neigh, d, 1), cost) )
                    G[node].extend(neighbors)
    return G

G1 = graph(0, 3)
r1 = min(dijkstra(G1, 1, 0, 3), dijkstra(G1, 1j, 0, 3))
print(r1)

G2 = graph(4, 10)
r2 = min(dijkstra(G2, 1, 4, 10), dijkstra(G2, 1j, 4, 10))
print(r2)

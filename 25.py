from collections import defaultdict
import random
import re

ll = [l.strip() for l in open('input.txt')]

V, E = set(), set()
for l in ll:
    ws = re.findall(r'\w+', l)
    src, dests = ws[0], ws[1:]
    V.add(src)
    for dest in dests:
        V.add(dest)
        edge = sorted( (src, dest) )
        E.add(tuple(edge))
E = list(E)

class DisjointSet():
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.parent[y] = x
        if self.parent[y] == self.parent[x]:
            self.rank[x] += 1

# I love Monte Carlo!!!!
def karger():
    DSU = DisjointSet()
    for v in V:
        DSU.rank[v] = 0
        DSU.parent[v] = v

    n_v = len(V)
    while n_v > 2:
        i = random.randrange(0, len(E))
        src, des = E[i]
        subset_1 = DSU.find(src)
        subset_2 = DSU.find(des)
        if subset_1 == subset_2: continue
        n_v -= 1
        DSU.union(subset_1, subset_2)

    cut_edges = []
    for e in E:
        s1, s2 = DSU.find(e[0]), DSU.find(e[1])
        if s1 != s2:
            cut_edges.append((e[0], e[1]))
    return cut_edges

while len(to_remove := karger()) != 3:
    continue

S1, S2 = to_remove[0]
E = [e for e in E if e not in to_remove]

G = defaultdict(list)
for a, b in E:
    G[a].append(b)
    G[b].append(a)

def connected(node):
    visited = set()
    def dfs(n):
        if n in visited: return
        visited.add(n)
        for neigh in G[n]:
            dfs(neigh)
    dfs(node)
    return visited

print(len(connected(S1)) * len(connected(S2)))

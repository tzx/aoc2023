import math
import re

lines = [li.strip() for li in open('input.txt').read().split('\n\n')]

ins = str(lines[0])
rest = lines[1].split('\n')

graph = {a: (b, c) for a,b,c in map(lambda x: re.findall(r'\w+', x), rest)}

def f(start, crit = lambda x: x != 'ZZZ'):
    cur = start
    i = 0
    while crit(cur):
        cur = graph[cur]['LR'.index( ins[i%len(ins)] )]
        i += 1
    return i

print(f('AAA'))
res2 = 1
for a in graph.keys():
    if a[-1] == 'A':
        res2 = math.lcm(res2, f(a, lambda x: x[-1] != 'Z'))
print(res2)

import re
from collections import defaultdict, deque
XMAS = {k: i for i, k in enumerate('xmas')}

workflows, parts = [b.strip() for b in open('input.txt').read().split('\n\n')]

F = defaultdict(list)

for workflow in workflows.split('\n'):
    match = re.match(r'(\w+){(.*)}', workflow)
    flow, rules = match[1], match[2]
    for r in rules.split(','):
        if '>' in r or '<' in r:
            m = re.match(r'(\w)([<>])(\d+):(\w+)', r)
            part, op, num, go = m[1], m[2], m[3], m[4]

            # LAMBDA CAPTURES, use default variable | joever i didn't include things for p2
            if op == '>': F[flow].append( (lambda x, part=part, num=num, go=go: x[XMAS[part]] > int(num), go, part, op, int(num)) )
            else: F[flow].append( (lambda x, part=part, num=num, go=go: x[XMAS[part]] < int(num), go, part, op, int(num)) )
        else:
            F[flow].append((lambda _, r=r: True, r, None))

def valid(t):
    status = 'in'
    while status not in 'AR':
        for lamb, go, *_ in F[status]:
            if lamb(t):
                status = go
                break
    return status == 'A'

r1 = 0
for ps in parts.split('\n'):
    nums = re.findall(r'\d+', ps)
    t = tuple(map(int, nums))
    if valid(t):
        r1 += sum(t)
print(r1)

def new_range(op, n, l, r):
    match op:
        case '>': l = max(l, n + 1)
        case '>=': l = max(l, n)
        case '<': r = min(r, n - 1)
        case '<=': r = min(r, n)
    return (l, r)

def splits(part, op, n, xl, xr, ml, mr, al, ar, sl, sr):
    match part:
        case 'x': xl, xr = new_range(op, n, xl, xr)
        case 'm': ml, mr = new_range(op, n, ml, mr)
        case 'a': al, ar = new_range(op, n, al, ar)
        case 's': sl, sr = new_range(op, n, sl, sr)
    return (xl, xr, ml, mr, al, ar, sl, sr)

r2 = 0
Q = deque([ ('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000) ])
while Q:
    state, xl, xr, ml, mr, al, ar, sl, sr = Q.popleft()
    if state == 'R' or any([ xr < xl, mr < ml, ar < al, sr < sl ]): continue
    if state == 'A':
        r2 += (xr-xl+1) * (mr-ml+1) * (ar-al+1) * (sr-sl+1)
        continue
    for edge in F[state]:
        match edge:
            case l, go, part, op, num:
                Q.append( (go, *splits(part, op, num, xl, xr, ml, mr, al, ar, sl, sr)) )
                xl, xr, ml, mr, al, ar, sl, sr = splits(part, '>=' if op == '<' else '<=', num, xl, xr, ml, mr, al, ar, sl, sr)
            case l, go, _:
                Q.append( (go, xl, xr, ml, mr, al, ar, sl, sr) )
print(r2)

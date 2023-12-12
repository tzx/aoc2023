import re
import itertools

# From Python docs, I don't have 3.12 on this computer :sob:
def batched(iterable, n):
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch

blocks = [b.strip() for b in open('input.txt').read().split('\n\n')]
seeds = [int(x) for x in re.findall(r'\d+', blocks[0])]

mappings = []
for mstr in blocks[1:]:
    mapping = list( batched(map(int, re.findall(r'\d+', mstr)), 3) )
    assert all(len(b) == 3 for b in mapping)
    mappings.append(sorted([(src, src + leng, dst-src) for dst, src, leng in mapping ]))

def mmap(mapping, ranges):
    res = []
    for st_, ed in ranges:
        st = st_
        for s, d, r in mapping:
            # Before translation
            res.append( (st, min(s, ed)) )
            # Translation, if not in range a >= b
            res.append( (max(s,st)+r, min(d,ed)+r) )
            st = max(st, min(d, ed))
        # After translation
        res.append( (st, ed) )
    return [(a, b) for a, b in res if a < b]

def f(ranges):
    for mapping in mappings:
        ranges = mmap(mapping, ranges)
    return min(a for a,_ in ranges)

print(f([(s, s+1) for s in seeds]))
print(f([ (x, x + y) for x,y in zip(seeds[::2], seeds[1::2])]))

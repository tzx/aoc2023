import re

lines = [li.strip() for li in open('input.txt')]
ts1 = map(int, re.findall(r'\d+', lines[0]))
ds1 = map(int, re.findall(r'\d+', lines[1]))
ts2 = int(''.join(re.findall(r'\d+', lines[0])))
ds2 = int(''.join(re.findall(r'\d+', lines[1])))

def f(ts, ds):
    res1 = 1
    for t, d in zip(ts, ds):
        cnt = 0
        for tp in range(t):
            if (t - tp) * tp > d:
                cnt += 1
        res1 *= cnt
    return res1

print(f(ts1, ds1))
print(f([ts2], [ds2]))

lines = [list(map(int, li.split())) for li in open('input.txt')]

def f(l):
    if all(x == 0 for x in l):
        return 0
    after = [b - a for a, b in zip(l, l[1:])]
    return l[-1] + f(after)

res1 = sum( f(x) for x in lines )
res2 = sum( f(x[::-1]) for x in lines )
print(res1)
print(res2)

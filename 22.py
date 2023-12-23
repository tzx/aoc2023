import re
from itertools import product

ll = [map(int, re.findall('\d+', l.strip())) for l in open('input.txt')]
N = len(ll)
bricks = sorted([((a,b,c),(d,e,f)) for a,b,c,d,e,f in ll],
                key=lambda x: (x[0][2], x[1][2]))

sup, fallen = {}, {}
for i, ((x1,y1,z1), (x2,y2,z2)) in enumerate(bricks):
    def germs(zp):
        touch = set()
        if z1 - zp < 1 or z2 - zp < 1:
            touch.add(-1)

        for (x,y,z) in product(range(x1,x2+1), range(y1,y2+1), range(z1-zp, z2+1-zp)):
            if (x,y,z) in fallen:
                touch.add(fallen[x,y,z])
        return touch

    zp = 0 # min
    while not (touch := germs(zp + 1)):
        zp += 1
    sup[i] = touch
    for (x,y,z) in product(range(x1,x2+1), range(y1,y2+1), range(z1-zp, z2+1-zp)):
        fallen[x,y,z] = i

bad = set()
for v in filter(lambda x: len(x) == 1, sup.values()):
    bad |= v
print(N - len(bad) + 1) # -1 is not brick

gravity = {}
for i in range(N):
    fall = {i}
    for j in range(i+1, N):
        if len(sup[j] - fall) == 0:
            fall.add(j)
    gravity[i] = len(fall) - 1

print(sum(gravity.values()))

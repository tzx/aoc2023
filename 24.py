import re
# from cvc5.pythonic import *
from z3 import *
from itertools import combinations

stones = [list(map(int, re.findall('-?\d+', l.strip()))) for l in open('input.txt')]
N = len(stones)

MIN = 200000000000000
MAX = 400000000000000

r1 = 0

for i, j in combinations(range(N), 2):
    a,b,_,da,db,_ = stones[i]
    x,y,_,dx,dy,_ = stones[j]
    S = Solver()

    t1, t2 = Reals('t1 t2')

    S.add(t1 >= 0)
    S.add(t2 >= 0)

    S.add(a + da * t1 == x + dx * t2)
    S.add(b + db * t1 == y + dy * t2)
    S.add(x + dx * t2 >= MIN)
    S.add(y + dy * t2 >= MIN)
    S.add(x + dx * t2 <= MAX)
    S.add(y + dy * t2 <= MAX)
    r1 +=  S.check() == sat
print(r1)

s = Solver()
X, Y, Z, DX, DY, DZ = [Real(v) for v in 'X Y Z DX DY DZ'.split()]
for i, (x,y,z,dx,dy,dz) in enumerate(stones):
    if i == 4: 
        break
    t = Real(f't{i}')
    s.add(t > 0)
    s.add(x + dx * t == X + DX * t)
    s.add(y + dy * t == Y + DY * t)
    s.add(z + dz * t == Z + DZ * t)

print('aa')
if s.check() == sat:
    m = s.model()
    print(eval( str(sum( [m.eval(X), m.eval(Y), m.eval(Z)] ))))

# P + tU = Q + tV
# => P-Q = t(V-U)
# too lazy

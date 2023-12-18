import re
ll = [l.strip() for l in open('input.txt')]

RDLU = 'RDLU'
dirs = {
    'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)
}

def f(steps):
    xs, ys = [0], [0]
    for dire, dist in steps:
        # dire, dist, color = re.findall(r'\w+', l)
        dy, dx = (dist * i for i in dirs[dire])
        nx, ny = xs[-1] + dx, ys[-1] + dy
        xs.append(nx)
        ys.append(ny)
    N = len(xs)
    xs.append(0); ys.append(0)

    P = sum( abs((ys[i+1] - ys[i]) + (xs[i+1] - xs[i])) for i in range(N) )
    A = 0.5 * sum( (ys[i] + ys[i+1]) * (xs[i] - xs[i+1]) for i in range(N) )

    # A = I + P/2 - 1
    # I = A - P/2 + 1
    # I + P = A + P/2 + 1
    return A + P//2 + 1


print(f( [ (dire, int(dist)) for dire, dist, _ in map(lambda x: re.findall(r'\w+', x), ll)] ) )
print(f( [ (RDLU[int(col[-1])], int(col[:-1], 16)) for _, _, col in map(lambda x: re.findall(r'\w+', x), ll)] ) )

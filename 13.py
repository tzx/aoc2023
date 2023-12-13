ll = [li.split() for li in open('input.txt').read().split('\n\n')]

def diff_hor(bl, i):
    amt_check = min(i, len(bl) - i)
    return sum(bl[i+k][j] != bl[i-k-1][j] for k in range(amt_check) for j in range(len(bl[0])))

def diff_ver(bl, j):
    trans = list(zip(*bl))
    return diff_hor(trans, j)

def f(dx = 0):
    ans = 0
    for bl in ll:
        for i in range(1, len(bl)):
            if diff_hor(bl, i) == dx:
                ans += 100 * i
        for j in range(1, len(bl[0])):
            if diff_ver(bl, j) == dx:
                ans += j
    return ans

print(f())
print(f(1))

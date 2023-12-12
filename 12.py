lines = [li.strip() for li in open('input.txt')]
res1 = res2 = 0

def r(row_idx, dmg_idx, row, dmgs, build, memo):
    key = (row_idx, dmg_idx, build)
    if key in memo:
        return memo[key]
    
    if row_idx == len(row):
        if build == 0 and dmg_idx == len(dmgs):
            return 1
        if dmg_idx == len(dmgs) - 1 and build == dmgs[-1]:
            return 1
        return 0
    
    ans = 0
    c = row[row_idx]
    if c in '.?' and build == 0:
        ans += r(row_idx + 1, dmg_idx, row, dmgs, build, memo)
    if c in '.?' and build > 0 and dmg_idx in range(len(dmgs)) and dmgs[dmg_idx] == build:
        ans += r(row_idx + 1, dmg_idx + 1, row, dmgs, 0, memo)
    if c in '#?':
        ans += r(row_idx + 1, dmg_idx, row, dmgs, build + 1, memo)

    memo[key] = ans
    return ans


for li in lines:
    row, damage = li.split()
    damages = list(map(int, damage.split(',')))

    res1 += r(0, 0, row, damages, 0, dict())
    res2 += r(0, 0, '#'.join([row] * 5), damages * 5, 0, dict())

print(res1)
print(res2)

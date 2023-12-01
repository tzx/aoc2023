import re

lines = [li.strip() for li in open('input.txt')]

ihateyou = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def f(non, greed):
    res = 0
    for l in lines:
        first = re.search(non, l)
        if not first:
            continue
        st = ihateyou.get(first.group(1), first.group(1))
        last = re.search(greed, l)
        st += ihateyou.get(last.group(1), last.group(1))
        res += int(st)
    return res

print( f(r'.*?([0-9])', r'.*([0-9])') )

words = "|".join(ihateyou.keys())
word_reg = r'{}'.format(words)
regnon = r'.*?([0-9]|' + word_reg + r')'
regreed = r'.*([0-9]|' + word_reg + r')'

print( f(regnon, regreed) )

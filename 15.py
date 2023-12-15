import re

l = open('input.txt').read()

def hash(st):
    cur_v = 0
    for ch in st:
        cur_v += ord(ch)
        cur_v *= 17
        cur_v = cur_v % 256
    return cur_v

boxes = [[] for _ in range(256)]
lengths = {}
r1 = r2 = 0

for st in l.split(','):
    r1 += hash(st)

    words = re.findall(r'\w+', st)
    match words:
        case label, amt:
            h = hash(label)
            if label not in boxes[h]: boxes[h].append(label)
            lengths[label] = int(amt)
        case label, *_:
            h = hash(label)
            if label in boxes[h]: boxes[h].remove(label)

for i, box in enumerate(boxes, 1):
    r2 += sum(i * j * lengths[label] for j, label in enumerate(box, 1))

print(r1)
print(r2)

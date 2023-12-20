from collections import defaultdict, deque, Counter
import math

ll = [l.strip() for l in open('input.txt')]

nexts = defaultdict(list)
conj, flip = {}, {}
rx_connect_press = {}

for l in ll:
    module, outputs = l.split(' -> ')
    outputs = outputs.split(', ')

    if module == "broadcaster":
        nexts[module] = outputs
        continue

    pre, module = module[0], module[1:]
    nexts[module] = outputs

    if 'rx' in outputs:
        rx_connect = module
    if pre == '&':
        conj[module] = {}
    if pre == '%':
        flip[module] = False

for mod, outputs in nexts.items():
    for neigh in outputs:
        if neigh in conj:
            conj[neigh][mod] = False

p_cntr = Counter()
def press():
    p_cntr[False] += 1
    Q = deque([ (None, "button", "broadcaster") ])
    while Q:
        pulse, src, to = Q.popleft()
        if to == "rx": continue
        if to == "broadcaster":
            p_cntr[False] += len(nexts[to])
            for dest in nexts[to]:
                Q.append( (False, to, dest) )
            continue
        
        new_pulse = False
        if to in conj:
            conj[to][src] = pulse
            new_pulse = any(not p for p in conj[to].values())

        if to in flip:
            if pulse: continue
            flip[to] = not flip[to]
            new_pulse = flip[to]

        p_cntr[new_pulse] += len(nexts[to])

        for neigh in nexts[to]:
            Q.append( (new_pulse, to, neigh) )

        for to, pulse in conj[rx_connect].items():
            if pulse and to not in rx_connect_press:
                global presses
                rx_connect_press[to] = presses

presses = 0
conj_rx_cnt = sum(1 for src, tos in nexts.items() if rx_connect in tos)

# Low -> False, High -> True
for _ in range(1000):
    presses += 1
    press()
print(p_cntr[False] * p_cntr[True])

while len(rx_connect_press) < conj_rx_cnt:
    presses += 1
    press()
print(math.lcm(*rx_connect_press.values()))

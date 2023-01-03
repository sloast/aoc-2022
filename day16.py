import time
nodes = {}

for l in open('16.test'):
    words = l.split()
    nodes[words[1]] = (int(words[4][5:-1]),{x[:2]:1 for x in words[9:]})


for k in [*nodes.keys()]:
    if k in nodes:
        f, e = nodes[k]
        if f == 0 and len(e) == 2:
            n = [*e.items()]
            n1, n2 = n[0][0], n[1][0]
            e1 = nodes[n1][1]
            e2 = nodes[n2][1]
            weight = e1[k] + e2[k]
            e1[n2] = weight
            e2[n1] = weight
            e1.pop(k)
            e2.pop(k)
            nodes.pop(k)

for k, v in nodes.items():
    print (k, ':', v)

best = 0

def go(k, prev):
    print(k)
    for c in nodes[k][1].keys():
        if c != prev:
            go(c, k)


opened_init = {k:False for k in nodes.keys()}
#go('AA', '')
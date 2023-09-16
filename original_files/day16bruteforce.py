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

def go(k, t, dt, pps, score, opened):
    global best
    
    for _ in range(dt):
        score += pps
        t += 1
        if t>=30:
            if score > best:
                best = score
                print(best)
            return
    if (not opened[k]) and nodes[k][0] > 0:
        opened[k] = True
        go(k, t, 1, pps+nodes[k][0], score, opened.copy())
    # print(sorted([(m, nodes[m]) for m in nodes[k][1].keys()], key=lambda x:-x[1][0]))
    else: 
        for n in sorted([(m, nodes[m]) for m in nodes[k][1].keys()], key=lambda x:-x[1][0] if not opened[x[0]] else 0):
            go(n[0], t, n[1][1][k], pps, score, opened.copy())
    return


opened_init = {k:False for k in nodes.keys()}
go('AA', 0, 1, 0, 0, opened_init)
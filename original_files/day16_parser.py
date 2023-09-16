import time
nodes = {}

for l in open('16'):
    words = l.split()
    nodes[words[1]] = (int(words[4][5:-1]),{x[:2]:1 for x in words[9:]})

#for i, (k, v) in enumerate(nodes.items()):
#    print (i, ':', k, ':', v)
    
s = '{'
arr = sorted(nodes.keys())

print(arr)



for k in arr:
    s += str(nodes[k][0]) + ','
print(s[:-1] + '}')

s = '{'
for k in arr:
    cs = '{'
    for val in nodes[k][1].keys():
        cs+= str(arr.index(val)) + ','
    s += cs[:-1]+'}'+','
print(s[:-1]+'}')
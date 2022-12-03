import re
f = map(str.strip, open('3', 'r').readlines())
f = map(lambda s: [s[:len(s)//2], s[len(s)//2:]], f)
total = 0
f = map(lambda x: re.search('|'.join(x[0]), x[1]).group(), f)
print(sum('_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) for c in f))

g = list(map(str.strip, (open('3'))))
print(sum('_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) for c in [re.search('|'.join(re.findall('|'.join(g[i]), g[i+1])), g[i+2]).group() for i in range(0, len(g), 3)]))

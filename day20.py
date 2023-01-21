class num:
    def __init__ (self, x):
        self.x = int(x)

f = [num(l) for l in open('20-k')]
g = f.copy()
tmp = num(0)

def get_coords():
    a = [c.x for c in g]
    inxarr=[*map(lambda x:(a.index(0)+x)%len(a), [1000,2000,3000])]
    for i, b in enumerate(map(lambda i:a[i],inxarr)):
        print(f'{[1000,2000,3000][i]}: {b}')
    return sum(map(lambda i:a[i],inxarr))

def mix():
    for c in f:
        inx = (g.index(c) + c.x) % (len(g)-1)
        g.remove(c)
        g.insert(inx, c)

# PART 1:
mix()
print("Part 1:", get_coords(),'\n')

# PART 2:
g = f.copy()
DECRYPTION_KEY = 811589153
for c in g:c.x *= DECRYPTION_KEY

for _ in range(10):
    mix()
print("Part 2:",get_coords(),'\n')

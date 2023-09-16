rows = [[*map(int, l.strip())] for l in open('8').readlines()]
rows.extend(list(map(list, zip(*rows))))
vis = [[0 for _ in r] for r in rows]

for k,r in enumerate(rows):
    h=-1
    for i,x in enumerate(r):
        if x>h: h=x;vis[k][i]=1
    h=-1
    for i,x in enumerate(reversed(r)):
        if x>h: h=x;vis[k][len(r)-i-1]=1
l = len(vis[0])      
count = 0
for x in range(l):
    for y in range(l):
        if vis[x][y] or vis[y+l][x]:
            count += 1

print(count)
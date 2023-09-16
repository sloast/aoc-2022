from collections import deque


coords = set([(int(l.split(',')[0]),int(l.split(',')[1]),int(l.split(',')[2])) for l in open('18')])
sides = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
score = 0
for c in coords:
    for diff in sides:
        score += 0 if tuple(map(lambda a,b: a+b, c, diff)) in coords else 1
print("\nPart 1:",score)

def neighbours(x):
    nbs, scr = [], 0
    for diff in sides:
        d = tuple(map(lambda a,b: a+b, x, diff))
        if (min(d) >= -1 and max(d) < 25):
            if d in coords:
                scr += 1
            else:
                nbs.append(d)
    return scr, nbs

score = 0

q = deque(((0, 0, 0),))
exclude = set(q)
while len(q) > 0:
    c = q.popleft()
    s, nbs = neighbours(c)
    for n in nbs:
        if n not in exclude:
            q.append(n)
            exclude.add(n)
    score += s
    
print("\nPart 2:",score,'\n')

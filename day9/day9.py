lines = open('9').readlines()
steps = []
for l in lines:
    for j in range(int(l.strip()[2:])):
        steps.append(l[0])


# for part 1
grid1 = [[0 for _ in range(len(steps)*2)] for _ in range(len(steps)*2)]
grid1[len(steps)][len(steps)] = 1

# for part 2
grid2 = [[0 for _ in range(len(steps)*2)] for _ in range(len(steps)*2)]
grid2[len(steps)][len(steps)] = 1

x = [0 for _ in range(10)]
y = [0 for _ in range(10)]

for s in steps:
    if s == 'R':
        x[0]+=1
    elif s=='L':
        x[0]-=1
    elif s=='U':
        y[0]+=1
    elif s=='D':
        y[0]-=1
    #print('H', x[0], y[0])
    for i in range(1,10):
        dx = x[i-1]-x[i]
        dy = y[i-1]-y[i]
        if max(abs(dx), abs(dy)) > 1:
            x[i] += dx//abs(dx) if abs(dx)>0 else 0
            y[i] += dy//abs(dy) if abs(dy)>0 else 0
            #print(i,x[i],y[i])
    # part 1
    grid1[x[1]+len(steps)][y[1]+len(steps)] = 1
    # part 2
    grid2[x[9]+len(steps)][y[9]+len(steps)] = 1
            

print("Part 1:", sum(sum(r) for r in grid1))
print("Part 2:", sum(sum(r) for r in grid2))
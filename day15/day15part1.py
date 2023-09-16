import re
arr = [[*map(int,re.findall('-?[0-9]+', l))] for l in open('15')]
size = max(max(l)for l in arr)*2

def dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

beacons = {}
sensors = []
i=0

for xs,ys,xb,yb in arr:
    beacons[xb, yb] = True
    sensors.append((xs, ys, dist(xs, ys, xb, yb)))
    
count = 0
rownum = 2000000
for i in range(-size, size):
    if i % (size//50) == 0:
        print(f'{round((i+size)/(size*2)*100)+1}%')
    for x,y,d in sensors:
        if dist(x,y,i,rownum) <= d and (i, rownum) not in beacons:
            count += 1
            break
        
print("Part 1:",count)
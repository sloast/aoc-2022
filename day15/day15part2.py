import re
arr = [[*map(int,re.findall('-?[0-9]+', l))] for l in open('15')]
size = 4000000

def dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

beacons = {}
sensors = []

for xs,ys,xb,yb in arr:
    beacons[xb, yb] = True
    sensors.append((xs, ys, dist(xs, ys, xb, yb)))

for n, (sx, sy, d) in enumerate(sensors):
    print(f'Sensor {n+1}')
    for i in range(d+1):
        for x,y in ((sx+i, sy+(d+1-i)), (sx-i, sy-(d+1-i)), (sx+i, sy-(d+1-i)), (sx-i, sy+d)):
            if (0<=x<=size and 0<=y<=size):
                flag = True
                for sx2,sy2,d2 in sensors:
                    if dist(x,y,sx2,sy2) <= d2:
                        flag = False
                        break
                if flag:
                    print("Found!")
                    print(x, y)
                    print((x*4000000+y))
                    exit()

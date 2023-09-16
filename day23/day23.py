from collections import deque
from time import time

time1=time2=time3=0
s = set()
proposed = {}
freqs = {}
order = deque()
def read():
    global order
    s.clear()
    order = deque([0,1,2,3])
    proposed.clear()
    for y, line in enumerate(open('23')):
        for x, c in enumerate(line):
            if c == '#':
                s.add((x, y))

directions = [(0,-1),(0, 1),(-1, 0),(1, 0)]
sides = [(0,-1),(-1,-1),(1,-1),(0,1),(-1,1),(1,1),(-1,0),(1,0)]

def add(a, b):
    return a[0]+b[0],a[1]+b[1]

def blocked(a, b):
    result = int(add(a,b) in s)
    if b[0] == 0:
        #result += add(a,( 1,b[1])) in s
        #result += add(a,(-1,b[1])) in s
        result += len(set([add(a,( 1,b[1])),add(a,(-1,b[1]))])&s)
    elif b[1] == 0:
        result += add(a,(b[0], 1)) in s
        result += add(a,(b[0],-1)) in s
    return bool(result)

def getrect():
    xs,ys=zip(*s)
    return (min(xs),min(ys)),(max(xs)+1,max(ys)+1)

def printout():
    (minx,miny),(maxx,maxy)=getrect()
    for i in range(miny,maxy):
        print(''.join(['#' if (j,i) in s else '.' for j in range(minx,maxx)]))
    print()

def move():
    #global time1,time2,time3
    for elf in s:
        neighbours = False
        #start = time()
        for d in sides:
            if add(elf, d) in s:
                neighbours = True
                break
        #time1 += time() - start
        #start = time()
        if neighbours:
            for o in order:
                if not blocked(elf, directions[o]):
                    newpos = add(elf,directions[o])
                    proposed[elf] = newpos
                    freqs[newpos] = freqs[newpos] + 1 if newpos in freqs else 1
                    break
        #time2+=time()-start
    #start = time()
    result = len(proposed)
    for elfpos,newpos in proposed.items():
        if freqs[newpos] == 1:
            s.remove(elfpos)
            s.add(newpos)
    proposed.clear()
    freqs.clear()
    order.append(order.popleft())
    #time3+=time()-start
    #print(result)
    return result
    

# Part 1
read()

for t in range(10):
    move()

#printout()
(ax,ay),(bx,by)=getrect()
print("\nPart 1:",sum(sum(1-int((j,i)in s)for j in range(ax,bx))for i in range(ay,by)))


# Part 2
read()
count = 1
while m:=move():
    count+=1
    #print("Proposed:",m)
print("Part 2: ",count,'\n')

#print(time1,time2,time3)
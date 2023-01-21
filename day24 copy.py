import math
import queue

class node:
    def __init__(self, x, y, t = 0):
        self.x, self.y = x, y
        self.t = t
        self.prev = None
        self.g = float('inf')
        self.f = float('inf')
        self.h = 0
        
    def __lt__(self, other):
        return self.f < other.f
    
    def __sub__ (self, other):
        return abs(self.x-other.x)+abs(self.y-other.y)
    
    def __str__(self):
        return f'x={self.x}, y={self.y}, h={self.h}'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y, self.t))


f = open('24').readlines()
print(len(f[0])-2, len(f)-2)
print(math.lcm(len(f[0])-2, len(f)-2))
directionSymbols = '>v<^'
directions = [(1, 0),(0, 1),(-1,0),(0,-1)]
blizzards = [{}]
history = []
ymax=xmax= 0
for y,line in enumerate(f[1:-1]):
    ymax=y+1
    for x,c in enumerate(line.strip()[1:-1]):
        xmax=x+1
        if c in directionSymbols:
            blizzards[0][(x, y)] = [directionSymbols.index(c)]
        else:
            assert c == '.'

startpos = (0, -1)
endpos = (xmax-1, ymax)
goal = node(xmax-1, ymax)
start = node(*startpos)
print(blizzards)
history.append(len(blizzards[0]))
t = 0

def printout():
    w = len(blizzards)-1
    print()
    for i in range(ymax):
        print(''.join([(directionSymbols[blizzards[w][(j,i)][0]] if (j,i) in blizzards[w] and len(blizzards[w][(j,i)]) == 1 else str(len(blizzards[w][(j,i)]))) if (j,i) in blizzards[w] and len(blizzards[w][(j,i)])>0 else '.' for j in range(xmax)]))
        
def h(a):
    return goal-a

def get_neighbors(n, t):
    a = []
    x,y=n.x,n.y
    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x,y)]:
        if ((nx,ny) not in blizzards[t] and 0 <= nx < xmax and 0 <= ny < ymax) or (nx==endpos[0] and ny==endpos[1]) or (0==nx and -1==ny):
            a.append(node(nx,ny))
    return a

def move_blizzards(t, replace=False):
    global blizzards
    nd = {}
    for (x,y),dls in blizzards[t].items():
        for d in dls:
            #print(x,y,d)
            dx,dy = directions[d]
            nx,ny = (x+dx)%xmax,(y+dy)%ymax
            if (nx,ny) in nd:
                nd[nx,ny].append(d)
            else:
                nd[nx,ny] = [d]
    if replace:
        blizzards[t] = nd
    else:
        blizzards.append(nd)
    #printout()
    #print(t)
            

q = queue.PriorityQueue()
q.put(start)
start.h=0
start.f=h(start)
start.g=0
goal.f=h(start)
seen = set((start,))
t = 0
start.t
move_blizzards(0,replace=True)

move_blizzards(0)
while not q.empty():
    
    n=q.get()
    if n.t >= len(blizzards)-1:
        move_blizzards(n.t)
        #print(n.t)
    t = n.t
    #print(t)
    for p in get_neighbors(n, n.t):
        
        p.t = n.t+1
        if p in seen:
            continue
        p.g = p.t
        p.f = h(p) + p.g
        p.h = h(p)
        p.prev = n
        q.put(p)
        seen.add(p)
        if p == goal:
            print(p.t)
            c = p
            while c is not None:
                print(c)
                c = c.prev
            print()
            print("Part 1: ",p.t)
            quit()

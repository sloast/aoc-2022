import queue

class node:
    def __init__(self, x, y):
        self.x, self.y = x, y
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

lines=[*map(str.strip,open('12').readlines())]
charset=sorted(list(set(''.join(lines))-set('SE\n')))
goal=node(0,0)
start:node=node(0,0)
hmap=[[]for _ in lines]
for i,l in enumerate(lines):
    for j,c in enumerate(l):
        n = node(i,j)
        if c == 'S':
            start=n
            n.h=0
        elif c == 'E':
            goal=n
            n.h=len(charset)-1
        else:
            n.h = charset.index(c)
        hmap[i].append(n)

def h(a):
    return goal-a

def get_neighbors(n):
    a = []
    x,y=n.x,n.y
    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if min(nx,ny)>=0 and nx<len(hmap) and ny<len(hmap[0]):
            if (hmap[nx][ny].h - n.h <=1):
                a.append(hmap[nx][ny])
    return a

q = queue.PriorityQueue()
q.put(start)
start.f=h(start)
start.g=0
s = [[' 'for _ in l] for l in hmap]
def found(n):
    print(n)
    
    i=-1
    while n is not None:
        s[n.x][n.y] = charset[n.h]
        t = n
        n = n.prev
        i+=1
    s[start.x][start.y]='S'
    s[goal.x][goal.y]='E'
    print('\n'.join(map(''.join,s)))
    print(f'length: {i}')
    

# part 1
while not q.empty():
    n=q.get()
    s[n.x][n.y] = '.'
    if n==goal:
        found(n)
        break
    for p in get_neighbors(n):
        t=n.g+1
        if t<p.g:
            p.prev = n
            p.g=t
            p.f=t+h(p)
            q.put(p)
g = [['.' for _ in range(200)] for _ in range(200)]
# b = [[False for _ in range(200)] for _ in range(200)]
lowest = 0
def prt():
    for r in zip(*(str(i) if i % 5 == 0 else '   ' for i in range(400,600))):
        print('    '+''.join(r))
    for i,l in enumerate(g[:lowest+1]):
        i = str(i)
        print(' '*(3-len(i)) + i , ''.join(l))

def sgt(x,y,a=None):
    if a is None:
        return g[y][x-400]
    g[y][x-400] = a

for l in map(lambda l:map(lambda x:map(int,x.strip().split(',')),l.split('->')), open('14')):
    ta=tb=-1
    for a,b in l:
        if ta!=-1:
            if ta==a:
                for i in range(min(tb,b),max(tb,tb:=b)+1):
                    sgt(a,i,'#')
                    lowest=max(lowest,i)
            else:
                for i in range(min(ta,a),max(ta,ta:=a)+1):
                    sgt(i,b,'#')
                lowest=max(lowest,b)
        else:
            ta,tb=a,b
i=0
while True:
    x,y=500,0
    flg = True
    while y<lowest:
        if sgt(x,y+1)=='.':
            y+=1
        elif sgt(x-1,y+1)=='.':
            x-=1
            y+=1
        elif sgt(x+1,y+1)=='.':
            x+=1
            y+=1
        else:
            flg=False
            break
    if flg:
        break
    sgt(x,y,'o')
    i+=1
sgt(500,0,'+')
prt()
print("Part 1:",i)
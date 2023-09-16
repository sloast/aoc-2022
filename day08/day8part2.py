rows = [[*map(int, l.strip())] for l in open('8').readlines()]

def tall(x,y,h):
    if min(x,y)<=0 or max(x,y)>=len(rows)-1:return True
    return rows[x][y]>=h

maxs = 0
for x in range(len(rows)):
    for y in range(len(rows)):
        nx,ny=x,y
        h=rows[x][y]
        s0=s1=s2=s3=0
        t=0
        while not t:
            if x==len(rows):break
            nx+=1
            s0+=1
            t=tall(nx,y,h)
        nx,t=x,0
        while not t:
            if x==0:break
            nx-=1
            s1+=1
            t=tall(nx,y,h)
        t=0
        while not t:
            if y==len(rows):break
            ny+=1
            s2+=1
            t=tall(x,ny,h)
        ny,t=y,0
        while not t:
            if y==0:break
            ny-=1
            s3+=1
            t=tall(x,ny,h)
        s=s0*s1*s2*s3
        if s>maxs:maxs=s
            
print(maxs)
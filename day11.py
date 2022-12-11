import math
z=[l.split('\n')for l in open("11").read().split('\n\n')]
l=[0 for _ in z]
q=[[int(m[0][7:-1]),0 if m[2][25:]=='old'else int(m[2][25:]),m[2][23]=='*',int(m[3][21:]),int(m[4][29:]),int(m[5][30:])]for m in z]
d=math.lcm(*map(lambda m:m[3],q))
s=[[*map(int,m[1].split(':')[1].split(','))]for m in z] # type: ignore
p=[*zip(s,q)]
for t in range(10000):
    for b,m in p:
        for o in b:
            l[m[0]]+=1
            y=m[1]if m[1]else o
            o=(o*y if m[2]else o+y)%d
            s[m[4]].append(o)if o%m[3]==0 else s[m[5]].append(o)
        b.clear()
x=sorted(l)
print(x[-1]*x[-2])
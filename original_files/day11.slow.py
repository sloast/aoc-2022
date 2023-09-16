# z=[*zip(*(map(str.strip,open("11")),)*7)]
import math
z=[l.split('\n')for l in open("11").read().split('\n\n')]
s,l=[],{m[0]:0 for m in z}
d=math.lcm(*map(lambda m:int(m[3][21:]),z))
for m in z:
    s.append([*map(int,m[1].split(':')[1].split(','))]) # type: ignore
for t in range(10000):
    for b,m in zip(s,z):
        for i,o in enumerate(b):
            l[m[0]]+=1
            y=o if m[2][25:]=='old'else int(m[2][25:])
            o=(o*y if m[2][23]=='*'else o+y)%d
            s[int(m[4][29:])].append(o)if o%int(m[3][21:])==0 else s[int(m[5][30:])].append(o)
        b.clear()
x=sorted(l.values())
print(x[-1]*x[-2])
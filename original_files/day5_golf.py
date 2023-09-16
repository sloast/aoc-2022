# part 1
m=[];a,b=open('5').read().split('\n'*2)
for c in list(zip(*[l.split()for l in(' '+a.replace('\n','\n ')).replace(' '*4,' -').split('\n')])):m.append([*reversed([*map(lambda x:x[1],filter(lambda y:len(y)>2,c))])])
for l in b.split('\nm'):a,b,c=map(int,l.split()[1::2]);t=[];[t.append(m[b-1].pop())if m[b-1]else[]for i in range(a)];m[c-1].extend(t)
print(''.join([n[-1]for n in m]))

# part 2
m=[];a,b=open('5').read().split('\n'*2)
for c in list(zip(*[l.split()for l in(' '+a.replace('\n','\n ')).replace(' '*4,' -').split('\n')])):m.append([*reversed([*map(lambda x:x[1],filter(lambda y:len(y)>2,c))])])
for l in b.split('\nm'):a,b,c=map(int,l.split()[1::2]);t=[];[t.insert(0,m[b-1].pop())if m[b-1]else[]for i in range(a)];m[c-1].extend(t)
print(''.join([n[-1]for n in m]))
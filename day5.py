arr=[]
a, b = open('5').read().split('\n\n')
a = (' ' + a.replace('\n', '\n ')).replace('    ', ' -')
for c in list(zip(*[l.split() for l in a.split('\n')])):
    arr.append(list(reversed(list(map(lambda x:x[1], filter(lambda y:len(y)>2,c))))))

#for l in b.split('\nm'):
#    l = [*map(int,l.split(' ')[1::2])]
#    for i in range(l[0]):
#        if arr[l[1]-1]:
#            arr[l[2]-1].append(arr[l[1]-1].pop())

for l in b.split('\nm'):
    l = [*map(int,l.split(' ')[1::2])]
    tmp = []
    for i in range(l[0]):
        if arr[l[1]-1]:
            tmp.append(arr[l[1]-1].pop())
    arr[l[2]-1].extend(reversed(tmp))

outputarr = []
left = True
for i in range(max(map(len,arr))):
    outputarr.append(' '.join(j[i] if len(j)>i else ' ' for j in arr))
print('\n'.join(reversed(outputarr)))
print(' '.join(str(i+1) for i in range(len(arr))))
print()

print(''.join([a.pop() for a in arr]))

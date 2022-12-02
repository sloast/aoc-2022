print(sum(map(lambda a:a[1]-2+(a[1]-a[0]+1)%3*3,map(lambda l:list(map('ABCXYZ'.index,l[::2])),open('2')))))

print(sum(map(lambda a:a[1]*3+(a[0]+a[1]-1)%3-8,map(lambda l:list(map('ABCXYZ'.index,l[::2])),open('2')))))

print(sum(map(lambda a,b:b-2+(b-a+1)%3*3,*zip(*map(lambda l:map('ABCXYZ'.index,l[::2]),open('2'))))))

print(sum(map(lambda a,b:b*3+(a+b-1)%3-8,*zip(*map(lambda l:map('ABCXYZ'.index,l[::2]),open('2'))))))

print(sum(b-87+(b-a-1)%3*3 for a,b in map(lambda l:map(ord,l[::2]),open('2'))))

print(sum(b*3+(a+b-1)%3-263 for a,b in map(lambda l:map(ord,l[::2]),open('2'))))

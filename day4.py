f = open('4')
f = list(map(lambda x: list(map(lambda y: list(map(int, y.split('-'))),(x[:-1]).split(','))), f))

# part 1
count = 0
for i in f:
    if i[0][0] <= i[1][0] <= i[1][1] <= i[0][1]:
        count += 1
    elif i[1][0] <= i[0][0] <= i[0][1] <= i[1][1]:
        count += 1

print(count)
count=0

# part 2
for i in f:
    if not (i[0][0] > i[1][1] or i[1][0] > i[0][1]):
        count+= 1

print(count)


l=list(list(('0'*(i<10)) + str(i) for i in j) for j in map(lambda l:map(int,'-'.join(l.split(',')).split('-')),open('4')))
print(' '.join(map(lambda x:x[0]+'-'+x[1]+','+x[2]+'-'+x[3],l)))
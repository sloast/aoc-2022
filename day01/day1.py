t, a = 0, []
for l in open('day1.txt', 'r').readlines():
    if l.strip() == '': a.append(t); t = 0
    else: t += int(l)
print(sum(sorted(a)[-3:]))

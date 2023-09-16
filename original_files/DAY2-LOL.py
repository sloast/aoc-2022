out = open('day2.lol', 'w')
inp = list(map(lambda l:list(map('ABCXYZ'.index,l[::2])),open('2')))

for a in 'ABC':
    for b in 'XYZ':
        print('\tOMG "' + a + b + '"')
        print('\t\tME HAS A SRS INDEX ITZ ' + str('XYZ'.index(b) + 3))
        print('\t\tTHEM HAS A SRS INDEX ITZ ' + str('ABC'.index(a)))
        print('\t\tGTFO')
print('\tOIC')
'''
s = '{'
for l in open('18'):
    s += '{' + l[:-1] + '},'
print(s[:-1] + '}')
'''

print(max(max(map(int, l.split(','))) for l in open('18')))
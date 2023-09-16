import re
blueprints = [[*map(int,re.findall('[0-9]+', s))][1:] for s in open('19')]
print(blueprints)

s = '{'
for b in blueprints:
    cs = '{'
    cs += str(b)[1:-1] + '},'
    
    s += cs.replace(' ', '')
print(s[:-1] + '}')
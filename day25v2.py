ls = [['=-012'.index(c)-2 for c in l.strip()] for l in open('25.test')]
digits = []

def sgt(i,x=None):
    if x is None:return digits[i] if i < len(digits) else 0
    if len(digits) == i:
        digits.append(x)
    else:
        digits[i] = x

def add(i,x):
    sgt(i,b:=sgt(i)+x)
    if c:=(b>2)-(b<-2):
        add(i+1, c)
        sgt(i,(b+2)%5-2)


for n in ls:
    for i,c in enumerate(reversed(n)):
        add(i,c)

print('Result:',''.join(['=-012'[x+2] for x in reversed(digits)]))

t,x,o=0,1,0
def f():
    return x*t*(t%40==20)
for c in open('10'):
    t+=1
    o+=f()
    if c[0]=='a':
        t+=1
        o+=f()
        x+=int(c[4:])
print(o)
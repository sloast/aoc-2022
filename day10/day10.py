t=o=0;x,s=2,''
f=lambda:x*t*(t%40==20)
g=lambda:('██'if(x-2<t%40<x+2)else'  ')if(t%40)else'\n'
for c in open('10'):
    t+=1;o+=f();s+=g()
    if c[0]=='a':
        t+=1;o+=f();s+=g()
        x+=int(c[4:])
print(f'Part 1: {o}\nPart 2:\n'+s)
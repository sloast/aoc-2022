def p(s):
    if s[0]=='[':
        if len(s)==2: return []
        inxs,u = [],0
        for i,c in enumerate(s:=s[1:-1]):
            if c == ',' and u == 0:
                inxs.append(i+1)
            elif c=='[':
                u+=1
            elif c==']':
                u-=1
        t = 0
        return[*map(p,[*(s[t:(t:=i)-1] for i in inxs),s[t:]])]
    else:
        return int(s)
    
def f(x,y):
    if type(x) is list:
        if type(y) is not list:
            y = [y]
    if type(y) is list:
        if type(x) is not list:
            x = [x]
        for i in range(max(len(x),len(y))):
            if i == len(x):return 1
            elif i == len(y):return -1
            if (r:=f(x[i],y[i]))!=0:
                return r
        return 0
    return 0 if x==y else 1 if x<y else -1

class pak:
    def __init__(self,c):
        self.content = c
    def __lt__(self,other):
        return f(self.content,other.content)>0
    def __str__(self):
        return str(self.content)


paks=[*map(lambda l: pak(p(l.strip())),filter(lambda l:len(l)>1,open("13"))), d1:=pak([[2]]), d2:=pak([[6]])]
print('\n'.join(map(str,paks:=sorted(paks))))
print((paks.index(d1)+1)*(paks.index(d2)+1))
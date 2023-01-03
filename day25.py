import math

def main():
    z = read("25.test")
    if False:
        print(f"\nVERS1.0: {conv1(z)}")
        print(f"VERS1.5: {conv(z)}")
        print(f"VERS2.0: {conv2(z)}\n")
    else:
        print(f"\nResult: {conv(z)}\n")

#x=sum(map(lambda l:sum(map(lambda a,b:a*b,[5**i for i in range(len(l)-2,-1,-1)],map(lambda c:'=-012'.index(c)-2,l[:-1]))),open('25')))
def read(filename):
    return sum(sum(map(lambda a,b:a*b,[5**i for i in range(len(l)-2,-1,-1)],['=-012'.index(c)-2 for c in l[:-1]]))for l in open(filename))

# VERSION 1 (goes right to left)

def conv1(x):
    s,i='',0
    while x!=0:
        b=pow(5,i);
        n='012=-'[x%(5*b)//b];
        x-=('=-012'.index(n)-2)*b;
        s=n+s;
        i+=1
    return s


# VERSION 1.5 (uses a dict)
def conv(x):
    d = {'=':-2,'-':-1,'0':0,'1':1,'2':2}
    s,i='',0
    while x!=0:
        b=5**i
        n='012=-'[x%(5*b)//b]
        x-=d[n]*b
        s=n+s
        i+=1
    return s


# VERSION 2 (goes left to right)
def conv2(x):
    s=''
    for i in range(math.ceil(math.log(x,5)),0,-1):
        a=[0]*5
        for j in range(5):
            a[j]=((x-(5**(i-1))*(j-2),'=-012'[j]))
        x,c=min(a,key=lambda a:abs(a[0]))
        s+=c
    return s

if __name__ == "__main__":
    main()
f=next(open('6')) # part 1
for i in range(len(f)):
    if len(set(f[i:i+4]))>3:print(i+4);break
    
f=next(open('6')) # part 2
for i in range(len(f)):
    if len(set(f[i:i+14]))>13:print(i+14);break

# golf
l=next(open("6"));print(min(i if len(set(l[i-4:i]))>3else len(l)for i in range(4,len(l))))

l=next(open("6"));print(min(i if len(set(l[i-14:i]))>13else len(l)for i in range(14,len(l))))
f=next(open('6')) # part 1
for i in range(len(f)):
    if len(set(f[i:i+4]))>3:print(i+4);break
    
f=next(open('6')) # part 2
for i in range(len(f)):
    if len(set(f[i:i+14]))>13:print(i+14);break

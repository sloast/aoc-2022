m,s,i='=-012'.index,'',0;x=sum(sum(map(lambda a,b:a*b,[5**(i-2)for i in range(len(l),1,-1)],[-2+m(c)for c in l[:-1]]))for l in open('25'))
while x!=0:b=pow(5,i);n='012=-'[x%(5*b)//b];x-=(m(n)-2)*b;s=n+s;i+=1
print(s)
# part 1
#print(sum(ord(s)-(96,38)[s<'a']for s in[(a&b).pop()for a,b in map(lambda x:(set(x[:len(x)//2]),set(x[len(x)//2:])),open('3'))]))
#print(sum([[ord(i[0])-(96,38)[i[0]<'a']for i in[*set(l[:len(l)//2])&set(l[len(l)//2:])]][0]for l in open('3')]))
print(sum([[ord(i)-58*(i>'Z')-38for i in[*set(l[:len(l)//2])&set(l[len(l)//2:])][0]][0]for l in open('3')]))

# part 2
# by me
#print(sum(ord(s)-(96,38)[s<'a']for s in[(a&b&c).pop()for a,b,c in zip(*(map(lambda x:set(x[:-1]),open('3')),)*3)]))
#print(sum(ord(s)-(96,38)[s<'a']for s in((a&b&c-set('\n')).pop()for a,b,c in zip(*(map(set,open("3")),)*3))))

# @geo#5319's solution
j="".join;print(sum(ord(s)-58*(s>'Z')-24 for s in j(j(a&b&c)for a,b,c in zip(*(map(set,open("3")),)*3)))) # type: ignore

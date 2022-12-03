# part 1
print(sum(ord(s)-(96,38)[s<'a']for s in[(a&b).pop()for a,b in map(lambda x:(set(x[:len(x)//2]),set(x[len(x)//2:])),open('3'))]))

# part 2
print(sum(ord(s)-(96,38)[s<'a']for s in[(a&b&c).pop()for a,b,c in zip(*(map(lambda x:set(x),open('3')),)*3)]))
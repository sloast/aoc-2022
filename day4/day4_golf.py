# part 1
# print(sum((a<=b)or(b<a)for a,b in map(lambda l:map(lambda x:set(range(*(lambda m:(m[0],m[1]+1))(list(map(int,x.split('-')))))),l.split(',')),open('4'))))
# m=map;print(sum((a<=b)or(b<a)for a,b in m(lambda l:m(lambda x:set(range(*(lambda m:(m[0],m[1]+1))(list(m(int,x.split('-')))))),l.split(',')),open('4'))))
# print(sum(a<=c<=b>=d or b<=d>=c>=a for a,b,c,d in map(lambda l:map(int,'-'.join(l.split(',')).split('-')),open('4'))))

# part 2
# print(sum(c<=b>=a<=d for a,b,c,d in map(lambda l:map(int,'-'.join(l.split(',')).split('-')),open('4'))))

# part 1
import re;print(sum(a<=c<=b>=d or b<=d>=c>=a for a,b,c,d in map(lambda x:map(int,re.split(',|-',x)),open('4'))))

# part 2
import re;print(sum(c<=b>=a<=d for a,b,c,d in map(lambda x:map(int,re.split(',|-',x)),open('4'))))

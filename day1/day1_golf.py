print(max(sum(map(int, l.split()))for l in open('1').read().split('\n'*2)))

print(sum(sorted(sum(map(int, l.split()))for l in open('1').read().split('\n'*2))[-3:]))
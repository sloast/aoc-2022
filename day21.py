import operator
operations = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.floordiv}

inp = [l.strip().split() for l in open('21')]
monkeys = {l[0][:-1]:[l[1], operations[l[2]], l[3]] if len(l) > 2 else int(l[1]) for l in inp}
#debugeys = {l[0][:-1]:l for l in inp}

def eval(monkey):
    dat = monkeys[monkey]
    if isinstance(dat, int):
        return dat
    else:
        return dat[1](eval(dat[0]), eval(dat[2]))
    
# Part 1
print("\nPart 1:", eval('root'))

# Part 2

opposites = {operator.sub: operator.add,
             operator.add: operator.sub,
             operator.floordiv: operator.mul,
             operator.mul: operator.floordiv}

def findhumn(monkey):
    dat = monkeys[monkey]
    if monkey == 'humn':
        return 1
    if isinstance(dat, int):
        return 0
    else:
        return 1 if findhumn(dat[0]) else 3 if findhumn(dat[2]) else 0
    
def calchumn(monkey,val):
    #print(val, ',', monkey, ': ', debugeys[monkey])
    if monkey == 'humn':
        return val
    dat = monkeys[monkey]
    currbranch = findhumn(monkey)
    if currbranch == 3 and dat[1] in [operator.sub, operator.floordiv]:
        val = dat[1](eval(dat[0]), val)
    else:
        val = opposites[dat[1]](val, eval(dat[3-currbranch]))
    #print(val, ',', monkey, ': ', currbranch, 'op=',debugeys[monkey][2] ,  eval(dat[3-currbranch]))
    return calchumn(dat[currbranch-1], val)


humn_branch = findhumn('root')

second_val = eval(monkeys['root'][3-(humn_branch)])
humnval = calchumn(monkeys['root'][humn_branch-1], second_val)
print('Part 2:',humnval)
monkeys['humn'] = humnval
result = eval(monkeys['root'][humn_branch-1])
print("\nroot:", second_val, '=', result, '->', 'correct' if result==second_val else 'wrong')
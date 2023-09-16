def part1():
    f = open('day2.txt', 'r').readlines()
    score = 0
    arr = 'ABCXYZ'
    for line in f:
        l = line.strip().split(' ')
        i0 = arr.index(l[0])
        i1 = arr.index(l[1]) - 3
        score += i1 + 1
        if i0 == i1:
            score += 3
        elif i1 - i0 == 1 or i1 - i0 == -2:
            score += 6
    print(score)


def part2():
    f = open('day2.txt', 'r').readlines()
    score = 0
    arr = 'ABCXYZ'
    for line in f:
        l = line.strip().split(' ')
        i0 = arr.index(l[0])
        i1 = arr.index(l[1]) - 3
        score += (i0 + 1 + i1 - 2) % 3 + 1 + i1 * 3
    print(score)


if __name__ == '__main__':
    part1()
    part2()

import re

f = [l[:-1] for l in open('22')]
board = f[:-2]
moves = f[-1]
width = max(len(l) for l in board)
height = len(board)

#print(width, height)
#print('\n'.join(board))
bounds = [(len(re.search(" *", l).group()), len(l)-1) for l in board]

x, y  = bounds[0][0], 0
dist = 0
direction = 0
vects = [(1,0),(0,1),(-1,0),(0,-1)]
board[y] = board[y][:x] + '>v<^'[direction] + board[y][x+1:]

def move(d):
    global x,y
    for _ in range(d):
        nx, ny = x + vects[direction][0], y + vects[direction][1]
        if direction % 2 == 0:
            if nx < bounds[ny][0]:
                nx = bounds[ny][1]
            elif nx > bounds[ny][1]:
                nx = bounds[ny][0]
        elif ny < 0 or ny >= len(board) or nx < bounds[ny][0] or nx > bounds[ny][1]:
            opposite = -vects[direction][1]
            cy = y
            while 0<=cy<len(board) and bounds[cy][0]<=nx<=bounds[cy][1]:
                cy += opposite
            ny = cy - opposite                
                
        if board[ny][nx] in '.>v<^':
            x, y = nx, ny
        board[y] = board[y][:x] + '>v<^'[direction] + board[y][x+1:]
m = ''
for m in moves:
    if m.isalpha():
        move(dist)
        #print(x, y)
        dist = 0
        direction += 1 if m == 'R' else -1
        direction %= 4
        board[y] = board[y][:x] + '>v<^'[direction] + board[y][x+1:]
        ##print('\n'.join(board),'\n')
    else:
        dist *= 10
        dist += int(m)
if m.isnumeric():
    move(dist)
    
board[y] = board[y][:x] + 'X' + board[y][x+1:]
print('\n'.join(board),'\n')
    
print("final pos: ",x, y)

print((y+1)*1000+(x+1)*4+direction)

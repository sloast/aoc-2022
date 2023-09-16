import re
import typing

'''
# test input
files = [l[:-1] for l in open('22.test')][:14]
CUBE_SIDE = 4
faces = [(2,0),(0,1),(1,1),(2,1),(2,2),(3,2)]
connection = {
    (0,0):(5,2), (0,1):(3,1), (0,2):(2,1), (0,3):(1,1),
    (1,0):(2,0), (1,1):(4,3), (1,2):(5,3), (1,3):(0,1),
    (2,0):(3,0), (2,1):(4,0), (2,2):(1,2), (2,3):(0,0),
    (3,0):(5,1), (3,1):(4,1), (3,2):(2,2), (3,3):(0,3),
    (4,0):(5,0), (4,1):(1,3), (4,2):(2,3), (4,3):(3,3),
    (5,0):(0,2), (5,1):(1,0), (5,2):(4,2), (5,3):(3,2),
}'''


# real input
files = [l[:-1] for l in open('22')]
CUBE_SIDE = 50
faces = [(1,0),(2,0),(1,1),(0,2),(1,2),(0,3)]
connection = {
    (0,0):(1,0), (0,1):(2,1), (0,2):(3,0), (0,3):(5,0),
    (1,0):(4,2), (1,1):(2,2), (1,2):(0,2), (1,3):(5,3),
    (2,0):(1,3), (2,1):(4,1), (2,2):(3,1), (2,3):(0,3),
    (3,0):(4,0), (3,1):(5,1), (3,2):(0,0), (3,3):(2,0),
    (4,0):(1,2), (4,1):(5,2), (4,2):(3,2), (4,3):(2,3),
    (5,0):(4,3), (5,1):(1,1), (5,2):(0,1), (5,3):(3,3),
}

# assert connections are consistent
for c,d in connection.items():
    e = connection[d[0], (d[1]+2)%4]
    #print(((c)==(e[0], (e[1]+2)%4)), c, connection[d[0], (d[1]+2)%4])
    assert ((c)==(e[0], (e[1]+2)%4))


board = files[:-2]
moves = files[-1]
x, y  = 0, 0
curr_face = 0
dist = 0
direction = 0
vects = [(1,0),(0,1),(-1,0),(0,-1)]

def local_to_global(x, y, face):
    return x+faces[face][0]*CUBE_SIDE, y+faces[face][1]*CUBE_SIDE

def rotate(x, y, angle):
    for _ in range(angle%4):
        tmp = y
        y = x
        x = CUBE_SIDE - tmp - 1
    return x,y

def move(d):
    global x,y,direction,curr_face
    for _ in range(d):
        nx, ny = x + vects[direction][0], y + vects[direction][1]
        next_face = curr_face
        next_direction = direction
        if min(nx, ny) < 0 or max(nx, ny) >= CUBE_SIDE:
            nx%=CUBE_SIDE;ny%=CUBE_SIDE
            next_face, next_direction = connection[(curr_face, direction)]
            nx, ny = rotate(nx, ny, next_direction-direction)
        
        gx, gy = local_to_global(nx, ny, next_face)
        if board[gy][gx] in '.>v<^':
            x, y = nx, ny
            curr_face, direction = next_face, next_direction
            board[gy] = board[gy][:gx] + '>v<^'[direction] + board[gy][gx+1:]
        #print('\n'.join(board),'\n')

gx, gy = local_to_global(x, y, curr_face)
board[gy] = board[gy][:gx] + '>' + board[gy][gx+1:]

m = ''
for m in moves:
    if m.isalpha():
        move(dist)
        dist = 0
        direction += 1 if m == 'R' else -1
        direction %= 4
        gx, gy = local_to_global(x, y, curr_face)
        board[gy] = board[gy][:gx] + '>v<^'[direction] + board[gy][gx+1:]
        #print('\n'.join(board),'\n')
    else:
        dist *= 10
        dist += int(m)
if m.isnumeric():
    move(dist)
    
gx, gy = local_to_global(x, y, curr_face)
board[gy] = board[gy][:gx] + 'X' + board[gy][gx+1:]
print('\n'.join(board),'\n')

print("final pos: ",gx, gy)
print("answer:",(gy+1)*1000+(gx+1)*4+direction,'\n')

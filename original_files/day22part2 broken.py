import re
import typing

CUBE_SIDE = 4

class Face:
    def __init__(self, content, posx, posy):
        self.board = content
        self.netconnections = [None for _ in range(4)]
        self.connections = [None for _ in range(4)]
        self.rotations = [None for _ in range(4)]
        self.x = posx
        self.y = posy
    def __str__(self):
        return str((self.x,self.y))
    def cpycon(self):
        self.netconnections = self.connections.copy()
    def printconnections(self):
        print(', '.join(map(lambda c:' None ' if c is None else str((c.x, c.y)), self.connections)))
    def printnconnections(self):
        print(', '.join(map(lambda c:' None ' if c is None else str((c.x, c.y)), self.netconnections)))
    def printoffsets(self):
        print(', '.join(map(lambda c:' None ' if c is None else '  '+str(c)+ '   ', self.rotations)))

files = [l[:-1] for l in open('22.test')]
board = files[:-2]
moves = files[-1]
width = max(len(l) for l in board)
height = len(board)


print(width, height)
print('\n'.join(board))
bounds = [(len(re.search(" *", l).group()), len(l)-1) for l in board]

facesgrid = [[None for _ in range(4)] for _ in range(4)]

for j in range(4):
    for i in range(4):
        x = i * CUBE_SIDE
        y = j * CUBE_SIDE
        if 0<=y<len(board) and bounds[y][0]<=x<=bounds[y][1]:
            print(i,j)
            facesgrid[j][i] = Face([[*l[x:x+CUBE_SIDE]] for l in board[y:y+CUBE_SIDE]], i, j)

for j in range(4):
    for i in range(4):
        curr = facesgrid[j][i]
        if i < 3 and curr is not None:
            curr = facesgrid[j][i]
            right = facesgrid[j][i+1]
            if right is not None:
                curr.connections[0] = right
                right.connections[2] = curr
                curr.rotations[0] = 2
                right.rotations[2] = 0
        if j < 3 and curr is not None:
            curr = facesgrid[j][i]
            down = facesgrid[j+1][i]
            if down is not None:
                curr.connections[1] = down
                down.connections[3] = curr
                curr.rotations[1] = 2
                down.rotations[3] = 0
        

for i in facesgrid:
    print(*map(str,i))

faces: list[Face] = [*filter(lambda x:x is not None,
                             [*facesgrid[0], *facesgrid[1], *facesgrid[2], *facesgrid[3]])]
for f in faces:f.cpycon()
f:Face = None
for f in faces:
    f.printconnections()
for f in faces:
    for side in range(4):
        if f.connections[side] is None:
            curr = f
            direction = (side+1)%4
            #expectedoffset = 3
            remaining = -1
            count = 0
            flg = False
            found = False
            while count < 6:
                dd = '>v<^'
                print(f'{dd[direction]} of {str(curr)}, for face {str(f)}, {dd[side]}, flg={not flg}, expectedoffset={expectedoffset}, forward')
                if curr.netconnections[direction] is None:
                    count+=1
                    flg = not flg
                    if flg:
                        if (direction - side)%4 == expectedoffset:
                            other = curr
                            #assert other.connections[direction] is None
                            f.connections[side] = other
                            other.connections[direction] = f
                            f.rotations[side] = (direction-side)%4
                            other.rotations[direction]=(side-direction)%4
                            found = True
                            break
                        expectedoffset=(expectedoffset +1) % 4
                    direction = (direction+1) % 4
                    
                else:
                    curr = curr.netconnections[direction]
                    direction = (direction-1) % 4
            curr = f
            direction = (side-1)%4
            expectedoffset = 1
            count = 0
            flg = False
            while not found and count < 6:
                dd = '>v<^'
                print(f'{dd[direction]} of {str(curr)}, for face {str(f)}, {dd[side]}, flg={not flg}, expectedoffset={expectedoffset}, reverse')
                if curr.netconnections[direction] is None:
                    count+=1
                    flg = not flg
                    if flg:
                        if (direction - side)%4 == expectedoffset:
                            other = curr
                            f.connections[side] = other
                            other.connections[direction] = f
                            f.rotations[side] = (direction-side)%4
                            other.rotations[direction]=(side-direction)%4
                            found = True
                            break
                        expectedoffset=(expectedoffset -1) % 4
                    direction = (direction-1) % 4
                    
                else:
                    curr = curr.netconnections[direction]
                    direction = (direction+1) % 4
                    
                            
                    

print(faces)
for f in faces:
    f.printconnections();f.printoffsets()
quit()

#print(bounds)
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
        #print('\n'.join(board),'\n')
        #board[y] = board[y].replace('<','.').replace('>','.').replace('^','.').replace('v','.')
m = ''
for m in moves:
    if m.isalpha():
        move(dist)
        print(x, y)
        print (m,"alp")
        dist = 0
        direction += 1 if m == 'R' else -1
        direction %= 4
        board[y] = board[y][:x] + '>v<^'[direction] + board[y][x+1:]
        print('\n'.join(board),'\n')
    else:
        dist *= 10
        dist += int(m)
        print(dist)
if m.isnumeric():
    move(dist)
    
board[y] = board[y][:x] + 'X' + board[y][x+1:]
print('\n'.join(board),'\n')
    
print("final pos: ",x, y)

print((y+1)*1000+(x+1)*4+direction)

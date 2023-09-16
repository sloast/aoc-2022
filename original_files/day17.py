jets = open('17').read().strip()

ONE_TRILLION = 1000000000000
blocksFallen = 0
TARGET_BLOCKS = ONE_TRILLION
jet_index = 0
block_index = 0
world = []
WORLD_WIDTH = 7
duplicate_detected = False
duplicate_height = 0;

blocks = [[(0,0),(1,0),(2,0),(3,0)], [(0,1),(1,0),(1,1),(1,2),(2,1)], [(0,0),(1,0),(2,0),(2,1),(2,2)], [(0,0),(0,1),(0,2),(0,3)], [(0,0),(0,1),(1,0),(1,1)]]
known_positions = {}

def valid(rx, ry, blk):
    for dx, dy in blocks[blk]:
        x, y = rx+dx, ry+dy
        if min(x, y)<0 or x>=WORLD_WIDTH:
            return False
        if y < len(world):
            if (world[y]) & (1 << x):
                return False
    return True

def putblock(rx, ry, blk):
    for dx, dy in blocks[blk]:
        nx, ny = rx+dx, ry+dy
        while ny >= len(world):
            world.append(0)
        
        world[ny] = world[ny] | (1 << nx)
        
def printout(limit=-1):
    for r in world if limit == -1 else world[:limit]:
        print(''.join(['@' if (r & (1 << x)) else '.' for x in range(WORLD_WIDTH)]))

while blocksFallen < TARGET_BLOCKS:
    
    if blocksFallen > 500 and not duplicate_detected:
        key = (block_index, jet_index, world[-1], world[-2], world[-3])
        
        if key in known_positions:
            duplicate_detected = True
            startBlocksFallen, startHeight = known_positions[key]
            numberOfBlocks = blocksFallen - startBlocksFallen
            repeated_block_height = len(world) - startHeight
            print("duplicate! at ", blocksFallen, ", length = ", numberOfBlocks, repeated_block_height)
            duplications_possible = (TARGET_BLOCKS - blocksFallen) // numberOfBlocks
            duplicate_height = duplications_possible * repeated_block_height
            TARGET_BLOCKS -= duplications_possible * numberOfBlocks
            
            
        else:
            known_positions[key] = (blocksFallen,  len(world))
            
    
    x, y = 2, len(world) + 3
    in_air = True
    while in_air:
        next_move = 1 if jets[jet_index] == '>' else -1
        jet_index = (jet_index + 1) % len(jets)
        
        if valid(x + next_move, y, block_index):
            x += next_move
        
        if valid(x, y - 1, block_index):
            y -= 1
        else:
            in_air = False
    
    putblock(x, y, block_index)
    
    block_index = (block_index + 1) % 5
    blocksFallen+=1

    #print(x, y)

#printout()
print(len(world))
print(len(world) + duplicate_height)
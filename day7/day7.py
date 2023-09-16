import re

class File:
    def __init__(self, name, parent, size):
        self.size = size
        self.parent = parent
        self.name = name
    
    def __eq__(self, other):
        return self.name == other.name and self.parent == other.parent
    def __str__(self):
        return str(self.size) + ' ' + self.name
    def getSize(self):
        return self.size

class Dir:
    def __init__(self, name, parent):
        self.size = 0
        self.name = name
        self.parent = parent
        self.children = []
    def __eq__(self, other):
        if self.name == '/':
            return self.name == other.name
        return self.name == other.name and self.parent == other.parent
    def __str__(self):
        return 'dir ' + self.name
    def getSize(self):
        self.size = 0
        for c in self.children:
            self.size += c.getSize()
        return self.size
    def __lt__(self, other):
        return self.size < other.size

files = []
dirs = [Dir('/', None)]
curr = dirs[0]

   
def finddir(name, parent):
    for d in dirs:
        if d.name == '/':
            if name == '/':
                return d
        elif d.name == name and d.parent == parent:
            return d
        

for l in open('7'):
    if l.startswith('$ cd ..'):
        if curr.name == '/':
            pass
        else:
            curr = curr.parent
    elif l.startswith('$ cd'):
        curr = finddir(l[5:].strip(), curr)
        print(curr)
    elif not l.startswith('$'):
        if re.match('[0-9]+ [a-zA-Z.]+', l.strip()):
            f = File(l.split()[1], curr, int(l.split()[0]))
            if not f in files:
                files.append(f)
                curr.children.append(f)
        elif l.startswith('dir'):
            d = Dir(l.split()[1], curr)
            if not d in dirs:
                dirs.append(d)
                curr.children.append(d)
print(files)
print(dirs)
print(curr)

total = 0

rootsize = dirs[0].getSize()

for d in dirs:
    if d.size <= 100000:
        total += d.size

print(total)

dirs.sort()
for d in dirs:
    if rootsize - d.size <= 40000000:
        print(d.size)
        break
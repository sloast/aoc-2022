class Test:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return self.name == other.name
    
a = Test('a')
b = Test('b')
c = Test('a')

arr = [b,c]

print(a == b)
print(a == c)
print(a in arr)
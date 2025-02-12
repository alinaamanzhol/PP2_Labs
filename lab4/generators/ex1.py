class Squares:
    def __init__(self, x):
        self.x = x
    
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a>self.x:
            raise StopIteration
        t = self.a
        self.a+=1
        return t**2

n = int(input())

num = Squares(n)


for i in num:
    print(i)
        

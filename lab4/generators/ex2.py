class Numbers:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.it = 0
        return self
    def __next__(self):
        if self.it > self.n:
            raise StopIteration
        self.t = self.it #0 
        self.it += 2 #2
        return self.t
    
n = int(input())
a = Numbers(n)
it = iter(a)
arr= []
for i in it:
    arr.append(i)
print(*arr, sep=', ')
        
    
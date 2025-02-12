def Squares(a, b):
    for i in range(a, b + 1):
        yield i**2
        
a = int(input())
b = int(input())
for i in Squares(a, b):
    print(i)
        
import math as m
def area(n, a):
    return (n*a**2)/(4*m.tan(m.pi/n))

n = int(input('Input number of sides: '))
a = int(input('Input length of a side: '))
s = area(n, a)
print(f"The area of the polygon is: {round(s)}")
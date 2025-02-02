class String:
    def __init__(self, text):
        self.a = text
        self.b = self.a.upper()
    
    def __str__(self):
        return self.b

t = String(input())

print(t.b)
    
    
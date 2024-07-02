class Calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        return self.n ** 2
    
    def cube(self):
        return self.n ** 3
    
    def square_root(self):
        return self.n ** (1 / 2)
    
a = Calculator(25)
print(a.square())
print(a.cube())
print(a.square_root())
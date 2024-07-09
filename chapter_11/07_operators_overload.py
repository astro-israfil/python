class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    def __mul__(self, num):
        return self.n + num.n
    def __sub__(self, num):
        return self.n + num.n

a = Number(4)
b = Number(5)
print(a + b)
class Two_D_Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i {self.j}j")


class Three_D_Vector(Two_D_Vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.i = i
        self.j = j
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i {self.j}j {self.k}k")


a = Two_D_Vector(10, 20)
b = Three_D_Vector(10, 20, 30)

a.show()
b.show()

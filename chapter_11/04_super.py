class Employee:
    a = 1
    def __init__(self):
        print("Contrutor of Employee")


class Programmer(Employee):
    b = 2
    def __init__(self):
        super().__init__()
        print("Contrutor of Programmer")


class Manager(Programmer):
    c = 3
    def __init__(self):
        super().__init__()
        print("Contrutor of Manager")


# m = Employee()
# p = Programmer()
mg = Manager()

# print(m.a)
# print(p.a, p.b)
print(mg.a, mg.b, mg.c)
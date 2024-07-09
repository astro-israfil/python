class Employee:
    a = 1


class Programmer(Employee):
    b = 2


class Manager(Programmer):
    c = 3


m = Employee()
p = Programmer()
mg = Manager()

print(m.a)
print(p.a, p.b)
print(mg.a, mg.b, mg.c)


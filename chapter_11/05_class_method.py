class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"a is {cls.a}")


employee = Employee()
employee.a = 45
employee.show()
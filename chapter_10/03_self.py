class Employee:
    language = "JavaScript"
    salary = 200000

    def greet_info(self):
        print(f"The language is {self.language}, The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")



israfil = Employee()

israfil.greet_info()
# Employee.greet_info(israfil)

israfil.greet()
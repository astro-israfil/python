class Employee:
    company = "Microsoft"

    def __init__(self, name, age, language, salary):
        self.name = name
        self.age = age
        self.language = language
        self.salary = salary
        print(f"Creating object for {name}")
    
    def greet_info(self):
        print(f"I am {self.name}. I am an employee of {self.company} and I am {self.age}")

employee1 = Employee("Israfil", 20, "JavaScript", 200000)
print(employee1.name, employee1.company)

employee2 = Employee("Rashed", 22, "Python", 300000)
print(employee2.name, employee2.company)
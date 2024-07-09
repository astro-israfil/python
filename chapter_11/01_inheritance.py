class Employee:
    company = "Microsoft"
    def greet_company(self):
        print(f"I am an employee of {self.company}")


class Programmer (Employee):
    language = "JavaScript"
    
    def greet(self):
        print(f"I am a {self.language} programmer")


programmer = Programmer()

programmer.greet_company()
programmer.greet()
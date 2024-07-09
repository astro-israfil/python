class Employee:
    company = "Microsoft"
    
    def sayCompanyName(self):
        print(f"I am an employee in {self.company}")


class Coder:
    language = "Python"

    def sayLanguage(self):
        print(f"I usually code {self.language}")


class Programmer(Employee, Coder):

    @staticmethod
    def greet():
        print("Programming is my passion")


p = Programmer()

p.sayCompanyName()
p.greet()
p.sayLanguage()
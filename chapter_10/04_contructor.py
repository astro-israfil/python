class Employee:
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")
    
    def greet_info(self):
        print(f"I am {self.name}, I am a {self.language} developer. my salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello")


employee1 = Employee("Israfil", "JavaScript", 200000)

print(employee1.name)
employee1.greet_info()
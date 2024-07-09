class Animal:
    pass

class Pet(Animal):
    pass

class Dog(Pet):
    @staticmethod
    def bark():
        print("bow bow")


dog = Dog()
dog.bark()
dog.bark()
dog.bark()
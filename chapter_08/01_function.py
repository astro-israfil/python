def greeting():
    print("Hello World!")
    return "Hello"


greet = greeting()
print(greet)


# Function with parameter
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print(result)


# Function with default parameter

def greet_person(name, ending="Thank you"):
    print(f"Hello {name}, good day")
    print(ending)


greet_person("Israfil", "Thanks")

greet_person("Dianna")



# Function with Variable-Length Arguments
def print_args(*args, **kwargs):
    print("*args:", args)
    print("**kwargs:", kwargs)


print_args(10, 32, 54, 132, name="Israfil", age=20)




# Lambda function
add = lambda x, y: x + y

print(add(1, 2))
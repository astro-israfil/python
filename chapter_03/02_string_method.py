greeting = "hello world"

print(len(greeting))
print(greeting.capitalize())
print(greeting.lower())
print(greeting.startswith("he"))
print(greeting.endswith("world"))
print(greeting.find("world"))
print(greeting.title())
print(greeting.split())
print(greeting.isdigit()) # False
print("4344".isdigit()) # True
print("Hello".isalpha()) # True
print(" ".join(["Hello", "World"]))

name = "           Israfil       "

print(name)

striped_name = name.strip()

print(striped_name)

print(greeting.replace("world", "python"))
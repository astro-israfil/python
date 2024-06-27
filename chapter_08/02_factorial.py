# n! = n X n - 1 X .... X 3 X 2 X 1
# n! = n X factorial(n - 1)

# Recursion
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Please enter a number: "))

print(f"Factorial of {n} is {factorial(n)}")
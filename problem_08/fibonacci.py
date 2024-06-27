# f = n + n - 1 + .... + 1

def fibonacci(n):
    if n == 0:
        return 0
    return n + fibonacci(n - 1)


n = int(input("Please enter a number: "))

print(f"Fibonacci of {n} is {fibonacci(n)}")
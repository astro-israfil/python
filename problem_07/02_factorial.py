# 5! = 1 X 2 X 3 X 4 X 5

n = int(input("Please enter a number you want factorial: "))

product = 1

for i in range(1, n + 1):
    product *= i

print(f"The factorial of {n} is {product}")
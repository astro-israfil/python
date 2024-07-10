a = int(input("Please enter the number a: "))
b = int(input("Please enter the number b: "))

if (b == 0):
    raise ZeroDivisionError("You can't divide a number by zero (0)")
else:
    print(f"a divided by b is qual to {a / b}")
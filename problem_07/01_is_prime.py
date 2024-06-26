n = int(input("Please enter a number: "))

for i in range(2, n):
    if (n % i) == 0:
        print("The number is not a prime number")
        break
else:
    print("This number is a prime number")
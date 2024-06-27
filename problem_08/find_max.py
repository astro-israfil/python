def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c


a = int(input("Please enter number a: "))
b = int(input("Please enter number b: "))
c = int(input("Please enter number c: "))

print(find_max(a, b, c))
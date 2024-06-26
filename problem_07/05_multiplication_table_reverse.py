"""
10 X 10 = 100
10 X 9 = 90
10 X 8 = 80
10 X 7 = 70
10 X 6 = 60
10 X 5 = 50
10 X 4 = 40
10 X 3 = 30
10 X 2 = 20
10 X 1 = 10
"""

n = int(input("Please enter a number: "))

for i in range(1, 11):
    print(f"{n} X {11 - i} = {n * (11 - i)}")
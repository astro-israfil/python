from typing import List

number = int(input("Please enter a number you want multiplication table: "))

multiplication_table: List[int] = [number * i for i in range(1, 11)]

print(multiplication_table)
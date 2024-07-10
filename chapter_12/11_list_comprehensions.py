from typing import List

numbers: List[int] = [10, 20, 30, 40, 50]

numbers_square: List[int] = [i ** 2 for i in numbers]

print(numbers_square)
from typing import List

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

for index, item in enumerate(numbers):
    if index != 2 and index != 4 and index != 6:
        continue
    else:
        print(item)
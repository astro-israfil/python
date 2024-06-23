fruits = ["Apple", "Banna", "Litchi", "Mango"]

fruits.append("Orange")

# print(fruits)

fruits_list = ["Cherry", "Watermelon"]

fruits.extend(fruits_list)

# print(fruits)

fruits.insert(1, "Pineapple")

# print(fruits)

fruits.remove("Litchi")

# print(fruits)

removed_fruit = fruits.pop(3)

# print(fruits, removed_fruit)

# print(fruits.index("Pineapple"))

numbers_list = [1, 5, 2, 3, 7, 5, 6]

# numbers_list.sort()
numbers_list.reverse()

# print(numbers_list)

busket = fruits.copy()

print(busket)

print(len(busket))
my_tupple = (10, 20, 30, 40, 50)


index = my_tupple.index(40)
print(index)
print(len(my_tupple))

# Packing a Tuple
another_tuple = 10, 20, 40, 50

# Unpacking a Tuple
a, b, c, d = another_tuple

print(another_tuple)
print(a, b, c, d)

# Concatenating and repeating tuple

repeated_tuple = my_tupple * 3

print(repeated_tuple)

concatenated_tupple = my_tupple + another_tuple

print(concatenated_tupple)


# Membership Operation
print(50 in my_tupple)
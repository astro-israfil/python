my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(my_dict, type(my_dict))

# using dict function

my_dict1 = dict(name="Israfil", age=20, city="Dhaka")

print(my_dict1)


# accessing dictionary
my_name = my_dict1['name']
print(my_name)


# modifying value
my_dict1["age"] = 22
print(my_dict1["age"])


# add key-value pairs
my_dict1["email"] = "israfil@abc.com"
print(my_dict1)

# delete a key of dict
del my_dict1["email"]
print(my_dict1)


# membership
is_name_in_dict = "name" in my_dict
print(is_name_in_dict)
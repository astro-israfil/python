my_dict = {
    "name": "Israfil",
    "age": 22,
    "city": "Dhaka",
    "email": "israfil@xyz.com"
}

# print(len(my_dict))

# my_dict.clear() # remove all keys from dictionary

# print(my_dict)

new_dict = my_dict.copy() # make a shallow copy of a dict

new_dict["name"] = "Abdullah"

# print(new_dict)
# print(my_dict)


# getting value using get method
print(my_dict.get("email"))

print(my_dict.items())

print(my_dict.keys())

email = my_dict.pop("email", "israfil@abc.com")
print(email)

print(my_dict)

my_dict.update({"name": "Abdullah", "age": 20})
print(my_dict)

values = my_dict.values()
print(values)
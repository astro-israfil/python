# f = open("file.txt", "r")
# text = f.read()
# f.close()
# print(text)

with open("file.txt") as f:
    print(f.read())
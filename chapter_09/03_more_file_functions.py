f = open("file.txt", "r")
# str_lines = f.readlines()
# f.close()

# print(str_lines, type(str_lines))

# str_line1 = f.readline()
# print(str_line1)

# str_line2 = f.readline()
# print(str_line2)

# str_line3 = f.readline()
# print(str_line3)

# str_line4 = f.readline()
# print(str_line4)

line = f.readline()
while (line):
    print(line)
    line = f.readline()

f.close()
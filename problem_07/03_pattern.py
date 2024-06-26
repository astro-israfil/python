"""
   #
  ###
 #####
#######
"""

line_of_hash = int(input("Please enter how many lines you want to print: "))

for i in range(1, line_of_hash + 1):
    print(" " * (line_of_hash - i), end="")
    print("#" * (2 * i - 1))
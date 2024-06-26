for i in range(10):
    if (i == 8):
        break         # break the loop here

    print(i)


for i in range(5):
    if (i == 3):
        continue      # skip the iteration here

    print(i)


for i in range(10):
    if (i == 5):
        pass          # do nothing when i == 5
    print(i)


for i in range(20):
    pass              # do nothing


i = 0
while (i < 5):
    print(i)
    i += 1
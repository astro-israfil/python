num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = int(input("Please enter a number: "))

if (num1 > num2):
    if (num1 > num3):
        print("Number 1 is biggest", num1)
    else :
        print("Number 3 is biggest", num3)
elif (num2 > num1): 
    if (num2 > num3): 
        print("Number 2 is biggest", num2)
    else :
        print("Number 3 is biggest", num3)
elif (num1 == num2) :
    if (num1 > num3) :
        print("Number 1 and 2 is equal and its greater than number 3")

    else :
        print("Number 3 is biggest")




if (num1 > num2 and num1 > num3) :
    print("number 1 is biggest")
elif (num2 > num1 and num2 > num3) :
    print("number 2 is biggest")
else :
    print("number 3 is biggest")
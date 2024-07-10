try:
    a = int(input("Please enter a number: "))
    print(f"You have entered the number {a}")

except Exception as e:
    print(e)

else:
    print("The programm is executed successfully")

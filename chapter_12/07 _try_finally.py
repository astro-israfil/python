def main():
    try:
        a = int(input("Please enter a number: "))
        print(f"You have entered the number {a}")
        return a

    except Exception as e:
        return e

    finally:
        print("This block of code is always going to be executed!")


a = main()
print(a)
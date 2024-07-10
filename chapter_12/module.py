def myFunc():
    print("Hello World")

if __name__ == "__main__":
    myFunc()
    print("This code is executing inside the file in which the code is written")
else:
    print("This code is executing inside the file where the code written file is imported as module")
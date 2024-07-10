try:
    a = int(input("Please enter a number "))
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
finally:
    print("loading = False")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

temperature_in_celsius = float(input("Please enter temperature in celsius: "))
print(f"Temperature in fahrenheit is {celsius_to_fahrenheit(temperature_in_celsius)}")
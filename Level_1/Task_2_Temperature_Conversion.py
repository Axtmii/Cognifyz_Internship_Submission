temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    converted = (temperature * 9/5) + 32
    print("Converted temperature:", converted, "F")
elif unit == "F":
    converted = (temperature - 32) * 5/9
    print("Converted temperature:", converted, "C")
else:
    print("Invalid unit. Please enter C or F.")
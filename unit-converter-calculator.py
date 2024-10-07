def unit_converter():
    print("Welcome to the Unit Converter Calculator")

    # Define conversion factors
    conversions = {
        "length": {
            "meters to feet": 3.28084,
            "feet to meters": 0.3048,
            "kilometers to miles": 0.621371,
            "miles to kilometers": 1.60934
        },
        "weight": {
            "kilograms to pounds": 2.20462,
            "pounds to kilograms": 0.453592
        },
        "temperature": {
            "celsius to fahrenheit": lambda c: (c * 9/5) + 32,
            "fahrenheit to celsius": lambda f: (f - 32) * 5/9
        }
    }

    # Select Unit Type
    print("\nAvailable unit types:")
    for unit_type in conversions.keys():
        print(f"- {unit_type}")
    unit_type = input("Select unit type: ").lower()

    if unit_type not in conversions:
        return "Invalid unit type selected."

    # Select specific conversion
    print(f"\nAvailable {unit_type} conversions:")
    for conversion in conversions[unit_type].keys():
        print(f"- {conversion}")
    conversion = input("Select conversion: ").lower()

    if conversion not in conversions[unit_type]:
        return "Invalid conversion selected."

    # Get input value
    value = float(input(f"\nEnter value to convert ({conversion.split(' to ')[0]}): "))

    # Convert
    if unit_type == "temperature":
        result = conversions[unit_type][conversion](value)
    else:
        result = value * conversions[unit_type][conversion]

    # Display result
    from_unit, to_unit = conversion.split(" to ")
    return f"\nResult: {value} {from_unit} is equal to {result:.2f} {to_unit}"

# Start the program
if __name__ == "__main__":
    print(unit_converter())
    print("Program stopped")

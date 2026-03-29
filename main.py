import argparse
import unit_conversion as uc
from helper_functions import perform_conversion

# Instantiate a parser
parser = argparse.ArgumentParser(description="A command line tool to convert US customary units to metric units.\
    Provide a value and a unit to the command line and conversion will be done.")

# Add arguments
parser.add_argument("value", type=float, nargs="?", help="The value to be converted")
parser.add_argument("unit", type=str, nargs="*", help="The unit to be converted")

# Add optional argument
parser.add_argument("-i", "--interactive", action="store_true", help="Run the tool in interactive mode")

# Collect arguments
args = parser.parse_args()

# Handle space arguments
args.unit = " ".join(args.unit)

# List of conversion classes
conversion_classes = [uc.Area, uc.Capacity, uc.Distance, uc.Mass, uc.Temperature, uc.Volume]


if args.interactive:
    print("Entering interactive mode (type 'quit' to exit)")
    # Create a while loop
    while True:
        cmd = input("Input a value and a unit (E.g., 3 feet) ").strip()
        # Create an exit for the loop
        if cmd.lower() == "quit":
            break
        
        # Split the input
        parts_input = cmd.split()
        if len(parts_input) < 2:
            print("Please provide a value and a unit")
            continue

        try:
            # Collect the value
            val = float(parts_input[0])
            # Collect the unit
            unit = " ".join(parts_input[1:])
            # Perform the conversion
            perform_conversion(value=val, unit=unit, conversion_classes=conversion_classes)

        except ValueError as e:
            # Only runs if float conversion fails
            print(e)
            continue
        
        
        
        

elif args.value is not None and args.unit is not None:
    # Single command line usage
    perform_conversion(value=args.value, unit=args.unit, conversion_classes=conversion_classes)

else:
    # Empty input
    parser.print_help()

'''
if args.interactive:
    print("Entering interactive mode (type 'quit' to exit)")
    # Create a while loop
    while True:
        cmd = input("Input a value and a unit (E.g., 3 feet)")
        # Create an exit for the loop
        if cmd.lower() == "quit":
            break
    
    # Search for the converter class
    found = False
    for converter in conversion_classes:
        try:
            # Try to instantiate the class (gives ValueError if unit doesn't match)
            conv_instance = converter(args.value, args.unit)
            print(conv_instance)
            found = True
            # Stop search if converter is identified
            break
        except ValueError:
            # Keep searching for the correct class
            continue

    if not found:
        print(f"Error: '{args.unit}' is not supported.")

else:
    # Search for the converter class
    found = False
    for converter in conversion_classes:
        try:
            # Try to instantiate the class (gives ValueError if unit doesn't match)
            conv_instance = converter(args.value, args.unit)
            print(conv_instance)
            found = True
            # Stop search if converter is identified
            break
        except ValueError:
            # Keep searching for the correct class
            continue

    if not found:
        print(f"Error: '{args.unit}' is not supported.")
    
    
        

# Search for the converter class
found = False
for converter in conversion_classes:
    try:
        # Try to instantiate the class (gives ValueError if unit doesn't match)
        conv_instance = converter(args.value, args.unit)
        print(conv_instance)
        found = True
        # Stop search if converter is identified
        break
    except ValueError:
        # Keep searching for the correct class
        continue

if not found:
    print(f"Error: '{args.unit}' is not supported.")'''
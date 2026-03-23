import argparse
import unit_conversion as uc

# Instantiate a parser
parser = argparse.ArgumentParser(description="A command line tool to convert US customary units to metric units.\
    Provide a value and a unit to the command line and conversion will be done.")

# Add arguments
parser.add_argument("value", type=float, help="The value to be converted")
parser.add_argument("unit", type=str, help="The unit to be converted")

# Collect arguments
args = parser.parse_args()

# List of conversion classes
conversion_classes = [uc.Area, uc.Capacity, uc.Distance, uc.Mass, uc.Temperature, uc.Volume]

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
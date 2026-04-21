import argparse
import unit_conversion as uc
from helper_functions import perform_conversion, print_supported_units, save_to_csv

def main():
    # Instantiate a parser
    parser = argparse.ArgumentParser(description="A command line tool to convert US customary units to metric units.\
        Provide a value and a unit to the command line and conversion will be done.")

    # Add arguments
    parser.add_argument("value", type=float, nargs="?", help="The value to be converted")
    parser.add_argument("unit", type=str, nargs="*", help="The unit to be converted")

    # Add optional arguments
    parser.add_argument("-i", "--interactive", action="store_true", help="Run the tool in interactive mode")
    parser.add_argument("-s", "--show", action="store_true", help="Show supported conversions")

    # Collect arguments
    args = parser.parse_args()

    # Handle space arguments
    args.unit = " ".join(args.unit)

    # List of conversion classes
    conversion_classes = [uc.Area, uc.Capacity, uc.Distance, uc.Mass, uc.Temperature, uc.Volume]

    if args.interactive:
        # Ask if user want to save conversion to a csv file
        ask_save = input("Do you want to save the conversions to a csv file? ('y' or 'n')? ").lower().strip()
        # Only accept 'y' or 'n'
        while ask_save not in ["y", "n"]:
            ask_save = input("Please enter 'y' for yes or 'n' for no: ").lower().strip()
        
        # Convert save answer to bool (True/False)
        yes_to_save = (ask_save.lower().strip() == "y")
        
        print("Entering interactive mode (type 'quit' to exit)")

        # Create a while loop
        while True:
            # Take user input    
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
                met_val, met_unit = perform_conversion(value=val, unit=unit, conversion_classes=conversion_classes)

                # Evaluate if the conversions should be saved to a csv file
                if yes_to_save:
                    save_to_csv(start_value=val, start_unit=unit, final_value=met_val, final_unit=met_unit)
                    print("Saved to conversion_results.csv")

            except ValueError as e:
                # Only runs if float conversion fails
                print(e)
                continue


    elif args.show:
        print_supported_units()
            
    elif args.value is not None and args.unit is not None:
        # Single command line usage
        perform_conversion(value=args.value, unit=args.unit, conversion_classes=conversion_classes)

    else:
        # Empty input
        parser.print_help()

if __name__ == "__main__":
    main()
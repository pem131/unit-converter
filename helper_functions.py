import csv
import os
from typing import TextIO

def perform_conversion(value: float, unit: str, conversion_classes: list[type]) -> tuple[float, str]:
    '''Returns the metric value after conversion or an ValueError if the unit is not supported'''
    # Search for the converter class
    for converter in conversion_classes:
        try:
            # Try to instantiate the class (gives ValueError if unit doesn't match)
            conv_instance = converter(value, unit)

            # Receive the conversion values
            met_val, met_unit = conv_instance.to_metric()

            # Print the result
            print(conv_instance)
            # Stop search if converter is identified
            return met_val, met_unit
        
        except ValueError:
            # Keep searching for the correct class
            continue
    
    raise ValueError(f"Unit {unit} is not supported.")

def save_to_csv(start_value: float, start_unit: str, final_value: float, final_unit: str) -> TextIO:
    '''Writes the values and units before and after conversion to a csv file'''
    # Define file name
    file_name = "conversion_results.csv"
    # Define the header
    csv_header = "non_converted_value", "non_converted_unit", "converted_value", "converted_unit"
    # Define the data
    data = [start_value, start_unit, final_value, final_unit]

    # Check if file exists
    file_exists = os.path.isfile(file_name)

    with open(file=file_name, mode="a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Only write if file didn't exist
        if not file_exists:
            writer.writerow(csv_header)
        
        # Add to file if it exist
        writer.writerow(data)


def print_supported_units() -> None:
    '''Prints the supported conversions'''
    print(
    '''DISTANCE
Inch\t\t-->\tCentimeters
Foot\t\t-->\tCentimeters
Yard\t\t-->\tCentimeters
Mile\t\t-->\tKilometers

AREA
Square inch\t-->\tSquare centimeters
Square foot\t-->\tSquare centimeters
Square yard\t-->\tSquare meters
Acre\t\t-->\tSquare meters
Square mile\t-->\tSquare kilometers

VOLUME
Cubic inch\t-->\tCubic centimeters
Cubic foot\t-->\tCubic centimeters
Cubic yard\t-->\tCubic centimeters

CAPACITY
Fluid ounce\t-->\tMilliliters
Cup\t\t-->\tMilliliters
Liquid pint\t-->\tMilliliters
Quart\t\t-->\tMilliliters
Liquid gallon\t-->\tLiters

MASS
Ounce\t\t-->\tGrams
Pound\t\t-->\tKilograms
Stone\t\t-->\tKilograms
Ton\t\t-->\tKilograms

TEMPERATURE
Fahrenheit\t-->\tKelvin
Celsius\t\t-->\tKelvin
''')
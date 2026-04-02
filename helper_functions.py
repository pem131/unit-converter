def perform_conversion(value: float, unit: str, conversion_classes: list[object]) -> tuple[float, str]:
    '''Returns the metric value after conversion or an ValueError if the unit is not supported'''
    # Search for the converter class
    found = False
    for converter in conversion_classes:
        try:
            # Try to instantiate the class (gives ValueError if unit doesn't match)
            conv_instance = converter(value, unit)
            print(conv_instance)
            found = True
            # Stop search if converter is identified
            break
        except ValueError:
            # Keep searching for the correct class
            continue
    
    if not found:
        raise ValueError(f"Unit {unit} is not supported.")

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
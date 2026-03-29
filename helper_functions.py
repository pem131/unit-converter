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
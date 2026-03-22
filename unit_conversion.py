class Distance:
    # Conversion constants
    INCH_TO_CM = 2.54
    FOOT_TO_CM = 30.48
    YARD_TO_CM = 91.44
    MILE_TO_KM = 1.61

    def __init__(self, value: float | int, unit: str = "inch"):
        self.value = value
        self.unit = unit.lower().rstrip("s")
    
    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (metric value, label)'''
        if self.unit == "inch":
            return float(self.value * self.INCH_TO_CM), "centimeters"
        elif self.unit in ["foot", "feet"]:
            return float(self.value * self.FOOT_TO_CM), "centimeters"
        elif self.unit == "yard":
            return float(self.value * self.YARD_TO_CM), "centimeters"
        elif self.unit == "mile":
            return (self.value * self.MILE_TO_KM), "kilometers"
        else:
            raise ValueError(f"Unit {self.unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the value'''
        # Get the metric value and label
        metric_value, label = self.to_metric()
        # Handle singular/plural for non metric
        display_unit = self.unit
        if self.value != 1:
            if self.unit == "inch":
                display_unit = "inches"
            elif self.unit == "foot":
                display_unit = "feet"
            elif not self.unit == "feet" and self.unit.endswith("s"):
                display_unit += "s"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self.value} {display_unit} is {metric_value:.2f} {label}"
 
class Area:
    # Coversion constants
    SQUARE_INCH_TO_SQUARE_CM = 6.45
    SQUARE_FOOT_TO_SQUARE_CM = 929
    SQUARE_YARD_TO_SQUARE_M = 0.84
    ACRE_TO_SQUARE_M = 4046.86
    SQUARE_MILE_TO_SQUARE_KM = 2.59

    def __init__(self, value: float | int, unit: str ="square inch"):
        self.value = value
        self.unit = unit.lower().rstrip("s")

    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (metric value, label)'''
        if self.unit == "square inch":
            return float(self.value * self.SQUARE_INCH_TO_SQUARE_CM), "square centimeters"
        elif self.unit in ["square foot", "square feet"]:
            return float(self.value * self.SQUARE_FOOT_TO_SQUARE_CM), "square centimeters"
        elif self.unit == "square yard":
            return float(self.value * self.SQUARE_YARD_TO_SQUARE_M), "square meters"
        elif self.unit == "acre":
            return float(self.value * self.ACRE_TO_SQUARE_M), "square meters"
        elif self.unit == "square mile":
            return float(self.value * self.SQUARE_MILE_TO_SQUARE_KM), "square kilometers"
        else:
            raise ValueError(f"Unit {self.unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the value'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        # Handle singular/plural for non-metric
        display_unit = self.unit
        if self.value != 1:
            if self.unit == "square inch":
                display_unit = "square inches"
            elif self.unit == "square foot":
                display_unit = "square feet"
            elif not self.unit == "square feet" and self.unit.endswith("s"):
                display_unit += "s"
        
        if self.value == 1:
            if self.unit == "square feet":
                display_unit = "square foot"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self.value} {display_unit} is {metric_value} {label}"

class Volume:
    # Conversion constants
    CUBIC_INCH_TO_CUBIC_CM = 16.4
    CUBIC_FOOT_TO_CUBIC_CM = 0.028
    CUBIC_YARD_TO_CUBIC_CM = 0.76

    def __init__(self, value: float | int, unit: str = "cubic inch") -> None:
        self.value = value
        self.unit = unit.lower().rstrip("s")
    
    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (metric value, label)'''
        if self.unit == "cubic inch":
            return float(self.value * self.CUBIC_INCH_TO_CUBIC_CM), "cubic centimeters"
        elif self.unit in ["cubic foot", "cubic feet"]:
            return float(self.value * self.CUBIC_FOOT_TO_CUBIC_CM), "cubic centimeters"
        elif self.unit == "cubic yard":
            return float(self.value * self.CUBIC_YARD_TO_CUBIC_CM), "cubic centimeters"
        else:
            raise ValueError(f"Unit {self.unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the value'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        # Handle singular/plural for non-metric
        display_unit = self.unit       
        if self.value != 1:
            if self.unit == "cubic inch":
                display_unit = "cubic inches"
            elif self.unit == "cubic foot":
                display_unit = "cubic feet"
            elif not self.unit == "cubic feet" and self.unit.endswith("s"):
                display_unit += "s"

        if self.value == 1:
            if self.unit == "cubic feet":
                display_unit = "cubic foot"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self.value} {display_unit} is {metric_value} {label}"

class Capacity:
    # Conversion constants
    FLUID_OUNCE_TO_ML = 29.57
    CUP_TO_ML = 236.59
    LIQUID_PINT_TO_ML = 473.18
    QUART_TO_ML = 946.36
    LIQUID_GALLON_TO_L = 3.76

    def __init__(self, value: float | int, unit: str = "fluid ounce"):
        self.value = value
        self.unit = unit.lower().rstrip("s")
    
    def to_metric(self) -> tuple[float. str]:
        '''Returns a tuple (metric value, label)'''
        if self.unit == "fluid ounce":
            return float(self.value * self.FLUID_OUNCE_TO_ML), "milliliters"
        elif self.unit == "cup":
            return float(self.value * self.CUP_TO_ML), "milliliters"
        elif self.unit == "liquid pint":
            return float(self.value * self.LIQUID_PINT_TO_ML), "milliliters"
        elif self.unit == "quart":
            return float(self.value * self.QUART_TO_ML), "milliliters"
        elif self.unit == "liquid gallon":
            return float(self.value * self.LIQUID_GALLON_TO_L), "liters"
        else:
            raise ValueError(f"Unit {self.unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the value'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        # Handle singular/plural for non-metric
        display_unit = self.unit
        if self.value != 1:
            if not self.unit.endswith("s"):
                display_unit += "s"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self.value} {display_unit} is {metric_value} {label}"

class Mass:
    # Conversion constants
    OUNCE_TO_G = 28.35
    POUND_TO_KG = 0.45
    STONE_TO_KG = 6.35
    TON_TO_KG = 1000

    def __init__(self, value: float | int, unit: str = "ounce"):
        self.value = value
        self.unit = unit.lower().rstrip("s")
    
    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (metric value, label)'''
        if self.unit == "ounce":
            return float(self.value * self.OUNCE_TO_G), "grams"
        elif self.unit == "pound":
            return float(self.value * self.POUND_TO_KG), "kilograms"
        elif self.unit == "stone":
            return float(self.value * self.STONE_TO_KG), "kilograms"
        elif self.unit == "ton":
            return float(self.value * self.TON_TO_KG), "kilograms"
        else:
            raise ValueError(f"Unit {self.unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the value'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        # Handle singular/plural for non-metric
        display_unit = self.unit
        if self.value != 1:
            display_unit += "s"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self.value} {display_unit} is {metric_value} {label}"

class Temperature:
    def __init__(self, value: float | int, unit: str = "fahrenheit"):
        self.value = value
        self.unit = unit.lower()
    
    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (metric value, label)'''
        if self.unit == "fahrenheit":
            return round(float(((self.value - 32) / 1.8) + 273.15), 2), "kelvin"
        elif self.unit == "celsius":
            return float(self.value + 273.15), "kelvin"
        else:
            raise ValueError(f"Unit {self.unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the value'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        return f"{self.value} {self.unit} is {metric_value} {label}"
class Distance:
    # Conversion constants
    INCH_TO_CM = 2.54
    FOOT_TO_CM = 30.48
    YARD_TO_CM = 91.44
    MILE_TO_KM = 1.61

    def __init__(self, value: float | int, unit: str = "inch"):
        self._value = value
        self._unit = unit.lower().rstrip("s")
    
    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (value, label)'''
        if self._unit == "inch":
            return round(float(self._value * self.INCH_TO_CM), 2), "centimeters"
        elif self._unit in ["foot", "feet"]:
            return round(float(self._value * self.FOOT_TO_CM), 2), "centimeters"
        elif self._unit == "yard":
            return round(float(self._value * self.YARD_TO_CM), 2), "centimeters"
        elif self._unit == "mile":
            return round((self._value * self.MILE_TO_KM), 2), "kilometers"
        else:
            raise ValueError(f"Unit {self._unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the output'''
        # Get the metric value and label
        metric_value, label = self.to_metric()
        # Handle singular/plural for non metric
        display_unit = self._unit
        if self._value != 1:
            if self._unit == "inch":
                display_unit = "inches"
            elif self._unit == "foot":
                display_unit = "feet"
            elif not self._unit == "feet" and not self._unit.endswith("s"):
                display_unit += "s"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self._value} {display_unit} is {metric_value:.2f} {label}"
 
class Area:
    # Coversion constants
    SQUARE_INCH_TO_SQUARE_CM = 6.45
    SQUARE_FOOT_TO_SQUARE_CM = 929
    SQUARE_YARD_TO_SQUARE_M = 0.84
    ACRE_TO_SQUARE_M = 4046.86
    SQUARE_MILE_TO_SQUARE_KM = 2.59

    def __init__(self, value: float | int, unit: str ="square inch"):
        self._value = value
        self._unit = unit.lower().rstrip("s")

    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (value, label)'''
        if self._unit == "square inch":
            return round(float(self._value * self.SQUARE_INCH_TO_SQUARE_CM),2), "square centimeters"
        elif self._unit in ["square foot", "square feet"]:
            return round(float(self._value * self.SQUARE_FOOT_TO_SQUARE_CM), 2), "square centimeters"
        elif self._unit == "square yard":
            return round(float(self._value * self.SQUARE_YARD_TO_SQUARE_M), 2), "square meters"
        elif self._unit == "acre":
            return round(float(self._value * self.ACRE_TO_SQUARE_M), 2), "square meters"
        elif self._unit == "square mile":
            return round(float(self._value * self.SQUARE_MILE_TO_SQUARE_KM), 2), "square kilometers"
        else:
            raise ValueError(f"Unit {self._unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the output'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        # Handle singular/plural for non-metric
        display_unit = self._unit
        if self._value != 1:
            if self._unit == "square inch":
                display_unit = "square inches"
            elif self._unit == "square foot":
                display_unit = "square feet"
            elif not self._unit == "square feet" and not self._unit.endswith("s"):
                display_unit += "s"
        
        if self._value == 1:
            if self._unit == "square feet":
                display_unit = "square foot"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self._value} {display_unit} is {metric_value:.2f} {label}"

class Volume:
    # Conversion constants
    CUBIC_INCH_TO_CUBIC_CM = 16.4
    CUBIC_FOOT_TO_CUBIC_CM = 0.028
    CUBIC_YARD_TO_CUBIC_CM = 0.76

    def __init__(self, value: float | int, unit: str = "cubic inch") -> None:
        self._value = value
        self._unit = unit.lower().rstrip("s")
    
    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (value, label)'''
        if self._unit == "cubic inch":
            return round(float(self._value * self.CUBIC_INCH_TO_CUBIC_CM), 2), "cubic centimeters"
        elif self._unit in ["cubic foot", "cubic feet"]:
            return round(float(self._value * self.CUBIC_FOOT_TO_CUBIC_CM), 2), "cubic centimeters"
        elif self._unit == "cubic yard":
            return round(float(self._value * self.CUBIC_YARD_TO_CUBIC_CM), 2), "cubic centimeters"
        else:
            raise ValueError(f"Unit {self._unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the output'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        # Handle singular/plural for non-metric
        display_unit = self._unit       
        if self._value != 1:
            if self._unit == "cubic inch":
                display_unit = "cubic inches"
            elif self._unit == "cubic foot":
                display_unit = "cubic feet"
            elif not self._unit == "cubic feet" and not self._unit.endswith("s"):
                display_unit += "s"

        if self._value == 1:
            if self._unit == "cubic feet":
                display_unit = "cubic foot"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self._value} {display_unit} is {metric_value:.2f} {label}"

class Capacity:
    # Conversion constants
    FLUID_OUNCE_TO_ML = 29.57
    CUP_TO_ML = 236.59
    LIQUID_PINT_TO_ML = 473.18
    QUART_TO_ML = 946.36
    LIQUID_GALLON_TO_L = 3.76

    def __init__(self, value: float | int, unit: str = "fluid ounce"):
        self._value = value
        self._unit = unit.lower().rstrip("s")
    
    def to_metric(self) -> tuple[float. str]:
        '''Returns a tuple (value, label)'''
        if self._unit == "fluid ounce":
            return round(float(self._value * self.FLUID_OUNCE_TO_ML), 2), "milliliters"
        elif self._unit == "cup":
            return round(float(self._value * self.CUP_TO_ML), 2), "milliliters"
        elif self._unit == "liquid pint":
            return round(float(self._value * self.LIQUID_PINT_TO_ML), 2), "milliliters"
        elif self._unit == "quart":
            return round(float(self._value * self.QUART_TO_ML), 2), "milliliters"
        elif self._unit == "liquid gallon":
            return round(float(self._value * self.LIQUID_GALLON_TO_L), 2), "liters"
        else:
            raise ValueError(f"Unit {self._unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the output'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        # Handle singular/plural for non-metric
        display_unit = self._unit
        if self._value != 1:
            if not self._unit.endswith("s"):
                display_unit += "s"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self._value} {display_unit} is {metric_value:.2f} {label}"

class Mass:
    # Conversion constants
    OUNCE_TO_G = 28.35
    POUND_TO_KG = 0.45
    STONE_TO_KG = 6.35
    TON_TO_KG = 1000

    def __init__(self, value: float | int, unit: str = "ounce"):
        self._value = value
        self._unit = unit.lower().rstrip("s")
    
    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (value, label)'''
        if self._unit == "ounce":
            return round(float(self._value * self.OUNCE_TO_G), 2), "grams"
        elif self._unit == "pound":
            return round(float(self._value * self.POUND_TO_KG), 2), "kilograms"
        elif self._unit == "stone":
            return round(float(self._value * self.STONE_TO_KG), 2), "kilograms"
        elif self._unit == "ton":
            return round(float(self._value * self.TON_TO_KG), 2), "kilograms"
        else:
            raise ValueError(f"Unit {self._unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the output'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        # Handle singular/plural for non-metric
        display_unit = self._unit
        if self._value != 1:
            if not self._unit.endswith("s"):
                display_unit += "s"
        
        # Handle singular/plural for metric
        if metric_value == 1:
            label = label.rstrip("s")
        
        return f"{self._value} {display_unit} is {metric_value:.2f} {label}"

class Temperature:
    def __init__(self, value: float | int, unit: str = "fahrenheit"):
        self._value = value
        self._unit = unit.lower()
    
    def to_metric(self) -> tuple[float, str]:
        '''Returns a tuple (value, label)'''
        if self._unit == "fahrenheit":
            return round(float(((self._value - 32) / 1.8) + 273.15), 2), "kelvin"
        elif self._unit == "celsius":
            return round(float(self._value + 273.15), 2), "kelvin"
        else:
            raise ValueError(f"Unit {self._unit} is not supported.")
    
    def __str__(self) -> str:
        '''Display the output'''
        # Get the metric value and label
        metric_value, label = self.to_metric()

        return f"{self._value} {self._unit} is {metric_value:.2f} {label}"
class DrinkConverter:
    def __init__(self):
        self.conversions = {
            'ml': 1,
            'l': 1000,
            'oz': 29.5735,
            'cup': 236.588,
            'pint': 473.176,
            'quart': 946.353,
            'gallon': 3785.41
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversions or to_unit not in self.conversions:
            return None

        # Convert the value to ml first
        value_in_ml = value * self.conversions[from_unit]

        # Convert from ml to the target unit
        converted_value = value_in_ml / self.conversions[to_unit]

        return converted_value
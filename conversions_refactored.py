''' In the event of unit conversion from distance to temperature or vice versa, the program will raise this exception
'''
class ConversionNotPossibleException(Exception):
    def __init__(self, message):
        self.message = "Conversion is not possible due to unit incompatibility."

def convert(fromUnit, toUnit, value):

    # Setting up boolean variables in order to test if units are compatible
    fromIsTempUnit = False
    fromIsDistUnit = False
    toIsTempUnit = False
    toIsDistUnit = False

    # Sets boolean values based on fromUnit and toUnit
    if fromUnit == "Fahrenheit" or fromUnit == "Kelvin" or fromUnit == "Celcius":
        fromIsTempUnit = True
    if fromUnit == "Meters" or fromUnit == "Yards" or fromUnit == "Miles":
        fromIsDistUnit = True
    if toUnit == "Fahrenheit" or toUnit == "Kelvin" or toUnit == "Celcius":
        toIsTempUnit = True
    if toUnit == "Meters" or toUnit == "Yards" or toUnit == "Miles":
        toIsDistUnit = True


    if fromIsTempUnit and toIsTempUnit: # fromUnit and toUnit must be the same for unit compatibility
        # celcius is the central unit conversion since from celcius we can obtain the other two units simply through one operation
        celcius = value
        if fromUnit == "Kelvin":
            celcius = value - 273.15
        if fromUnit == "Fahrenheit":
            celcius = ((value-32.0)*(5.0/9.0))

        # based on the celcius, we can easily obtain these values for kelvin and fahrenheit
        kelvin = celcius + 273.15
        fahrenheit = (celcius*(9.0/5.0))+32

        # return the toUnit
        if toUnit == "Fahrenheit": return fahrenheit
        if toUnit == "Celcius": return celcius
        if toUnit == "Kelvin": return kelvin

    elif fromIsDistUnit and toIsDistUnit: # fromUnit and toUnit must be the same for unit compatibility
        # miles is the central unit conversion since from miles we can obtain the other two units simply through one operation
        miles = value
        if fromUnit == "Yards":
            miles = value/1760.0
        if fromUnit == "Meters":
            miles = value/1609.344

        # based on the miles, we can easily obtain these values for yards and meters
        yards = miles*1760.0
        meters = miles*1609.344

        # return the toUnit
        if toUnit == "Miles": return miles
        if toUnit == "Yards": return yards
        if toUnit == "Meters": return meters

    else:   # in the event that both units are not distances or temperatures, raise this exception
        raise ConversionNotPossibleException("Conversion is not possible due to unit incompatibility.")

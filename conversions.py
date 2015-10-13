
''' Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins '''
def convertCelciusToKelvin(celcius):
    return round(celcius+273.15, 10)


''' Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit '''
def convertCelciusToFahrenheit(celcius):
    return round((celcius*(9.0/5.0)) + 32, 10)


''' Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celcius '''
def convertFahrenheitToCelcius(fahrenheit):
    return round(((fahrenheit-32)*(5.0/9.0)), 10)


''' Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvin '''
def convertFahrenheitToKelvin(fahrenheit):
    return round(((fahrenheit-32)*(5.0/9.0))+273.15, 10)


''' Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celcius '''
def convertKelvinToCelcius(kelvin):
    return round(kelvin-273.15, 10)


''' Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit '''
def convertKelvinToFahrenheit(kelvin):
    return round((((kelvin-273.15)* (9.0/5.0))+32), 10)



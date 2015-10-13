import conversions_refactored
import unittest
import random

''' Checks that all temperature conversions in list are working '''
class KnownTemperatureValues(unittest.TestCase):
    knownTemperatureValues = ( (0.0, 273.15, 32.0),
                    (300.0, 573.15, 572.0),
                    (25.49, 298.64, 77.882),
                    (200, 473.15, 392),
                    (150.00, 423.15, 302.00),
                    (-220.00, 53.15, -364.00),
                    (-40.0, 233.15, -40.0),
                    )

    # Works by checking all conversions for each row in knownTemperatureValues
    def testConvert(self):
        print "\nNow testing convert() function with temperature:"

        # iterate for the entire knownTemperatureValues contents
        for i in range(0,len(self.knownTemperatureValues)):
            print "   TESTING ROUND %i" % (i+1)

            # assertAlmostEqual is used for floats due to the inexact calcuations of floats

            # conversion of celcius to kelvin
            ck = conversions_refactored.convert("Celcius", "Kelvin", self.knownTemperatureValues[i][0])
            # comparison of the kelvin result to the expected value in knownTemperatureValues
            self.assertAlmostEqual(ck, self.knownTemperatureValues[i][1], 4)
            print "      Checking %f celcius is converted to %f kelvin; actual: %f" % (self.knownTemperatureValues[i][0], self.knownTemperatureValues[i][1], ck)

            # conversion of celcius to fahrenheit
            cf = conversions_refactored.convert("Celcius", "Fahrenheit", self.knownTemperatureValues[i][0])
            # comparison of the fahrenheit result to the expected value in knownTemperatureValues
            self.assertAlmostEqual(cf, self.knownTemperatureValues[i][2], 4)
            print "      Checking %f celcius is converted to %f fahrenheit; actual: %f" % (self.knownTemperatureValues[i][0], self.knownTemperatureValues[i][2], cf)

            # conversion of kelvin to celcius
            kc = conversions_refactored.convert("Kelvin", "Celcius", self.knownTemperatureValues[i][1])
            # comparison of the celcius result to the expected value in knownTemperatureValues
            self.assertAlmostEqual(kc, self.knownTemperatureValues[i][0], 4)
            print "      Checking %f kelvin is converted to %f celcius; actual: %f" % (self.knownTemperatureValues[i][1], self.knownTemperatureValues[i][0], kc)

            # conversion of kelvin to fahrenheit
            kf = conversions_refactored.convert("Kelvin", "Fahrenheit", self.knownTemperatureValues[i][1])
            # comparison of the fahrenheit result to the expected value in knownTemperatureValues
            self.assertAlmostEqual(kf, self.knownTemperatureValues[i][2], 4)
            print "      Checking %f kelvin is converted to %f fahrenheit; actual: %f" % (self.knownTemperatureValues[i][1], self.knownTemperatureValues[i][2], kf)

            # conversion of fahrenheit to celcius
            fc = conversions_refactored.convert("Fahrenheit", "Celcius", self.knownTemperatureValues[i][2])
            # comparison of the celcius result to the expected value in knownTemperatureValues
            self.assertAlmostEqual(fc, self.knownTemperatureValues[i][0], 4)
            print "      Checking %f fahrenheit is converted to %f celcius; actual: %f" % (self.knownTemperatureValues[i][2], self.knownTemperatureValues[i][0], fc)

            # conversion of fahrenheit to kelvin
            fk = conversions_refactored.convert("Fahrenheit", "Kelvin", self.knownTemperatureValues[i][2])
            # comparison of the kelvin result to the expected value in knownTemperatureValues
            self.assertAlmostEqual(fk, self.knownTemperatureValues[i][1], 4)
            print "      Checking %f fahrenheit is converted to %f kelvin; actual: %f" % (self.knownTemperatureValues[i][2], self.knownTemperatureValues[i][1], fk)
            print ""



''' Checks that all distance conversions in list are working '''
class KnownDistanceValues(unittest.TestCase):
    knownDistanceValues = ( (0, 0, 0),
                            (1, 1760, 1609.344),
                            (15, 26400, 24140.16),
                            (0.0006213712, 1.0936133, 1),
                            (0.0005682, 1, 0.91440) )

    # Works by checking all conversions for each row in knownDistanceValues
    def testConvert(self):
        print "\nNow testing convert() function with distance:"
        for i in range(0,len(self.knownDistanceValues)):
            print "   TESTING ROUND %i" % (i+1)

            # assertAlmostEqual is used for floats due to the inexact calcuations of floats

            # conversion of miles to yards
            iy = conversions_refactored.convert("Miles", "Yards", self.knownDistanceValues[i][0])
            # comparison of the yards result to the expected value in knownTemperatureValues
            self.assertAlmostEqual(iy, self.knownDistanceValues[i][1], 4)
            print "      Checking %f miles is converted to %f yards; actual: %f" % (self.knownDistanceValues[i][0], self.knownDistanceValues[i][1], iy)

            # conversion of miles to meters
            ie = conversions_refactored.convert("Miles", "Meters", self.knownDistanceValues[i][0])
            # comparison of the meters result to the expected value in knownTemperatureValues)
            self.assertAlmostEqual(ie, self.knownDistanceValues[i][2], 4)
            print "      Checking %f miles is converted to %f meters; actual: %f" % (self.knownDistanceValues[i][0], self.knownDistanceValues[i][2], ie)

            # conversion of yards to miles
            yi = conversions_refactored.convert("Yards", "Miles", self.knownDistanceValues[i][1])
            # comparison of the miles result to the expected value in knownTemperatureValues)
            self.assertAlmostEqual(yi, self.knownDistanceValues[i][0], 4)
            print "      Checking %f yards is converted to %f miles; actual: %f" % (self.knownDistanceValues[i][1], self.knownDistanceValues[i][0], yi)

            # conversion of yards to meters
            ye = conversions_refactored.convert("Yards", "Meters", self.knownDistanceValues[i][1])
            # comparison of the meters result to the expected value in knownTemperatureValues)
            self.assertAlmostEqual(ye, self.knownDistanceValues[i][2], 4)
            print "      Checking %f yards is converted to %f meters; actual: %f" % (self.knownDistanceValues[i][1], self.knownDistanceValues[i][2], ye)

            # conversion of meters to miles
            ei = conversions_refactored.convert("Meters", "Miles", self.knownDistanceValues[i][2])
            # comparison of the miles result to the expected value in knownTemperatureValues)
            self.assertAlmostEqual(ei, self.knownDistanceValues[i][0], 4)
            print "      Checking %f meters is converted to %f miles; actual: %f" % (self.knownDistanceValues[i][2], self.knownDistanceValues[i][0], ei)

            # conversion of meters to yards
            ey = conversions_refactored.convert("Meters", "Yards", self.knownDistanceValues[i][2])
            # comparison of the yards result to the expected value in knownTemperatureValues)
            self.assertAlmostEqual(ey, self.knownDistanceValues[i][1], 4)
            print "      Checking %f meters is converted to %f yards; actual: %f" % (self.knownDistanceValues[i][2], self.knownDistanceValues[i][1], ey)
            print ""


''' Checks that converting from one unit to itself returns the same value for all units '''
class SanityCheck(unittest.TestCase):
    def testSanity(self):
        print "\nNow testing sanity of convert():"
        for i in range(0, 5):
            print "   TESTING ROUND %i" % (i+1)

            # assertAlmostEqual is used for floats due to the inexact calcuations of floats

            # create a random number use for conversion of celcius
            celciusInput = random.random()*100
            # convert celcius to celcius for sanity check
            celciusConverted = conversions_refactored.convert("Celcius", "Celcius", celciusInput)
            self.assertAlmostEqual(celciusInput, celciusConverted, 4)
            print "      %f Celcius converted to Celcius is %f" % (celciusInput, celciusConverted)

            # create a random number use for conversion of kelvin
            kelvinInput = random.random()*1000
            # convert kelvin to kelvin for sanity check
            kelvinConverted = conversions_refactored.convert("Kelvin", "Kelvin", kelvinInput)
            self.assertAlmostEqual(kelvinInput, kelvinConverted, 4)
            print "      %f Kelvin converted to Kelvin is %f" % (kelvinInput, kelvinConverted)

            # create a random number use for conversion of fahrenheit
            fahrenheitInput = random.random()*100
            # convert fahrenheit to fahrenheit for sanity check
            fahrenheitConverted = conversions_refactored.convert("Fahrenheit", "Fahrenheit", fahrenheitInput)
            self.assertAlmostEqual(fahrenheitInput, fahrenheitConverted, 4)
            print "      %f Fahrenheit converted to Fahrenheit is %f" % (fahrenheitInput, fahrenheitConverted)

            # create a random number use for conversion of meters
            metersInput = random.random()*100
            # convert meters to meters for sanity check
            metersConverted = conversions_refactored.convert("Meters", "Meters", metersInput)
            self.assertAlmostEqual(metersInput, metersConverted, 4)
            print "      %f Meters converted to Meters is %f" % (metersInput, metersConverted)

            # create a random number use for conversion of yards
            yardsInput = random.random()*100
            # convert yards to yards for sanity check
            yardsConverted = conversions_refactored.convert("Yards", "Yards", yardsInput)
            self.assertAlmostEqual(yardsInput, yardsConverted, 4)
            print "      %f Yards converted to Yards is %f" % (yardsInput, yardsConverted)

            # create a random number use for conversion of miles
            milesInput = random.random()*100
            # convert miles to miles for sanity check
            milesConverted = conversions_refactored.convert("Miles", "Miles", milesInput)
            self.assertAlmostEqual(milesInput, milesConverted, 4)
            print "      %f Miles converted to Miles is %f" % (milesInput, milesConverted)
            print ""


''' Checks that converting from incompatible units will raise a ConversionNotPossibleexception
    Will attempt a distance unit to temperature conversion and reverse
'''
class IncompatibleUnits(unittest.TestCase):
    def testIncompatibleUnits(self):
        print "\nNow testing all incompatible units raises ConversionNotPossibleException:"

        print "   Checking if Miles-Celcius raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Miles", "Celcius", 0)

        print "   Checking if Miles-Kelvin raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Miles", "Kelvin", 0)

        print "   Checking if Miles-Fahrenheit raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Miles", "Fahrenheit", 0)

        print "   Checking if Yards-Celcius raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Yards", "Celcius", 0)

        print "   Checking if Yards-Kelvin raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Yards", "Kelvin", 0)

        print "   Checking if Yards-Fahrenheit raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Yards", "Fahrenheit", 0)

        print "   Checking if Meters-Celcius raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Meters", "Celcius", 0)

        print "   Checking if Meters-Kelvin raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Meters", "Kelvin", 0)

        print "   Checking if Meters-Fahrenheit raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Meters", "Fahrenheit", 0)

        print "   Checking if Celcius-Miles raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Celcius", "Miles", 0)

        print "   Checking if Celcius-Yards raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Celcius", "Yards", 0)

        print "   Checking if Celcius-Meters raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Celcius", "Meters", 0)

        print "   Checking if Kelvin-Miles raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Kelvin", "Miles", 0)

        print "   Checking if Kelvin-Yards raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Kelvin", "Yards", 0)

        print "   Checking if Kelvin-Meters raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Kelvin", "Meters", 0)

        print "   Checking if Fahrenheit-Miles raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Fahrenheit", "Miles", 0)

        print "   Checking if Fehrenheit-Yards raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Fahrenheit", "Yards", 0)

        print "   Checking if Fehrenheit-Meters raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert, "Fahrenheit", "Meters", 0)



if __name__ == "__main__":
    unittest.main()
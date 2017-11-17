#CTI-110
#M6T1-Kilometer Converter
#Jaime Rodriguezmiller
#Novemeber 12, 2017

# this asks the user to enter a distance and stores it
def askUserForKilometers():
    userKilometers = float( input( "Please enter the distance" + \
                                   " in kilometers: "))
    return userKilometers
# converst kilometers to miles with a mathmatical equation and stores the miles
def convertKilometersToMiles( userKilometers ):
    miles = userKilometers * 0.6214
    return miles
# calls the information the user typed and then calls the formula with the user
# info to convert kilometers to miles and prints the results to the user
def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles = convertKilometersToMiles( userKilometersTyped )

    
    print( userKilometersTyped, "kilometers converted to miles is", \
           format( convertedMiles, ".2f"), "miles" )
main()    

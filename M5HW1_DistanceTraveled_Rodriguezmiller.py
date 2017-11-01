#CTI-110
#M5HW1:Distance Traveled
#Jaime Rodriguezmiller
#October 22, 2017

#Value to the speed and time variable.
vehicleSpeed = float( input('What is the speed of the vehicle: '))
timeTraveled = int( input('How many hours has it traveled?: '))

#Get the distance traveled.
print('Hour','Distance Traveled')
for currentHour in range( 1, timeTraveled + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print( currentHour, '\t', distanceTraveled )
    

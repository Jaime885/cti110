#CTI-110
#M5HW2:Running Total
#Jaime Rodriguezmiller
#October 22, 2017

total=0  
while total >= (0):  #while loop that lets you inptu number
    newNumber = int(input('Enter a number: '))
    if newNumber < (0):  #if statment that breaks the while loo if - input
        break
    total = newNumber + total  #total is calculated even if while is interrupted but will not add - number   
        
print('The total is: ',total)
    


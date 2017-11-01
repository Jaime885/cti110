#CTI-110
#M5HW3:Factorial
#Jaime Rodriguezmiller
#October 22, 2017

#Write a program that asks the user for a nonnegative integer and then uses a
#loop to calculate the factorial of that number. Display the factorial 
#Here is an example program run.
#(The user’s entries, after the “?”, are listed in bold.)
#Enter a nonnegative integer? 4
#The factorial of 4 is 24

userInteger = int( input('Enter a non-negative integer: '))

while userInteger < 1:
    userInteger = int( input('Please enter a positive number please: '))

factorial = 1

for currentNumber in range( 1, userInteger +1):
    factorial = factorial * currentNumber

print()
print('The factorial of', userInteger, 'is', factorial )



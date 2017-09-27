#CTI-110
#M3HW1-Age Classifier
#Jaime Rodriguezmiller
#September 24, 2017

def main():
    #This program asks the user to enter their age.  The return displays a
    #message indicating whether the person is an infant, a child, a teenager
    #or and adult.

    Age = eval(input('Enter Age:  '))

    if 20 <= Age <= 150:
      print('Your are an Adult')
    elif 13 <= Age <= 19:
      print('You are a teenager')
    elif 2 <= Age <= 12:
      print('You are a child')
    elif 0 <= 1:
      print('You are an infant')


main()

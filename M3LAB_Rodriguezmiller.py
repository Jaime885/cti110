#CTI-110
#M3LAB-
#Jaime Rodriguezmiller
#September 24, 2017

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    
    
    

    
    score = eval(input('Enter grade: '))

    if 90 <= score <=100:
      print('Your grade is: A')
      
    elif 80 <= score <=89:
      print('Your grade is: B')
    elif 70 <= score <=79:
      print('Your grade is: C')
    elif 60 <= score <=69: 
      print('Your grade is: D')
    elif 50 <= score <=59:
      print('Your grade is: F')
    elif 0 <= score <=49:
      print('Your grade is: F')
# program start

main()

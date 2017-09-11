#CTI-110
#M2HW2- Tip Tax Total
#Jaime Rodriguezmiller
#September 9, 2017

#Cost of a meal purchased at a restaurant
foodcost = float( input("Please enter the cost of the food: "))
#Calculates the amount of tip
tip = 0.18 * foodcost
#Calculates the total sales tax
SalesTax=0.07*foodcost
#Calculates the total amount food+tip+tax
total=foodcost+tip+SalesTax

print("Meal: $",format(foodcost,",.2f" ))
print("Sales Tax: $",format(SalesTax,",.2f"))
print("Tip: $",format(tip,",.2f"))
print("Total: $",format(foodcost+tip+SalesTax,",.2f"))





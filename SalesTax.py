#Prompt the use to enter the square feet of wall to be painted and store in the variable named wall_space

wall_space = float(input("Enter square feet of wall space: "))

#prompt the user to enter a price of paint per gallon
paint_price_per_gallon = float(input("Enter price of paint per gallon: "))

#using if statement to test a condition that for every 115 square feet of wall sapace execute the statements in the if block,
#if otherwise execute the statements in the else block
if wall_space == 115:
    paint_required = 1
    hours_for_labor = 8
    labor_charges = hours_for_labor*20
    print("Paint requied=", paint_required)
    print("Labor Charges=", labor_charges)
else:
    paint_required = (wall_space*1)/115
    hours_for_labor = (wall_space*8)/115
    print("The number of gallons of paint required", round(paint_required))
    print("The hours of labor required:", round(hours_for_labor))
    paint_cost = paint_required*paint_price_per_gallon
    print("The cost of paint:", round(paint_cost))
    labor_charges = hours_for_labor*20
    print("The labor charges:", round(labor_charges))
    total_cost = paint_cost+labor_charges
    print("The total cost of paint job:", round(total_cost))

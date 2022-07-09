#A program that gets today's date and uses today's date to get the name of the day of the
#week in short form with first letter capitalized
#Use if statements to determine today's fare

#importing python built-in modules for getting date and days of the week from calendar 
import datetime
from datetime import date
import calendar

#craeting variables to hold today's date and day
date = date.today()
Day = date.weekday()

#creating a function that uses if statements to determine today's fare 
def Get_Fare():
    if Day >= 0 and Day <= 4:
        Fare = 100
    elif Day == 5:
        Fare = 60
    elif Day == 6:
        Fare = 80
    else:
        print("Invalid day, enter another valid day.")
        return(Fare)
    #Printing fare
    print("Fare:", Fare)

#Printing The Date i.e Today's date and corresponding Day
print("Date:", date)
print("Day:", date.strftime("%a").capitalize())

#Calling Get_Fare funtion to print out today's fare
Get_Fare()

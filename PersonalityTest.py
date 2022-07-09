#prompt the user to enter the number of books he/she has purchased

Number_of_books=int(input("Enter number of books purchased: "))

#Use a if else condition to test the following condtions and print the reults for every true condition
if Number_of_books==0:
    points_earned=0
elif Number_of_books==1:
    points_earned=6
elif Number_of_books==2:
    points_earned=16
elif Number_of_books==3:
    points_earned=32
elif Number_of_books>=4:
    points_earned=60
else:
    print("Enter a positive integer.")
 
print("Number of points awarded is:", points_earned)
    
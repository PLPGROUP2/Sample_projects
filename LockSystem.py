from datetime import datetime

def door():
    trials = 2
    
    #preset password that will be used to gain access to the door
    
    Door_password = "PLP2022"  
    
    #initiate a boolean variable to use in testing the passwords                                   
    bl = True
    while bl:
        user_password = input("Enter your password: ")
        
        #Double check the use_password again Door_password to see if they match
        if Door_password == user_password:                       
            print("Welcome")
            
            #nce the password is accepted, the boolean variable becomes false hence program breaks out of while loop
            bl = False                             
        elif trials == 0:
            
            return 0
        else:

            print(f"Wrong password\nyou have {trials} remaining trials")
            trials -=1
if door()==0:
    print("You have entered the wrong password 3 times.")
else:
    
    #Create a lis of commands to use on the door
    
    command_list = ["Open","Close","Quit"]                 
    bol = True
    count = 0
    while bol:
        val = True
        while val:
            command = input("Enter your command: ")
            
            #Use if condition to check if command issued is part of the commands suite
            
            if command in command_list:                 
                val = False
            else:
                print("Invalid input")
                print("Use one of the following commands!!:",command_list)
        if count == 0 and command == "Open":
            open_date=datetime.now()      #datetime.now records the first time oor is opened              
            print("Door last open at ",open_date)       
            print("The door is now open")
            count += 1
        elif count!= 0 and command == "Open":
            print("Door last open at ",open_date)
            print("The door is already open!")             #since count variable is more than zero, it means the door was already opened
        elif count!=0 and command == "Close":
            close_date=datetime.now()                      #datetime.now records last time door was closed
            print("Door last closed at ",close_date)
            print("The door is now locked")
            count = 0                                      #reset the count to zero since door is now closed
        elif count == 0 and command == "Close":
            print("The door is already locked!")           #since count variable is more than  zero, it means the door was already closed
        else:
            print("Goodbye!")
            bol = False


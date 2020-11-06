# Drone Control Py by Drone Team 2-1
# Sprint Week Project #1, November 2020
# Python program for sending user commands to the Tello Drone

import tello_abridged

# TODO: Track if drone is in the air or not

#Connect to the drone
#t = tello_abridged.Tello()
#t.connect_and_initialize()

# List of valid commands the tello will accept
# Takeoff and land are in their own list because they don't need arguments
standard_commands = ["up","down","left","right","forward","back","cw","ccw","flip"]
noarg_commands = ["takeoff","land"]


while True:
    
    # Start the main loop and run until the user quits
    # TODO: Setup input validation
    print("--* Drone Control Py *--")
    while True:
        
        # Print the list of commands and wait for the user's input
        print("Available Commands: {} {}".format(noarg_commands,standard_commands)) 
        user_command = input("Command: ")
        
        # Make sure the user enters a valid command by checking against a list of commands
        if user_command.lower() in standard_commands or user_command.lower() in noarg_commands:
            break
        else:
            print("Please input a valid command.")

    # We don't need to prompt user for a second value if it's taking off or landing
    if user_command.lower() not in noarg_commands:
        # Second input to ask for a number value in centimeters
        # TODO: Setup input validation
        # Validation for most commands must be between 20 and 500
        # Validation for cw and ccw comands must be between 1 and 360
        if user_command == "cw" or user_command == "ccw":
            
            while True:
                user_num = int(input("Degrees: "))
                
                if user_num >= 1 and user_num <= 360:
                    break
                else:
                    print("Please enter a number between 1 and 360")
        
        elif user_command == "flip":
            user_num = input("Direction (l,r,f): ")
                    
        else:
                
            while True:
                user_num = int(input("Centimeters: "))
                
                if user_num >= 2 and user_num <= 500:
                    break
                else:
                    print("Please enter a number between 20 and 500")
        
    # Make sure we have a condition to quit the program.
    # TODO: Look into issue with height & cm travelled
    # This section will handle the user's commands and send them to the drone using t.send_command
    # 
    # If the command is a takeoff or landing, it will send a command without an argument
    if user_command.lower() in noarg_commands:
        t.send_command(user_command.lower())
        
    # If the command is any of the other standard commands, it will send command + argument
    elif user_command.lower() in standard_commands:
        # Creating a new variable so we can combine user_command and user_num into a single string
        command = user_command.lower() + " " + str(user_num)
        # Then we pass that combined command to the tello
        t.send_command(command)

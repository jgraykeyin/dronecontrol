import tello_abridged

#Connect to the drone
t = tello_abridged.Tello()
t.connect_and_initialize()

# List of valid commands the tello will accept
# TODO: enter all the commands into this list
valid_commands = []

# Start a loop here to start taking inputs
while True:
    
    # First input to ask for the command.
    # TODO: Setup input validation
    # We'll need to make sure it's one of the valid commands, ie takeoff
    # Perhaps make a list of commands and check against that?
    user_command = input("Command: ")

    # We don't need to prompt user for a second value if it's taking off
    if user_command.lower() != "takeoff":
        # Second input to ask for a number value in centimeters
        # TODO: Setup input validation
        # Validation for most commands must be between 20 and 500
        # Validation for cw and ccw comands must be between 1 and 360
        user_cm = int(input("Centimeters: "))
        
    # Setup if statements to handle user commands.
    # Make sure we have a condition to quit the program.
    # Commands we must support: takeoff, up, down, left, right, forward, back, cw, ccw, land
    # 
    if user_command.lower() == "takeoff":
        t.send_command(user_command.lower())
        
    elif user_command.lower() == "up":
        # Creating a new variable so we can combine user_command and user_cm into a single string
        command = user_command.lower() + " " + str(user_cm)
        # Then we pass that combined command to the tello
        t.send_command(command)
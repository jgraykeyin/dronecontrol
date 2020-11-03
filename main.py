import tello_abridged

#Connect to the drone
t = tello_abridged.Tello()
t.connect_and_initialize()

# Start a loop here to start taking inputs
while True:
    
    # First input to ask for the command.
    # TODO: Setup input validation
    user_command = input("Command: ")

    # We don't need to prompt user for a second value if it's taking off
    if user_command.lower() != "takeoff":
        # Second input to ask for a number value in centimeters
        # TODO: Setup input validation
        user_cm = int(input("Centimeters: "))
        
    # Setup if statements to handle user commands.
    # Make sure we have a condition to quit the program.
    if user_command.lower() == "takeoff":
        t.send_command(user_command.lower())
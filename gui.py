import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [  [sg.Text("Drone Control")],
            [sg.Button("Takeoff"),sg.Button("Land")],
            [sg.Button("Up"),sg.Button("Down")],
            [sg.Button("Left"),sg.Button("Right")]]

# Create the window
window = sg.Window('Drone Control',layout)

# Event loop to process events and get inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    print("You entered:", values[0])

window.close()
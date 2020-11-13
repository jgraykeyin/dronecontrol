# Drone Control Py by Drone Team 2-1
# Sprint Week Project #1, November 2020
# Python program for sending user commands to the Tello Drone

import tello_abridged
import PySimpleGUI as sg

#Connect to the drone
t = tello_abridged.Tello()
t.connect_and_initialize()

sg.theme("DarkAmber")
# Create the layout for the GUI 
layout = [ [sg.Button('Takeoff',font=("Helvetica", 18))],
           [sg.Button('Land',font=("Helvetica", 18))],
           [sg.Button('Cancel',font=("Helvetica",18))]  ]

# Create the window
window = sg.Window('Drone Control',layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    elif event == 'Takeoff':
        t.send_command('takeoff')

    elif event == 'Land':
        t.send_command('land')


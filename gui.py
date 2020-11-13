# Drone Control Py by Drone Team 2-1
# Sprint Week Project #1 Bonus, November 2020
# GUI Python program for sending user commands to the Tello Drone

import tello_abridged
import PySimpleGUI as sg
import speech_recognition as sr


#Connect to the drone
t = tello_abridged.Tello()
t.connect_and_initialize()

# Initialize the Speech Recognition for listening
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

sg.theme("DarkAmber")
# Create the layout for the GUI 
layout = [ [sg.Button('Takeoff',font=("Helvetica", 18),size=(10,1))],
           [sg.Button('Land',font=("Helvetica", 18),size=(10,1))],
           [sg.Text('Parameter in cm: ',font=("Helvetica", 18)), sg.InputText()],
           [sg.Button('Up',font=("Helvetica", 18),size=(10,1)),sg.Button('Down',font=("Helvetica", 18),size=(10,1))],
           [sg.Button('Left',font=("Helvetica", 18),size=(10,1)),sg.Button('Right',font=("Helvetica", 18),size=(10,1))],
           [sg.Button('Speak',font=("Helvetica", 18))] ]

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
    
    elif event == 'Up':
        t.send_command("up {}".format(values[0]))

    elif event == 'Down':
        t.send_command("down {}".format(values[0]))

    elif event == 'Left':
        t.send_command("left {}".format(values[0]))

    elif event == 'Right':
        t.send_command("right {}".format(values[0]))

    elif event == 'Speak':
        # Listen to what the smart device says and return the output
        print("Listening...")
        with mic as source:
            audio = r.listen(source,phrase_time_limit=3)

        try:
            command = r.recognize_google(audio)
        except sr.UnknownValueError:
            command = "Unable to understand audio."
        except sr.RequestError as e:
            command = "Error {0}".format(e)

        t.send_command(command)


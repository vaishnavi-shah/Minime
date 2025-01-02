import tkinter as tk
import speech_recognition as sr
import pyttsx3
import os
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)
            process_command(command)
    except Exception as e:
        print("Sorry, I could not understand the command.")
        speak("Sorry, I could not understand that.")

def process_command(command):
    if 'open website' in command:
        speak("Opening website...")
        webbrowser.open('https://www.google.com')
    elif 'open notepad' in command:
        speak("Opening Notepad...")
        os.system('notepad')
    elif 'exit' in command:
        speak("Goodbye!")
        root.quit()
    else:
        speak("I did not understand that command.")

# Set up the main GUI window
root = tk.Tk()
root.title("Jarvis Assistant")

# Create a label
label = tk.Label(root, text="Click the button to start voice command", font=("Arial", 14))
label.pack(pady=10)

# Button to activate listening
listen_button = tk.Button(root, text="Listen", font=("Arial", 14), command=listen)
listen_button.pack(pady=10)

# Start the GUI loop
root.mainloop()

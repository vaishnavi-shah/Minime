import tkinter as tk
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyautogui
import os
import requests
import time
from plyer import notification
import random
import pyjokes

# Initialize the speech engine for text-to-speech
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
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            process_command(command)
    except Exception as e:
        print("Sorry, I couldn't understand.")
        speak("Sorry, I couldn't understand that.")

def process_command(command):
    if 'open notepad' in command:
        os.system('notepad')
        speak("Opening Notepad.")
    elif 'open whatsapp' in command:
        os.system('WhatsApp')
        speak("opening WhatsApp.")
    elif 'open camera' in command:
        os.system('camera')
        speak("opening Camera.")
    
    elif 'search' in command:
        query = command.replace('search', '').strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on Google.")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif 'weather' in command:
        city = "Mumbai"  # You can modify this to take city as input
        weather_api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
        weather_data = requests.get(weather_api).json()
        if weather_data["cod"] == "404":
            speak("City not found.")
        else:
            main = weather_data["main"]
            weather_desc = weather_data["weather"][0]["description"]
            speak(f"The temperature in {city} is {main['temp']} Kelvin with {weather_desc}.")
    elif 'set reminder' in command:
        reminder_time = 10  # Example: Set reminder for 10 seconds
        reminder_message = "Meeting in 10 minutes!"
        set_reminder(reminder_time, reminder_message)
    elif 'exit' in command:
        speak("Goodbye!")
        root.quit()
    else:
        speak("Sorry, I didn't catch that.")

def set_reminder(time_in_seconds, message):
    time.sleep(time_in_seconds)
    notification.notify(
        title="Reminder",
        message=message,
        timeout=10
    )
    speak(f"Reminder set! I will notify you in {time_in_seconds // 60} minutes.")

# GUI Setup using Tkinter
root = tk.Tk()
root.title("Minime")
root.geometry("600x400")
root.config(bg="#282828")

status_label = tk.Label(root, text="Click below to start listening", font=("Arial", 16), bg="#282828", fg="white")
status_label.pack(pady=20)

listen_button = tk.Button(root, text="Listen", font=("Arial", 14), width=20, height=2, command=listen, bg="#4CAF50", fg="white")
listen_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), width=20, height=2, command=root.quit, bg="#f44336", fg="white")
exit_button.pack(pady=20)

# Run the GUI
root.mainloop()

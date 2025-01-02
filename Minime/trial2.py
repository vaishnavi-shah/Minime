import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import os
from plyer import notification
import time

# Initialize speech engine
engine = pyttsx3.init()

# Helper function for speaking text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Search Google function
def search_google(topic):
    search_url = f"https://www.google.com/search?q={topic}"
    webbrowser.open(search_url)
    speak(f"Searching for {topic} on Google.")

# Reminder function
def set_reminder(reminder_time, reminder_message):
    time.sleep(reminder_time)
    notification.notify(
        title="Reminder",
        message=reminder_message,
        timeout=10
    )
    speak(f"Reminder set! I'll notify you in {reminder_time // 60} minutes.")

# Writing in Notepad function
def write_in_notepad(text):
    os.system('notepad')
    time.sleep(1)
    pyautogui.typewrite(text)

# Sing a song function
def sing_song():
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    song = "🎶 Twinkle twinkle little star, How I wonder what you are! 🎶"
    speak(song)

# Listen to commands using speech recognition
def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            speak("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)
            process_command(command)
    except Exception as e:
        print("Sorry, I could not understand the command.")
        speak("Sorry, I could not understand that.")

# Process commands
def process_command(command):
    if 'search for' in command:
        topic = command.replace('search for', '').strip()
        search_google(topic)
    elif 'set reminder' in command:
        time_in_minutes = int(command.split()[2])
        reminder_message = " ".join(command.split()[3:])
        set_reminder(time_in_minutes * 60, reminder_message)
    elif 'write in notepad' in command:
        text_to_write = command.replace('write in notepad', '').strip()
        write_in_notepad(text_to_write)
    elif 'sing a song' in command:
        sing_song()
    elif 'exit' in command:
        speak("Goodbye!")
        root.quit()
    else:
        speak("I did not understand that command.")

# GUI Setup using Tkinter
root = tk.Tk()
root.title("Jarvis Assistant")
root.geometry("600x400")  # Set window size

# Set background color or image
root.config(bg="#282828")

# Add a label for assistant status
status_label = tk.Label(root, text="Click below to start!", font=("Arial", 16), bg="#282828", fg="white")
status_label.pack(pady=20)

# Create buttons for each command
listen_button = tk.Button(root, text="Listen", font=("Arial", 14), width=20, height=2, command=listen, bg="#4CAF50", fg="white", activebackground="#45a049")
listen_button.pack(pady=10)

search_button = tk.Button(root, text="Search Google", font=("Arial", 14), width=20, height=2, command=lambda: search_google('Python programming'), bg="#2196F3", fg="white", activebackground="#1976D2")
search_button.pack(pady=10)

reminder_button = tk.Button(root, text="Set Reminder", font=("Arial", 14), width=20, height=2, command=lambda: set_reminder(5*60, "Meeting in 5 minutes!"), bg="#FF9800", fg="white", activebackground="#FB8C00")
reminder_button.pack(pady=10)

song_button = tk.Button(root, text="Sing a Song", font=("Arial", 14), width=20, height=2, command=sing_song, bg="#9C27B0", fg="white", activebackground="#8E24AA")
song_button.pack(pady=10)

# Add an Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), width=20, height=2, command=root.quit, bg="#f44336", fg="white", activebackground="#e53935")
exit_button.pack(pady=20)

# Running the main event loop
root.mainloop()

import pyttsx3
import datetime
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)

# Speak Function
def speak(audio):
    """Function to convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

# Read the alarm time from the file
try:
    with open("Alarmtext.txt", "r") as extractedtime:
        time = extractedtime.read().strip()
        if not time:
            raise ValueError("Alarm time not found in file.")
except FileNotFoundError:
    print("Alarmtext.txt file not found.")
    exit()

# Clear the file after reading
with open("Alarmtext.txt", "w") as deletetime:
    deletetime.truncate(0)

def ring(alarm_time):
    """Function to trigger the alarm at the specified time."""
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            speak("Alarm ringing, sir.")
            try:
                os.startfile("Alarm.mp3")  # Replace with the correct file path
            except FileNotFoundError:
                speak("Alarm sound file not found.")
            break

# Start the alarm
try:
    print(f"Alarm set for: {time}")
    ring(time)
except Exception as e:
    print(f"Error: {e}")

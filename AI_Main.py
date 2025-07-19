
import os
from click import command
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import webbrowser
import requests
from bs4 import BeautifulSoup
import pyautogui
import speedtest



from Intro import play_gif
play_gif

       
# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)


#Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Optional: adjust for ambient noise
        audio = r.listen(source, timeout=10)  # Listen for audio input
    try:
        query = r.recognize_google(audio)  # Recognize speech using Google API
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""





print("Speak 'Wake Up' to raise me")





#Read Command Function
def read_commands():
    """Function to read commands from a text file."""
    try:
        with open("c:\\xampp\\htdocs\\PythonProject\\DeskTopAi\\commands.txt", "rb") as f:
            commands = f.readlines()
        return [command.strip() for command in commands]
    except FileNotFoundError:
        return []
    


#Write Command
def write_commands(command):
    """Function to store the command in a text file."""
    with open("c:\\xampp\\htdocs\\PythonProject\\DeskTopAi\\commands.txt", "a") as f:
        f.write(command + "\n")

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close
    os.startfile("Alarm.py")
    
# Main function of search
def search(query, platform):
    """Generic function to search on different platforms."""
    query = query.replace(f"{platform}", "").replace("search", "").strip()
    if platform == "youtube":
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir.")
    elif platform == "wikipedia":
        speak("Searching from Wikipedia...")
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia...")
        print(results)
        speak(results)
    elif platform == "google":
        speak("This is what I found on Google, sir")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, sentences=1)
            speak(result)
        except Exception:
            speak("Sorry sir, I could not find anything on Google, as per your search.")
# Main function of search
def search(query, platform):
    """Generic function to search on different platforms."""
    query = query.replace(f"{platform}", "").replace("search", "").strip()
    if platform == "youtube":
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir.")
    elif platform == "wikipedia":
        speak("Searching from Wikipedia...")
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia...")
        print(results)
        speak(results)
    elif platform == "google":
        speak("This is what I found on Google, sir")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, sentences=1)
            speak(result)
        except Exception:
            speak("Sorry sir, I could not find anything on Google, as per your search.")


# Code for conversation 
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "rest" in query:
                    speak("Ok sir, you can call me anytime")
                    exit()
                
                # JARVIS 2.0
                    
                elif "change password" in query:
                    new_pw = input("Enter the new password: ")
                    with open("c:\\xampp\\htdocs\\PythonProject\\DeskTopAi\\JarvisKey.txt", "w") as new_password:
                        new_password.write(new_pw)
                    speak("Done Sir")
                    speak(f"New Password is {new_pw}")
                
                elif "screenshot" in query:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("screenshot.png")
                elif"sleep" in query:
                    speak("Ok sir, Speak WAKE UP to raise me ")
                    break
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("Camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload() / 1048576  # Megabyte = 1024 * 1024
                    download_net = wifi.download() / 1048576
                    speak(f"Wifi Upload Speed is {upload_net:.2f} Megabytes")
                    speak(f"Wifi Download Speed is {download_net:.2f} Megabytes")
                
                elif "ipl score" in query:
                    from plyer import notification
                    import requests
                    from bs4 import BeautifulSoup

                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    
    # Check if the request was successful
                    if page.status_code == 200:
                        soup = BeautifulSoup(page.text, "html.parser")
                        speak("Hello")
        # Find the team names and scores
                        teams = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
                        scores = soup.find_all(class_="cb-ovr-flo")

                        if len(teams) >= 2 and len(scores) >= 11:
                            team1 = teams[0].get_text()
                            team2 = teams[1].get_text()
                            team1_score = scores[8].get_text()
                            team2_score = scores[10].get_text()

            # Print the scores
                            print(f"{team1} : {team1_score}")
                            print(f"{team2} : {team2_score}")

            # Send notification
                            notification.notify(
                                title="IPL SCORE :- ",
                                message=f"{team1} : {team1_score}\n{team2} : {team2_score}",
                                timeout=15
                            )
                        else:
                            print("Could not find the required team or score information.")
                    else:
                        print(f"Failed to retrieve data. Status code: {page.status_code}")
                        
                        
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\xampp\\htdocs\\PythonProject\\DeskTopAi\\FocusMode.py")
                        exit()

                    
                    else:
                        pass
                
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)
                    
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                    
                elif "i am fine" in query:
                    speak("Good to hear that sir, how can I help you?")
                    
                elif "how are you" in query:
                    speak("I am fine sir, just waiting for you.")
                    
                elif "thank you" in query:
                    speak("Always welcome sir.")
                    
                elif "where are you" in query:
                    speak("I am in your system sir, I am a virtual assistant.")
                    
                elif "play a game" in query:
                    from Game import game_play
                    game_play()
                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                elif "google" in query:
                    search(query, "google")
                    
                elif "youtube" in query:
                    search(query, "youtube")
                
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video Paused")
                
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video Playing")
                
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video Muted")
                
                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                    
                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("c:\\xampp\\htdocs\\PythonProject\\DeskTopAi\\Remember.txt","+w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("c:\\xampp\\htdocs\\PythonProject\\DeskTopAi\\Remember.txt","r")
                    speak("You told me " + remember.read())
                
                                
                elif "wikipedia" in query:
                    search(query, "wikipedia")
                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                
                elif "calculate" in query:
                    from Calculator import wolframalpha
                    from Calculator import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                elif "temperature" in query:
                    search = "Temperature in "
                    location = query.replace("temperature in ", "")
                    url = f"https://www.google.com/search?q=temperature+in+{location}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} {location} is {temp}")
                    
                elif "set an alarm" in query:
                    speak("Please tell the time in hours, minutes, and seconds.")
                    print("Example:-00:00:00")
                    time_input = input("Please tell the time: ")
                    alarm(time_input)
                    speak("Alarm set, sir.")
                    
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
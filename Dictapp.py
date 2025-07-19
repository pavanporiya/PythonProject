import os
import pyautogui
import webbrowser
import pyttsx3
import query
from time import sleep
from AI_Main import speak

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)


dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("launching sir")
    if ".com" in query or ".co.in" in query or ".org" in query or "chrome" in query or "commandprompt" in query or "excel" in query or "vscode" in query or "powerpoint" in query or "paint" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace("","")
        webbrowser.open(f"https://www.{query}")
    
    else:
        keys =list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start{dict[app]}")

def closeappweb(query):
    speak("Closing sir")
    if "one tab" in query or "1 tab" in query or "the tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("The Tab is closed, sir")
        
    elif "two tab" in query or "2 tab" in query: 
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Tabs are closed, sir")
    
    elif "three tab" in query or "3 tab" in query: 
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Tabs are closed, sir")
    
    elif "four tab" in query or "4 tab" in query: 
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Tabs are closed, sir")
    
    elif "five tab" in query or "5 tab" in query: 
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Tabs are closed, sir")
    
    elif "six tab" in query or "6 tab" in query: 
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Tabs are closed, sir")
        
    elif "seven tab" in query or "7 tab" in query: 
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Tabs are closed, sir")
    
    else:
        keys = list(dictapp.keys())
        for app in keys:  # Change here to iterate over keys
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")  # Use dictapp instead of dict
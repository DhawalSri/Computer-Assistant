import pywhatkit as kit
from time import sleep
import pyautogui
import speech_recognition
import pyttsx3
import datetime
import webbrowser
import os
from bs4 import BeautifulSoup
from time import sleep
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("understanding....")
        query = r.recognize_google(audio,language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def ClearCache():
    pyautogui.hotkey("win","r")
    pyautogui.typewrite("%temp%")
    pyautogui.press("enter")
    sleep(1)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("del")
    pyautogui.press("enter")

    
    
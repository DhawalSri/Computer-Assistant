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

def wmsg(query):
    speak("sending message")
    #msg = query
    if "govind" in query:
        query = query.replace("message","")
        query = query.replace("govind","")
        query = query.replace("to","")
        msg = query
        kit.sendwhatmsg_instantly("+919235148944", msg)
        sleep(1.0)
        pyautogui.click(1791,973)

    if "ashutosh" in query or "ashu" in query:
        query = query.replace("message", "")
        query =  query.replace("asutosh", "")
        query = query.replace("ashu", "")
        query = query.replace("to", "")
        msg = query
        kit.sendwhatmsg_instantly("+918736815344", msg)
        sleep(1.0)
        pyautogui.click(1791,973)

    elif "disha" in query:
        query = query.replace("message","")
        query = query.replace("disha","")
        query = query.replace("to","")
        msg = query
        kit.sendwhatmsg_instantly("+919264949086", msg)
        sleep(1.0)
        pyautogui.click(1791,973)

    if "steve" in query:
        query = query.replace("message","")
        query = query.replace("steve","")
        query = query.replace("to","")
        msg = query
        kit.sendwhatmsg_instantly("+917408912031", msg)
        sleep(1.0)
        pyautogui.click(1791,973)

    if "naina" in query:
        query = query.replace("message","")
        query = query.replace("naina","")
        query = query.replace("to","")
        msg = query
        kit.sendwhatmsg_instantly("+916392152694", msg)
        sleep(1.0)
        pyautogui.click(1791,973)

    if "papa" in query:
        query = query.replace("message","")
        query = query.replace("papa","")
        query = query.replace("to","")
        msg = query
        kit.sendwhatmsg_instantly("+919415195860", msg)
        sleep(1.0)
        pyautogui.click(1791,973)

    if "misthi" in query or "mishthi" in query:
        query = query.replace("message","")
        query = query.replace("misthi","")
        query = query.replace("mishthi","")
        query = query.replace("to","")
        msg = query
        kit.sendwhatmsg_instantly("+919453947765", msg)
        sleep(1.0)
        pyautogui.click(1791,973)

    if "niyati" in query:
        query = query.replace("message","")
        query = query.replace("niyati","")
        query = query.replace("to","")
        msg = query
        kit.sendwhatmsg_instantly("+917985990914", msg)
        sleep(1.0)
        pyautogui.click(1791,973)
    if "anurag" in query:
        query = query.replace("message","")
        query = query.replace("anurag","")
        query = query.replace("to","")
        msg = query
        kit.sendwhatmsg_instantly("+919341636364", msg)
        sleep(1.0)
        pyautogui.click(1791,973)



    


#phn_no = "+919235148944"
#msg = "Hello bro"


#kit.sendwhatmsg_instantly(phn_no, msg)
#sleep(1.0)
#pyautogui.click(1791,973)

import pyttsx3
import speech_recognition
from bs4 import BeautifulSoup
import requests
import datetime
import os
import pyautogui
import keyboard
import random
import webbrowser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from plyer import notification
from pygame import mixer
import subprocess
import tkinter as tk
import threading
import sys

overlay = None  # Global reference for GUI overlay





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 290)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class StickyOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # Remove border
        self.root.attributes('-topmost', True)  # Always on top
        self.root.attributes('-alpha', 0.85)  # Translucent
        self.root.configure(bg='black')

        screen_width = self.root.winfo_screenwidth()
        self.root.geometry(f"160x60+{screen_width - 180}+30")  # Top-right corner

        # Label showing the status
        self.label = tk.Label(self.root, text="Listening...", font=("Segoe UI", 12),
                              fg="white", bg="black", anchor='w')
        self.label.pack(fill="both", expand=True, padx=10)

        # Close Button
        self.close_btn = tk.Button(self.root, text="✕", command=self.exit_app,
                                   bg="black", fg="red", borderwidth=0, font=("Arial", 12))
        self.close_btn.place(relx=1.0, rely=0.0, anchor="ne")

    def run(self):
        self.root.mainloop()

    def exit_app(self):
        self.root.destroy()
        sys.exit()

    def update_text(self, new_text):
        self.label.config(text=new_text)

# Run it in a separate thread so it doesn’t block your assistant loop
def launch_overlay():
    global overlay
    overlay = StickyOverlay()
    overlay.run()

gui_thread = threading.Thread(target=launch_overlay, daemon=True)
gui_thread.start()

import time
time.sleep(1)

def takeCommand():
    overlay.update_text("Listening...")
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        overlay.update_text("Processing...")
        print("understanding....")
        query = r.recognize_google(audio,language="en-in")
        print(f"You said: {query}\n")
        overlay.update_text("Listening...")
    except Exception as e:
        print("Say that again")
        overlay.update_text("Didn't catch that")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "take rest" in query:
                    speak("Ok sir, You can call me anytime.")
                    break

                elif "thank you" in query:
                    speak("You're welcome, sir")

                elif "play" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "launch" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "pause" in query:
                    pyautogui.press("k")
                elif "resume" in query:
                    pyautogui.press("k")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted, sir.")
                elif "volume up" in query or "increase the volume" in query:
                    from keyboard import volumeup
                    speak("turning volume up")
                    volumeup()
                elif "volume down" in query or "decrease the volume" in query:
                    from keyboard import volumedown
                    speak("turning volume down")
                    volumedown()
                elif "tired" in query:
                    speak("Playing your favourite playlist sir.")
                    webbrowser.open("https://music.amazon.in/my/playlists/8240b65a-605c-4287-ac36-0140f0544011")
                    sleep(3.0)
                    pyautogui.click(570,490)
                    sleep(1.0)
                    pyautogui.click(570,490)
                elif "shutdown" in query or "shut down" in query:
                    speak("Are you sure you want to shut down the computer?")
                    query = takeCommand().lower()
                    if "no" in query:
                        speak("Aborting shut down, sir")
                        # exit()
                    elif "yes" or "sure" in query:
                        speak("Shutting down the computer sir")
                        os.system("shutdown /s /t 1")
                elif "restart" in query:
                    speak("Are you sure you want to restart the computer?")
                    query = takeCommand().lower()
                    if "no" in query:
                        speak("Aborting restart")
                    elif "yes" or "sure" in query:
                        os.system("shutdown /r /t 5")
                elif "sleep" in query:
                    speak("Are you sure you want to put the computer to sleep?")
                    query = takeCommand().lower()
                    if "no" in query:
                        speak("Aborting sleep")
                    elif "yes" or "sure" in query:
                        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                elif "message" in query:
                    from whatmsg import wmsg
                    wmsg(query)
                    speak("message sent sir")
                    sleep(1.0)
                    pyautogui.hotkey("ctrl","w")
                elif "take a screenshot" in query:
                    pyautogui.screenshot("scrshot.png")
                    speak("done sir")
                elif "switch windows" in query:
                    pyautogui.hotkey("alt", "tab")

                #TESTING PHASE
                #elif "unlock my computer" in query:
                    #speak("Unlocking your computer sir")
                    #from pcUnlock import unlock
                    #kunlock()

                elif "lock my computer" in query:
                    speak("Locking your computer sir.")
                    cmd='rundll32.exe user32.dll, LockWorkStation'
                    subprocess.call(cmd)
                    
                elif "schedule my day" in query:
                    tasks = [] #emptyList
                    speak("Do you want to remove old tasks")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        numberoftask = int(input("enter the number of tasks:"))
                        i = 0
                        for i in range(numberoftask):
                            tasks.append(input("Enter the tasks:"))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        numberoftask = int(input("enter the number of tasks:"))
                        for i in range(numberoftask):
                            tasks.append(input("Enter the tasks:"))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notifi.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My Schedule",
                        message = content,
                        timeout = 15
                    )
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press("enter")
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "temperature" in query:
                    search = "temperature in lucknow is"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "bye jarvis" in query:
                    speak("goodbye, sir.")
                    exit()

                #TESTING PHASE
                # elif "text to speech" or "Text to speech" in query:
                #     speak("Here your text sir")
                #     from TexttoSpeech import textTospeech
                #     textTospeech()
                #     # print(query)

                if "calculate" in query:
                    from gpt import Chatgpt
                    Chatgpt(query)


   
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
import openai



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 250)

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

def Chatgpt(query):
    openai.api_key = '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'

    messages = [{"role": "system", "content": query}]
    while True:
        message = query
        if message:
            message.append({"role": "user", "content": message},)
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

            reply = chat.choices[0].message.content
            speak(f"Chatgpt: {reply}")

            # messages.append({"role": "assistant", "content": reply})
    


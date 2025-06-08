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

def unlock():


    pyautogui.press("space")
    sleep(0.2)
    pyautogui.press("2")
    sleep(0.2)
    pyautogui.press("2")
    sleep(0.2)
    pyautogui.press("6")
    sleep(0.2)
    pyautogui.press("0")
    sleep(0.2)
    pyautogui.press("1")
    sleep(0.2)
    pyautogui.press("2")
    
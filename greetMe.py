import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak("Good Morning sir.")
        speak(f"The time is {strTime}")
        speak("How may i help you?")
        
    elif 12 < hour < 18:
        speak("Good Afternoon, sir")

    else:
        speak("Good evening, sir")

        

    #speak("Please tell me, How can I help you?")
    
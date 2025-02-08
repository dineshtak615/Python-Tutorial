# ex -11
import pyttsx3
import time 
timeinterval=30
engine=pyttsx3.init()

command ={" hey harry drink the water hey harry drink the water "}

for cmd in command:
    engine.say(f"harry sir {cmd}")
    time.sleep(timeinterval)
    engine.runAndWait()
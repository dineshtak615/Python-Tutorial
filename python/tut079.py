# ex--9
import pyttsx3
shoutout={"manish ", "danish",'amit',"lokesh"}
engine=pyttsx3.init()

for name in shoutout:
    engine.say(f"shoutout to {name}")
    engine.runAndWait()
# from os import system

# names=["rahul","rohan","amit","javed","ritika","jhon"]
# for name in names:
#     system(f"say shoutout to {name}")
import os
from time import sleep
from termcolor import colored
import json
# import pyttsx3
# engine = pyttsx3.init()
# voice = engine.getProperty('voices')[0]  # the french voice
# engine.setProperty('voice', voice.id)

with open('5.json', encoding='utf-8') as fh:
    data = json.load(fh)

for el in data:
    os.system("clear")
    print(colored(el["citation"], "green"))
    # engine.say(el["citation"])
    # engine.runAndWait()
    sleep(2)

    print(colored(el["procedes"], "yellow"))
    # engine.say(el["procedes"])
    # engine.runAndWait()

    print(colored(el['analyse'], "blue"))
    # engine.say(el["analyse"])
    # engine.runAndWait()
    sleep(3)

import os
from time import sleep
from termcolor import colored
import json
# import pyttsx3
# engine = pyttsx3.init()
# voice = engine.getProperty('voices')[0]  # the french voice
# engine.setProperty('voice', voice.id)

os.system("clear")
n = input('Entrez le numero de texte (1,2,3,4,5,7,8): ')
with open(f'{n}/{n}.json', encoding='utf-8') as fh:
    data = json.load(fh)

for el in data:
    os.system("clear")
    input(colored(el["citation"], "green"))
    # engine.say(el["citation"])
    # engine.runAndWait()

    input(colored(el["procedes"], "yellow"))
    # engine.say(el["procedes"])
    # engine.runAndWait()

    input(colored(el['analyse'], "blue"))
    # engine.say(el["analyse"])
    # engine.runAndWait()
    # sleep(6)

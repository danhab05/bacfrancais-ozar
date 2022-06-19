import urllib.request
import json
import os
import platform
from time import sleep
import requests
from termcolor import colored
import json
# import pyttsx3
# engine = pyttsx3.init()
# voice = engine.getProperty('voices')[0]  # the french voice
# engine.setProperty('voice', voice.id)
while True:
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    while True:
        try:
            with open('msg.txt') as f:
                msg = f.readline()
            n = input(msg)
            with open(f'Json_files/{n}/{n}.json', encoding='utf-8') as fh:
                data = json.load(fh)
            break
        except Exception:
            pass

    title = ""
    for el in data:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        citation = el["citation"]
        if "MOUVEMENT" in citation:
            title = citation
        else:
            print(colored(title, "red"))
        input(colored(citation, "green"))
        input(colored(el["procedes"], "yellow"))
        input(colored(el['analyse'], "blue"))

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
            response = requests.get("https://raw.githubusercontent.com/danhab05/bacfrancais-ozar/master/msg.txt")
            msg = response.text
            n = input(msg)
            with urllib.request.urlopen(f"https://raw.githubusercontent.com/danhab05/bacfrancais-ozar/master/Json_files/{n}/{n}.json") as url:
                data = json.loads(url.read().decode())
            break
        except Exception as e:
            if "HTTPSConnectionPool" in str(e):
                with open('msg.txt') as f:
                    msg = f.readline()
                n = input(msg)
                with open(f'Json_files/{n}/{n}.json', encoding='utf-8') as fh:
                    data = json.load(fh)
                break
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

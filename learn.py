import os
import platform
from time import sleep
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
            n = input('Entrez le numero de texte (1,2,3,4,5,7,8,9,10): ')
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

        

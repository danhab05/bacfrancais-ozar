import requests
try:
    response = requests.get("https://raw.githubusercontent.com/danhab05/bacfrancais-ozar/master/msg.txt")
    msg = response.text
except Exception as e:
    print(e)
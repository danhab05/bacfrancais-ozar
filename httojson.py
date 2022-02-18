
import json
from bs4 import BeautifulSoup
lst = []

with open('a.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    tr = soup.find_all("tr")
    for td in tr:
        dt = td.find_all("td")
        try:
            if "EXTRAIT" not in dt[0].text:
                lst.append(
                    {
                        "citation": dt[0].text,
                        "procedes": dt[1].text,
                        "analyse": dt[2].text
                    }
                )
        except Exception:
            pass
with open('m1.json', 'w', encoding='utf-8') as f:
    json.dump(lst, f, ensure_ascii=False, indent=4)

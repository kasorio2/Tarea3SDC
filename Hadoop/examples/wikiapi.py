import requests
import json
import wikipediaapi
import os

paises = ["Argentina", "Bolivia", "Perú", "Brazil", "Canada", "Venezuela", "Chile", "Rusia", "Alemania", "España",
                  "El Salvador", "Italia", "Francia", "Guatemala", "Australia", "Colombia", "Ecuador", "Uruguay", "México",
                  "Filipinas", "Nigeria", "Qatar", "China", "Japón", "Grecia", "Portugal", "Costa Rica", "Cuba",
                  "India", "Israel"]

i = 1

for paginas in paises:
    if i <= 15:
        wiki_wiki = wikipediaapi.Wikipedia(user_agent='tarea3sd',language='en',extract_format=wikipediaapi.ExtractFormat.WIKI)
        page = wiki_wiki.page(paginas)
        if page.exists():
            text = '{} {}<splittername>{}'.format(i, page.fullurl ,json.dumps(page.text))
            file = f"./carpeta1/{i}{paginas}.txt"
            if os.path.isfile(file):
                os.remove(file)
            with open(file, 'wb') as f:
                f.write(text.encode('utf-8'))  
    else:
        wiki_wiki = wikipediaapi.Wikipedia(user_agent='tarea3sd',language='en',extract_format=wikipediaapi.ExtractFormat.WIKI)
        page = wiki_wiki.page(paginas)
        if page.exists():
            text = '{} {}<splittername>{}'.format(i, page.fullurl ,json.dumps(page.text))
            file = f"./carpeta2/{i}{paginas}.txt"
            if os.path.isfile(file):
                os.remove(file)
            with open(file, 'wb') as f:
                f.write(text.encode('utf-8'))
    i += 1

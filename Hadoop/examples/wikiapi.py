import requests
import json
import wikipedia as wiki
import os

p = ["Argentina", "Bolivia", "Perú", "Brazil", "Canada", "Venezuela", "Chile", "Russia", "Alemania", "España",
                  "El Salvador", "Italia", "Francia", "Guatemala", "Australia", "Colombia", "Ecuador", "Uruguay", "México",
                  "Filipina", "Nigeria", "Qatar", "China", "Japón", "Greece", "Portugal", "Costa Rica", "Cuba",
                  "India", "Israel"]

i = 1

for i in p:
    a = wiki.page(i,auto_suggest=False)
    carpeta = "carpeta1" if p.index(i) < 15 else "carpeta2"
    with open("./"+carpeta+"/"+str(p.index(i))+"wiki"+str(i.replace(" ", "_"))+".txt", "w") as f:
        f.write(str(p.index(i))+"xdxdxd")
        f.write('\n')
        f.write(a.content)
        f.write('\n')
        f.close()
    print("Escribio el archivo: "+i)
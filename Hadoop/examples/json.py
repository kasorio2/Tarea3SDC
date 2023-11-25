#!/usr/bin/env python
# -*- coding:utf-8 -*

import sys
import json
import os

current_word = None
current_count = 0
word = None

doc_count = {}

for line in sys.stdin:
    result = line.replace("\n", "").split('\t')

    if result[0] in doc_count.keys():
        if result[1] in doc_count[result[0]].keys():
            doc_count[result[0]][result[1]] += 1
        else:
            doc_count[result[0]][result[1]] = 1
    else:
        doc_count[result[0]] = {result[1]: 1}

# Convertir el diccionario a formato JSON
output_json = json.dumps(doc_count, indent=2)

# Crear la carpeta 'outhadoop' si no existe
output_folder = 'outhadoop'
os.makedirs(output_folder, exist_ok=True)

# Guardar el resultado en un archivo JSON dentro de la carpeta 'outhadoop'
output_file = os.path.join(output_folder, 'output.json')
with open(output_file, 'w') as json_file:
    json_file.write(output_json)

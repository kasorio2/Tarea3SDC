import json
import re

files = {}  # Inicializa un diccionario vacío para almacenar los datos

# Abre el archivo de entrada para lectura
a_file = open("./outhadoop/part-00000", "r")

# Ignora la primera línea del archivo
next(a_file)

# Itera a través de las líneas restantes del archivo
for line in a_file:
    # Elimina los espacios en blanco al principio y al final de cada línea
    l = line.strip()

    # Divide la línea en palabra y pos utilizando el primer carácter de tabulación
    word, pos = l.split("\t", 1)

    word = re.sub(r'[-{}""+\/#*:.-_¿?·$%1234567890]', '', word)  # Elimina caracteres en minúscula

    # Divide la cadena pos en una lista de subcadenas utilizando el espacio como separador
    P = pos.split(" ")

    # Itera a través de las subcadenas en P
    for i in P:
        # Elimina paréntesis y divide la subcadena en dos partes utilizando la coma como separador
        a, c = (i.replace("(", "").replace(")", "")).split(",")
        a = re.sub(r'[-{}""+\/#*:.-_¿?·$%1234567890]', '', a)  # Elimina caracteres en minúscula

        # Verifica si la palabra ya está en el diccionario 'files'
        if word in files:
            files[word][a] = int(c)
        else:
            # Si la palabra no está en el diccionario, agrégala con un nuevo diccionario como su valor
            files[word] = {a: int(c)}

# Cierra el archivo de entrada
a_file.close()

# Abre el archivo JSON de salida para escritura
with open("./database/db.json", "w") as outfile:
    # Escribe el diccionario 'files' en el archivo JSON con sangría para mejorar la legibilidad
    json.dump(files, outfile, indent=4)

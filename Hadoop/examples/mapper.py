#!/usr/bin/env python
# -*-coding:utf-8 -*

# Importar el módulo sys para la entrada estándar
import sys
import psycopg2
import re

connection = psycopg2.connect(  user = "postgres",
                                password = "postgres",
                                host = "db",
                                port = "5432",
                                database = "db")

# Iterar sobre cada línea de la entrada estándar
for line in sys.stdin:
    docs = line.lower()
    arr = []

    i = 0
    # Dividir la línea en dos partes usando el marcador '<splittername>'
    name, docs = docs.split('<splittername>')
    name, url = name.split()

    # Iterar sobre una lista de caracteres a ser eliminados o reemplazados
    for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&"]:
        docs = docs.replace(char, '')

    for word in docs.split():
            # Check if the word is a letter
            if not word.isalpha():
                # Skip the word
                continue

            # Add the processed word to the array
            arr.append((word, name, 1))

    # Iterar sobre la lista 'arr' ordenada y imprimir cada elemento
    for word_data in sorted(arr):
        word, name, count = word_data
        print(f"{word}\t{name}\t{count}")

    try:
        cursor = connection.cursor()
        for i in range(30):
            cursor.execute("INSERT INTO paginas (id, url) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", (name, url))
            connection.commit()

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

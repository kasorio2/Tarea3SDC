#!/usr/bin/env python
# -*-coding:utf-8 -*
import psycopg2
import re
import json
import os

try:
    cursor = connection.cursor()
    print("Registrando elementos a la base de datos...")
    with open('outhadoop/part-00000','r') as archivo:
     next(archivo)
     for linea in archivo:
         datos = re.findall(r'\b\w+\b|\([^)]*\)', linea)

         letra = datos[0]
         pares = [tuple(map(int, par.strip('()').split(' '))) for par in datos[1:]]
         for n, m in pares:
             cursor.execute("INSERT INTO registros (palabra, documento, repeticiones) VALUES (%s, %s, %s) ON CONFLICT (palabra, documento) DO NOTHING", (letra, n, m))
         
         connection.commit()
    
    while True:
         print("\nMenú")
         print("1. Buscar palabra")
         print("2. Salir")

         opcion = input("Seleccione una opción: ")
         if opcion == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            palabra = input("Inserte palabra: ")

            query = f"SELECT documento, repeticiones, url FROM paginas INNER JOIN registros ON paginas.id = registros.documento WHERE palabra = '{palabra}' ORDER BY repeticiones DESC LIMIT 5"
            cursor.execute(query)

            resultados = cursor.fetchall()
            resultados_json = []
            column_names = [desc[0] for desc in cursor.description]

            for fila in resultados:
                fila_json = dict(zip(column_names, fila))
                resultados_json.append(fila_json)
            
            print(json.dumps(resultados_json, indent=2))
         elif opcion == "2":
            break
         else:
            print("Opcion Incorrecta")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
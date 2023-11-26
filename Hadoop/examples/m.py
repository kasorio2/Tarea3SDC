import json
import re

# Función para cargar el índice invertido desde el archivo JSON
def cargar_indice_invertido():
    with open("./database/db.json", "r") as infile:
        return json.load(infile)

# Función para procesar la consulta del usuario
def procesar_consulta(consulta):
    # Eliminar caracteres especiales y convertir a minúsculas
    consulta_procesada = re.sub(r'[-{}""+\/#*:.-_¿?·$%1234567890]', '', consulta.lower())
    # Dividir la consulta en palabras clave
    return consulta_procesada.split()

# Función para buscar los mejores resultados basados en la consulta y el índice invertido
def buscar_mejores_resultados(indice_invertido, consulta, num_resultados=5):
    resultados = {}
    palabras_clave = procesar_consulta(consulta)

    # Iterar sobre las palabras clave de la consulta
    for palabra in palabras_clave:
        if palabra in indice_invertido:
            # Iterar sobre los documentos y frecuencias asociadas a la palabra
            for documento, frecuencia in indice_invertido[palabra].items():
                if documento in resultados:
                    resultados[documento] += frecuencia
                else:
                    resultados[documento] = frecuencia

    # Ordenar los documentos por puntaje en orden descendente
    resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

    # Seleccionar los mejores resultados
    mejores_resultados = resultados_ordenados[:num_resultados]

    return mejores_resultados

# Función principal del programa
def main():
    # Cargar el índice invertido
    indice_invertido = cargar_indice_invertido()

    # Obtener la consulta del usuario
    consulta_usuario = input("Ingrese su consulta: ")
    
    # Buscar y obtener los mejores resultados
    resultados = buscar_mejores_resultados(indice_invertido, consulta_usuario)

    # Imprimir los mejores resultados
    print("Los 5 mejores resultados son:")
    for resultado in resultados:
        documento_id = resultado[0]
        frecuencia = resultado[1]
        print(f"Documento {documento_id}: {frecuencia} veces")

# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()

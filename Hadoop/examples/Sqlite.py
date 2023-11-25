import sqlite3

# Conectar a la base de datos SQLite (asegúrate de cambiar 'tu_base_de_datos.db' al nombre de tu base de datos)
conn = sqlite3.connect('tu_base_de_datos.db')
cursor = conn.cursor()

# Crear una tabla si no existe (ajusta la estructura según tus necesidades)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS WordCount (
        Document INTEGER,
        Frecuencia INTEGER,
        URL TEXT
    )
''')


# Insertar datos en la tabla
for word, document, count in data:
    cursor.execute('INSERT INTO WordCount (Word, Document, Count) VALUES (?, ?, ?)', (word, document, count))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
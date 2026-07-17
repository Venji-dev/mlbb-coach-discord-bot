import sqlite3
import csv

# 1. Conectamos a la base de datos
conexion = sqlite3.connect("heroes.db")
cursor = conexion.cursor()

# 2. Borramos la tabla vieja
cursor.execute("DROP TABLE IF EXISTS heroes")

# 3. Crear tablas de la nueva carpeta
cursor.execute("""
    CREATE TABLE heroes (
        heroes TEXT PRIMARY KEY,
        jungla TEXT,
        linea_exp TEXT,
        linea_mid TEXT,
        linea_gold TEXT,
        roamer TEXT,
        consejo_general TEXT
    )
""")

# 4. Leer el archivo csv e insertar las filas
with open("heroes.csv", mode="r", encoding="latin-1") as archivo_csv:
    lector = csv.DictReader(archivo_csv, delimiter=";")

    for fila in lector:
        cursor.execute("""
         INSERT INTO heroes (heroes, jungla, linea_exp, linea_mid, linea_gold, roamer, consejo_general)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            fila["heroes"],
            fila["jungla"],
            fila["linea_exp"],
            fila["linea_mid"],
            fila["linea_gold"],
            fila["roamer"],
            fila["consejo_general"]
        ))

# 5. Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()
print("¡Base de datos con 10 heroes nuevos actualizada con exito!")
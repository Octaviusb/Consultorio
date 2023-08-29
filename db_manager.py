import os
import sqlite3

class DBManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_tables(self):
        # Crear una conexión a la base de datos
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # Crear la tabla "datos_personales" si no existe
        cur.execute('''
            CREATE TABLE IF NOT EXISTS datos_personales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha_nacimiento TEXT NOT NULL,
                edad INTEGER NOT NULL,
                pregunta1 TEXT NOT NULL,
                pregunta2 TEXT NOT NULL,
                -- Agrega el resto de campos del cuestionario aquí
                -- Por ejemplo:
                -- pregunta3 TEXT NOT NULL,
                -- pregunta4 TEXT NOT NULL,
                -- ...
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Cerrar el cursor y la conexión a la base de datos
        cur.close()
        conn.close()

    def insert_datos_personales(self, datos_personales):
        # Crear una conexión a la base de datos
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # Construir la consulta SQL para insertar los datos
        sql = "INSERT INTO datos_personales (nombre, fecha_nacimiento, edad, pregunta1, pregunta2) VALUES (?, ?, ?, ?, ?)"
        values = (datos_personales['nombre'], datos_personales['fecha_nacimiento'], datos_personales['edad'],
                  datos_personales['pregunta1'], datos_personales['pregunta2'])
        cur.execute(sql, values)
        conn.commit()

        # Cerrar el cursor y la conexión a la base de datos
        cur.close()
        conn.close()

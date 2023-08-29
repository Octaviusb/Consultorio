import os
import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Configuración de la base de datos SQLite
db_path = os.path.join(os.path.dirname(__file__), 'consultorio.db')

def create_table():
    # Crear una conexión a la base de datos
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Crear tabla datos_personales si no existe
    cur.execute('''
        CREATE TABLE IF NOT EXISTS datos_personales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            direccion TEXT,
            telefono TEXT,
            diagnostico TEXT,
            tratamiento TEXT,
            evolucion TEXT,
            cita_anterior TEXT,
            nueva_cita TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Llamamos a la función create_table() para crear la tabla antes de ejecutar la app Flask
create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombreAdmin = request.form['nombreAdmin']
        direccionAdmin = request.form['direccionAdmin']
        telefonoAdmin = request.form['telefonoAdmin']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        evolucion = request.form['evolucion']
        citaAnterior = request.form['citaAnterior']
        nuevaCita = request.form['nuevaCita']

        try:
            # Crear una conexión a la base de datos
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()

            # Construir la consulta SQL para insertar los datos
            sql = "INSERT INTO datos_personales (nombre, direccion, telefono, diagnostico, tratamiento, evolucion, cita_anterior, nueva_cita) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            values = (nombreAdmin, direccionAdmin, telefonoAdmin, diagnostico, tratamiento, evolucion, citaAnterior, nuevaCita)

            # Ejecutar la consulta SQL
            cur.execute(sql, values)
            conn.commit()

            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()

            return redirect('/ver_datos')
        
        except Exception as e:
            return "Error al guardar los datos: " + str(e)

    return render_template('index.html')

@app.route('/ver_datos')
def ver_datos():
    try:
        # Crear una conexión a la base de datos
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # Consulta SQL para obtener todos los registros de la tabla datos_personales
        cur.execute("SELECT * FROM datos_personales")
        registros = cur.fetchall()

        # Cerrar el cursor y la conexión a la base de datos
        cur.close()
        conn.close()

        return render_template('ver_datos.html', registros=registros)

    except Exception as e:
        return "Error al obtener los datos: " + str(e)

@app.route('/ver_cuestionario/<int:paciente_id>')
def ver_cuestionario(paciente_id):
    try:
        # Obtener los datos del paciente con el paciente_id desde la base de datos
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM datos_personales WHERE id=?", (paciente_id,))
        paciente = cur.fetchone()
        cur.close()
        conn.close()

        # Renderizar la plantilla cuestionario.html y pasar los datos del paciente
        return render_template('cuestionario.html', paciente=paciente)

    except Exception as e:
        return "Error al obtener los datos del paciente: " + str(e)


    # Editar paciente    

@app.route('/editar_paciente/<int:paciente_id>', methods=['GET', 'POST'])
def editar_paciente(paciente_id):
    try:
        if request.method == 'POST':
            # Obtener los datos del formulario
            nombre = request.form['nombre']
            direccion = request.form['direccionAdmin']
            telefono = request.form['telefonoAdmin']
            diagnostico = request.form['diagnostico']
            tratamiento = request.form['tratamiento']
            evolucion = request.form['evolucion']
            cita_anterior = request.form['citaAnterior']
            nueva_cita = request.form['nuevaCita']

            try:
                # Actualizar los datos del paciente en la base de datos
                conn = sqlite3.connect(db_path)
                cur = conn.cursor()

                sql = "UPDATE datos_personales SET nombre=?, direccion=?, telefono=?, diagnostico=?, tratamiento=?, evolucion=?, cita_anterior=?, nueva_cita=? WHERE id=?"
                values = (nombre, direccion, telefono, diagnostico, tratamiento, evolucion, cita_anterior, nueva_cita, paciente_id)

                cur.execute(sql, values)
                conn.commit()

                cur.close()
                conn.close()

                return redirect('/ver_datos')

            except Exception as e:
                return "Error al guardar los cambios: " + str(e)

        # Tu código para editar y mostrar los datos del paciente en el formulario
        # ...

    except Exception as e:
        return "Error en la edición del paciente: " + str(e)


    # Obtener los datos del paciente para prellenar el formulario
    paciente = obtener_datos_del_paciente(paciente_id)  # Asegúrate de que esta función esté definida

    return render_template('editar_paciente.html', paciente=paciente)

    # Agegar paciente

@app.route('/agregar_paciente', methods=['GET', 'POST'])
def agregar_paciente():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombreAdmin = request.form['nombreAdmin']
        direccionAdmin = request.form['direccionAdmin']
        telefonoAdmin = request.form['telefonoAdmin']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        evolucion = request.form['evolucion']
        citaAnterior = request.form['citaAnterior']
        nuevaCita = request.form['nuevaCita']
        
        try:
            # Crear una conexión a la base de datos
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()

            # Construir la consulta SQL para insertar los datos
            sql = "INSERT INTO datos_personales (nombre, direccion, telefono, diagnostico, tratamiento, evolucion, cita_anterior, nueva_cita) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            values = (nombreAdmin, direccionAdmin, telefonoAdmin, diagnostico, tratamiento, evolucion, citaAnterior, nuevaCita)

            # Ejecutar la consulta SQL
            cur.execute(sql, values)
            conn.commit()

            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()

            return redirect('/ver_datos')
        
        except Exception as e:
            return "Error al guardar los datos: " + str(e)

    return render_template('agregar_paciente.html')


if __name__ == '__main__':
    app.run(debug=True)
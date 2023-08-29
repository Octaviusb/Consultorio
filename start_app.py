import os
import webbrowser
import subprocess

def main():
    # Ruta al ejecutable generado por pyinstaller o cx_Freeze
    executable_path = os.path.join(os.path.dirname(__file__), 'dist', 'app.exe')

    # Iniciar Gunicorn en segundo plano
    subprocess.Popen(['gunicorn', 'app:app', '-c', 'gunicorn_config.py'])

    # Abrir la aplicación en el navegador web
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    main()

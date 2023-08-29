# Archivo de configuración de Gunicorn

# Número de procesos de trabajo (workers) que se ejecutarán
workers = 4

# Host y puerto en el que Gunicorn escuchará las solicitudes
bind = '127.0.0.1:5000'

# Log de acceso a Gunicorn
accesslog = '-'  # "-" indica que se imprimirá en la consola
errorlog = '-'   # "-" indica que se imprimirá en la consola

# Nivel de verbosidad del log
loglevel = 'info'

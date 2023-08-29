import multiprocessing

bind = '127.0.0.1:8000'  # Cambia esta dirección si deseas que tu aplicación escuche en otras interfaces o puertos.

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2

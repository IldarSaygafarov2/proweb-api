import multiprocessing

bind = '127.0.0.1:5555'
workers = multiprocessing.cpu_count() + 1
user = 'root'
timeout = 120
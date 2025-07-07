import multiprocessing

bind = '127.0.0.1:7894'
workers = multiprocessing.cpu_count() + 1
user = 'ildar'
timeout = 120
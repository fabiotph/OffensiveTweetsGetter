import threading
from datetime import datetime

def write_log(message, console_print=False):
    with open('log.txt', mode='a', encoding='utf-8') as log_file:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        full_log_message = '[{}] - {}'.format(date, message)
        
        log_file.write(full_log_message)
        if(console_print):
            print(full_log_message)

def write_log_parallel(message, console_print):
    t = threading.Thread(target=write_log, args=(message, console_print))
    t.start()


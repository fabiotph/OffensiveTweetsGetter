import threading
import csv
import time

SLEEP_TIME = 0.3 #secs

def write_csv(queue, query):
    while True:
        if not queue.empty():
            rows = queue.get_nowait()
            if(rows is None):
                break
            with open('tweets.csv', mode='a', encoding='utf-8') as csv_file:
                csv_file_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                for row in rows:
                    csv_file_writer.writerow([row['id'], row['text'], query])
        else:
            time.sleep(SLEEP_TIME)

def write_csv_parallel(queue, query):
    t = threading.Thread(target=write_csv, args=(queue, query))
    t.start()


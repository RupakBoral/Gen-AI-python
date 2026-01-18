# Concurrency is executing a single task at a time but with faster context switching, so it appears to be running multiple tasks at once.

import threading 
import time
from datetime import datetime


def walk():
    for i in range(1, 5):
        time_india = datetime.now().astimezone()
        print(f"Walked {i} km at {time_india}")
        time.sleep(2)


def run():
    for i in range(1, 5):
        time_india = datetime.now().astimezone()
        print(f"Ran {i} km at {time_india}")
        time.sleep(3)


walk_thread = threading.Thread(target=walk, name='walk_thread')
run_thread = threading.Thread(target=run, name='run_thread')
    

walk_thread.start()
run_thread.start()

walk_thread.join()
run_thread.join()
# Global Interpreter Lock
# It is a mutex (lock) used by CPython (the standard Python interpreter) to ensure that only one thread executes Python bytecode at a time.
# Such situations can be avoided using GIL which assigns mutex to a particular thread, to avoid sharing with other threads.

import threading
import time

global count
count = 0

def counting():
    global count
    print(f"{threading.current_thread().name} Starting to count...")

    start_time = time.time()

    for _ in range(100_000_000):
        count = count + 1

    end_time = time.time()

    print(f"{threading.current_thread().name} Counting completed in {end_time - start_time:.2f}")

t1 = threading.Thread(target=counting, name="Thread 1")
t2 = threading.Thread(target=counting, name="Thread 2")

t1.start()
t2.start()

t1.join()
t2.join()

print(count)
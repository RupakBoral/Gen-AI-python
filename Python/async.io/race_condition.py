# a bug in systems where the outcome depends on the unpredictable timing of multiple threads or processes accessing and changing shared data, leading to inconsistent or incorrect results

import threading
import time 

chunk_id = 0

def increment():
    global chunk_id
    for _ in range(10_000):
        time.sleep(0)
        chunk_id += 1
    

threads = [threading.Thread(target=increment) for _ in range(20)]

for t in threads: t.start()

for t in threads: t.join()

print(chunk_id)
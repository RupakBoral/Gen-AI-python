# In multiprocessing, each thread has its own GIL, so it is faster

from multiprocessing import Process
import time

count = 0

def counting():
    global count
    print(f"Starting to count...")

    start_time = time.time()

    for _ in range(100_000_000):
        count = count + 1

    end_time = time.time()

    print(f"Counting completed in {end_time - start_time:.2f}")
    print(count)

if __name__ == "__main__":

    p1 = Process(target=counting, name="Process 1")
    p2 = Process(target=counting, name="Process 2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

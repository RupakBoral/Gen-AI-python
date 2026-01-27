from threading import Thread
import time

a = 10

def fn1():
    global a
    time.sleep(2)
    a = 3
    print("Hello from fn1")

def fn2():
    global a
    time.sleep(4)
    a = 6
    print("Hello from fn2")

t1 = Thread(target=fn1)
t2 = Thread(target=fn2)

t1.start()
t2.start()

print(f"1. a: {a}") # main thread doesnot wait for thread completion and prints

t2.join()

print(f"1. a: {a}") # main thread waits for completion of t2
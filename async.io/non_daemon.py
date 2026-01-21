import asyncio
import threading
import time

def logg_in():
    while True:
        time.sleep(1)
        print("Logs")
        

threading.Thread(target=logg_in, daemon=False).start()

time.sleep(3)
print("Done checking")
    
    

# Non-daemon threads continue to execute even after the main threads finishes it execution
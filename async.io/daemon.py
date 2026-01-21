import asyncio
import threading
import time

def logg_in():
    while True:
        time.sleep(1)
        print("Logs")
        
async def check():
    await asyncio.sleep(3)
    print("Done checking")
    

threading.Thread(target=logg_in, daemon=True).start()


asyncio.run(check())

# Daemon Threads finishes after the main threads execution finish
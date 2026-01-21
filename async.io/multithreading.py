# Seperate thread operates in this case, and the main thread with event loop stays free
# True Parallelism using MULTI-THREADING

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_item(item):
    # Thread blocking function
    print(f"Checking item: {item}")
    time.sleep(3)
    return f"Item: {item} is available"
    
async def main():
    # loop = asyncio.get_running_loop()
    # with ThreadPoolExecutor() as pool:
        # result = await loop.run_in_executor(pool, check_item, "Lenovo LOQ")  # ---> Same thing as below
        # print(result)
    result = await asyncio.to_thread(check_item, "Samsung")
    print(result)
    
asyncio.run(main())


# When to use:
# If it blocks and can’t be awaited, run it in an executor.


# With run_in_executor:
# Blocking work runs in another thread
# Async tasks stay responsive
# This is how you mix async code + legacy blocking code


# In one sentence
# 👉 Your code runs a slow, blocking function in a background thread so it doesn’t freeze the asyncio event loop.

# Multitasking with a single main thread
# Until one of the async operation is in progress other async operations can be executed, as soon as it finish the thread switch back and executes it

import asyncio

async def check_item(item):
    print("Checking item", item)
    await asyncio.sleep(2)    # async operation in progress
    print("Found the item", item)

async def other_task():
    for i in range(1, 4):
        print(f"Doing other work {i}")  # starts this async operation
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(check_item("Apple"))
    task2 = asyncio.create_task(other_task())

    await task1
    await task2

asyncio.run(main())

from threading import Thread
import requests
import time

def download_image(url):
    print("Starting to download image")
    res = requests.get(url=url)
    print(res)

urls = [
    'https://httpbin.org/image/jpeg',
    'https://httpbin.org/image/png',
    'https://httpbin.org/image/svg',
]

threads = []

start_time = time.time()

for url in urls:
    t = Thread(target=download_image, args=(url, ))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()
    
end_time = time.time()

print(f"All file downloded in {end_time - start_time:.2f} secs")
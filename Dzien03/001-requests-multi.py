
# Requests w wersji async
import requests
import grequests
import time
from multiprocessing.pool import ThreadPool

BASE_URL = "http://51.91.120.89/TABLICE/"
response = requests.get(BASE_URL)
lines = response.text.split("\n")
urls = [BASE_URL+line.strip() for line in lines[:10] ]
print(urls)

done_urls = []

def download_url(url):
    global done_urls
    r = requests.get(url, proxies={
        'http:' : 'http://127.0.0.1:5001',
        'https:' : 'http://127.0.0.1:5001',
    })
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as fd:
        fd.write(r.content)
        done_urls.append( (file_name,r.status_code) )
        print("save:",url)


ts1 = time.time()
result = ThreadPool(20).imap_unordered(download_url, urls)
for _ in result:
    pass
ts2 = time.time()
print(f"{ts2-ts1}")
print(done_urls)

ts1=time.time()
reqs = [grequests.get(url)  for url in urls]
result = grequests.map(reqs)
ts2=time.time()
print(f"{ts2-ts1}")

for r in result:
    file_name = r.url.split("/")[-1]
    with open("greq/" + file_name, "wb") as fd:
        fd.write(r.content)
        done_urls.append((file_name, r.status_code))
        print("save:", r.url)
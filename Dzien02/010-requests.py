
# Bilbioteka requests
import requests
from requests.auth import HTTPBasicAuth

response = requests.get("https://api.github.com/",
                        verify=False, allow_redirects=True,
                        timeout=(10, 30))
print(response.content)
print(response.text)
data_json = response.json()
print(data_json)

response = requests.get("https://api.github.com/search/repositories",
                        params={
                          "q" : "request+language:python"
                        },
                        headers = {
                            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0"
                        },
                        verify=False, allow_redirects=True,
                        timeout=(10, 30))

data_json = response.json()
print()

# HTTP / POST
response = requests.post("https://httpbin.org/post", data={
    "key1" : "value1",
    "key2" : "value2"
})
print(response.json())

# Basic-auth
url = "https://api.ambra.com.pl/j3GsmoZgcL/260/CQ02.png"
response = requests.get(url,
                        auth=HTTPBasicAuth("service","alamakota")
                        )
file_name = url.split("/")[-1]
with open( file_name, "wb") as fd:
    fd.write(response.content)
print(response)

# UPLOAD plików
with open("CQ02.png", "rb") as fd:
    upload_files = {
        "CQ02.png" : fd
    }
    response = requests.post("https://httpbin.org/post", files=upload_files)
    print(response.json())

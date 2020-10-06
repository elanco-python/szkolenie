
# Bilbioteka requests
import requests

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

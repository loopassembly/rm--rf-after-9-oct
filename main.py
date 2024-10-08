import requests
url="https://bit.ly/2560dsa"
response = requests.get(url)
print(response.text)
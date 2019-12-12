import requests

response = requests.get("http://www.naver.com").text
print(response)


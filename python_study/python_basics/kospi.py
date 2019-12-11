import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/marketindex/").text
soup = BeautifulSoup(response, 'html.parser')

# kospi = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value").text
# print(kospi)
kospi = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value")
print(kospi.text)
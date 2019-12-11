import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.naver.com").text
soup = BeautifulSoup(response, "html.parser")
word = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5)   a > span.ah_k")
for i in word :
    print(i.text)


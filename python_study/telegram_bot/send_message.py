import requests
import private
from decouple import config

#가져오기
token = private.token
app_url = f'https://api.telegram.org/bot{token}'

# token = config("TELEGRAM_BOT_TOKEN")
# app_url = f'https://api.telegram.org/bot{token}'

#응답내용 저장하기
update_url = f"{app_url}/getUpdates"
response = requests.get(update_url)
response = response.json()

#chat
chat_id = response.get("result")[0].get("message").get("chat").get("id")
# chat_id = private.chat_id
# chat_id = config("CHAT_ID")

# send message
message_url = f"{app_url}/sendMessage?chat_id={chat_id}&text=안녕하세요"
print(requests.get(message_url))

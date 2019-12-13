from decouple import config
import private
import requests

token = private.token
app_url = f'https://api.telegram.org/bot{token}'

set_webhook_url = f'{app_url}/setWebhook?url=https://didix.pythonanywhere.com/{token}'
#
# GET 방식
response = requests.get(set_webhook_url)
print(response.text)
from flask import Flask
from flask import request
from decouple import config
from flask import render_template
import requests
import private
import random

app =  Flask(__name__)

token = private.token

app_url = f'https://api.telegram.org/bot{token}'

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():

    message = request.args.get("message")

    update_url = f"{app_url}/getUpdates"
    response = requests.get(update_url)
    response = response.json()
    chat_id = response.get("result")[0].get("message").get("chat").get("id")

    message_url = f"{app_url}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(message_url)
    return "메세지 전송완료!"

@app.route(f"/{token}", methods=["POST"])
def telegram():

    from_telegram = request.get_json()
    
    chat_id = from_telegram.get("message").get("from").get('id')
    text = from_telegram.get("message").get("text")

    if from_telegram.get('message').get('photo') is not None:
        # 클로바 코드 요기에 작성!
        # 1. 우선 파일의 아이디 값을 가져온다.
        file_id = from_telegram.get('message')\
            .get('photo')[-1]\
            .get('file_id')
        # 2. 가져온 파일 아이디로 실제 파일을 가져온다.
        file_res = requests.get(f'{app_url}/getFile?file_id={file_id}')
        # 3. file path를 뽑아내서 저장
        file_path = file_res.json().get('result').get('file_path')
        
        # 4. 최종적으로 해당 파일의 경로를 찾아서 저장
        file_url = f'https://api.telegram.org/file/bot{token}/{file_path}'
        # 5. 사진(파일)이 있는 주소로 요청을 보내서 가져오자!
        real_file_res = requests.get(file_url, stream=True)

        headers = {
            'X-Naver-Client-Id': private.client_id,
            'X-Naver-Client-Secret': private.client_secret
        }
        clova_res = requests.post(
            'https://openapi.naver.com/v1/vision/celebrity',
            headers = headers,
            files = {
                'image': real_file_res.raw.read()
            }
        )
        
        # 닮은 유명인의 수가 있을 경우!
        if clova_res.json().get('info').get('faceCount'):
            celebrity = clova_res.json()\
                .get('faces')[0]\
                .get('celebrity')
            reply = f"{celebrity.get('value')}-{celebrity.get('confidence')*100}%"
        else:
            reply = '인식된 사람이 없습니다.'
    
    
    else:

        # lotto라고 입력하면 번호 출력하기 아니면 echo
        if text == "/lotto" :
            reply = random.sample(range(1,46),6)
            reply.sort()

        # 파파고 번역 (POST방식)
        elif text[0:4] == "/번역 " : #/번역 번역할문장
            headers = {
                "X-Naver-Client-Id" : private.client_id,
                "X-Naver-Client-Secret" : private.client_secret
            }

            data = {
                'source': 'en',
                'target': 'ko',
                'text': text[4:]
            }

            papago_url = "https://openapi.naver.com/v1/papago/n2mt"
            papago_res = requests.post(papago_url, data=data, headers=headers)
            papago_res = papago_res.json()
            reply = papago_res.get("message").get("result").get("translatedText")

        # elif 

        else :
            reply = text


    requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={reply}')
    return "", 200


if __name__ == '__main__':
    app.run(debug=True)

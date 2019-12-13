from flask import Flask
from flask import render_template
from flask import request
import requests
import random

app =  Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"



@app.route('/ascii')
def ascii():
    return render_template('ascii.html')

@app.route('/ascii_result')
def ascii_result():
    #1 word를 받아오는 명령어
    word = request.args.get('word')

    #2 받아온 word를 url주소로 넘겨주는 명령어
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}').text

    #3 template 폴더의 ascii_result.html을 불러오는 명령어
    return render_template('ascii_result.html', word=word, result=result)


@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    lotto_numbers = request.args.get('lotto_numbers')

    numbers = lotto_numbers.split()
    numbers_int = []

    for number in numbers:
        numbers_int.append(int(number))

    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = response.json()
    # drwtNo6 = lotto.get("drwtNo6")
    # print(drwtNo6)
    
    winner=[]
    match_count=0

    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    for number in numbers_int:
        for win_n in winner:
            if win_n == number:
                match_count +=1

    if match_count == 6:
        result="1등 당첨입니다!"

    #2 List Comprehension
    return render_template('lotto_result.html',
        lotto_round=lotto_round, 
        winner=winner, 
        numbers_int=numbers_int, 
        match_count=match_count,
        result = result
    )

    return render_template('lotto_result.html')


if __name__ == '__main__':
    app.run(debug=True)

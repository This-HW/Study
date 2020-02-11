#!/usr/bin/env python3
import cgi
from botengine import make_reply
# 입력 양식의 글자 추출하기 --- (※1)
form = cgi.FieldStorage()
# 메인 처리 --- (※2)
def main():
    m = form.getvalue("m", default="")
    if   m == "" : show_form()
    elif m == "say" : api_say()
# 사용자의 입력에 응답하기 --- (※3)
def api_say():
    print("Content-Type: text/plain; charset=euc-kr")
    print("")
    txt = form.getvalue("txt", default="")
    if txt == "": return
    res = make_reply(txt)
    print(res)
# 입력 양식 출력하기 --- (※4)
def show_form():
    print("Content-Type: text/html; charset=euc-kr")
    print("")
    print("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Machine-learning Chat-bot project</title>
        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
        <style>
            h1   { text-align: center; margin: 0px; }
            div  { padding:10px; border-radius: 10px; }
            span { 
              border-radius: 10px; 
              background-color: rgba(255, 255, 240, 0.342);
              padding:10px;
              padding-block-end : 0px; 
              padding-block-start: 0px;
              margin:5px; 
              text-size-adjust: auto; 
              flex:auto 
            }
            img  { max-width: 100%; display: flex; }
            .container {
              display: flex;
              flex-direction: column;
              width: 1;
              height: 1;
              align-items: stretch;
            }

            #chat{
              display: flex;
              flex-direction: column;  
            }
            .chat-container{
              display: flex;
              width: 100%;
              padding: 0px;
              align-self: center;
              max-width: 600px;
              flex-direction: column;
              background-color:lightgray;
            }
            .usr { 
              text-align: right; 
              display: flex;
              flex-direction: row;
            }
            .bot { 
              text-align: left; 
              display: flex;
              flex-direction: row;
            }
            .icon {
              flex: 0.1;
              margin: 0px;
              padding: 0px;
              align-items: center;

            }
            .talk {
              flex: 0.9;
              flex-direction: column;
              margin: 0px;
              padding: 0px;
            }
            .enter {
              display: flex;
              text-align: center;
              flex-direction: column;
              border-radius: 10px;
            }
            #txt-input{
              display: flex;
              flex: 1;
              border: 5px;
              padding: 3px;
            }
            #ent-button{
              display: flex;
              flex: 1;
              border: 5px;
              padding: 3px;
            }
        </style>
    </head>
    <body>
      <div class="container">
        <div class="chat-container">
          <div style="background-color: rgba(180, 180, 180, 0.863); border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;">
            <h1>Chat-bot with ML</h1>
          </div>
          <div id="chat">
            
          </div>
        <div class='enter'>
          <div id="txt-input">
            <input type="text" id="txt" style="height:30px; border-radius: 10px; flex: 100%; background-color: rgba(192, 192, 192, 0.61); border:0px;" onkeydown="check_ent();">
          </div>
          <div id="ent-button">
            <button onclick="say()" style="height:30px; border-radius: 10px; flex: 100%; background-color:rgba(192, 192, 192, 0.61); border:0px;" >전송</button>
          </div>
        </div>

        <script>
          var url = "./chatbot.py";
          var user_img = "";
          function check_ent(){
            if(event.keyCode == 13){
              say();  // 실행할 이벤트
            }
          }
          function say() {
            var txt = $('#txt').val();
            $.get(url, {"m":"say","txt":txt},
              function(res) {
                var html = "<div class='usr'><div class='talk'><div style='padding-bottom: 0px;'>user</div><span>" + esc(txt) +"</span></div> <div class='icon'><img src='https://postfiles.pstatic.net/MjAyMDAyMDlfMTE1/MDAxNTgxMjA0ODQzMjQz.HU0PUSRj9y-hdvi4KKPJuFROc99LqWDOXe66Ut6Yebgg.4C57msSUqNJfEMYJ8QqGnxF_wjD1em8MsEPhkZGlrYsg.PNG.didix/user_icon.png?type=w580'></div></div>" +
                "<div class='bot'> <div class='icon'> <img src='https://postfiles.pstatic.net/MjAyMDAyMDlfNDMg/MDAxNTgxMjA0ODIyMjQz.xWlq03vSHLQgGQCtEuP4AneKmsFPPtJj03v4I2-GKUUg.lPmpeU5Y00fV9JUFwZBlKqtXBJmEsayoKBw3SZ2DZ4kg.PNG.didix/chatbot_icon.png?type=w580'> </div> <div class='talk'> <div style='padding-bottom: 0px;'>chat_bot</div> <span>" + esc(res) + "</span></div></div>";
                $('#chat').html($('#chat').html()+html);
                $('#txt').val('').focus();
                document.body.scrollTop = document.body.scrollHeight;
              });
          }
          function esc(s) {
              return s.replace('&', '&amp;').replace('<','&lt;')
                      .replace('>', '&gt;');
          }
        </script>
      </div>
    </body>
    </html>
    """)
main()
from flask import Flask, render_template, request, flash, redirect
import requests, logging
from bs4 import BeautifulSoup

# Flask 객체 인스턴스 생성
app = Flask(__name__)
app.secret_key = 'asdf'


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userId = request.form.get('userId')
        userPw = request.form.get('userPw')

        print(f'아이디 :  {userId}, 패스워드 : {userPw}')

        if userId == '' or userPw == '':
            flash('아이디 혹은 비밀번호를 입력하지 않으셨습니다.')
            return render_template('login.html')
        else:
            flash('로그인 성공')
            return render_template('login.html')
    else:
        return render_template("login.html")


@app.route('/', methods=["GET"])
def index():
    return "zzz"


@app.route('/crawling')
def crawling():
    # 엔터치기
    req = requests.get('https://www.naver.com/')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []

    for i in soup.select(".theme_cont"):
        myList.append(i)
        print(i)

    return render_template("index.html", list=myList)


@app.route('/about')
def about():
    return "about World!"


if __name__ == '__main__':
    app.run()

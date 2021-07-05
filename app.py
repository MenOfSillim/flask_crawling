from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

# Flask 객체 인스턴스 생성
app = Flask(__name__)


@app.route('/')
def index():
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

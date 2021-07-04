from flask import Flask, render_template

# Flask 객체 인스턴스 생성
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/about')
def about():
    return "about World!"


if __name__ == '__main__':
    app.run()

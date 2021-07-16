from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_crawling" #2
mongo = PyMongo(app) #3

board = mongo.db.board #4
test = {
  "name": "test",
}
board.insert_one(test)
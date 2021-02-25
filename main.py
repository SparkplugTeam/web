# Python modules
import os

# Pip modules
from flask import *
import requests

# our fuckery
from datatypes.User import User
from datatypes.Post import Post
from datatypes.Category import Category

JSERV_URL = "http://localhost:4040"
API_KEY = "SparkPlug"
DB_NAME = "SparkPlug"

JSERV_HEADERS = {"x-api-key": API_KEY}

app = Flask(__name__)


@app.route("/")
def root():
    u = User("Yeet", "yoink", "hee@hoo.com")
    c = Category("aa", "aaaaaaaa", u)
    p = Post(u, c, "fuck", "shitass")
    return render_template("page.html", page="Home", content=p.renderPost())


@app.route("/jserv/new")
def newobj():
    nid = requests.request(
        "GET", JSERV_URL + "/query/newId?q=" + DB_NAME, headers=JSERV_HEADERS, data={}
    ).text
    return nid


app.run(host="0.0.0.0", port=8000, debug=True)

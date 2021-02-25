# Python modules
import os, json

# Pip modules
from sanic import Sanic
from sanic import response
from jinja2 import Template
import requests

# our fuckery
from datatypes.User import User
from datatypes.Post import Post
from datatypes.Category import Category


def template_html(name):
    return open("templates" + os.path.sep + name + ".html").read()


# Templates (for now)
main_template = Template(template_html("page"))

JSERV_URL = "http://localhost:4040"
API_KEY = "SparkPlug"
DB_NAME = "SparkPlug"

JSERV_HEADERS = {"x-api-key": API_KEY}

app = Sanic(name=__name__)

u = User("Yeet", "yoink", "hee@hoo.com")
c = Category("aa", "aaaaaaaa", u)
p = Post(u, c, "fuck", "shitass")


@app.route("/")
async def root(request):
    return response.html(main_template.render(page="Home", content=p.renderPost()))

# This bork
@app.route("/jserv/new")
async def newobj(request):
    nid = requests.request(
        "GET", JSERV_URL + "/query/newId?q=" + DB_NAME, headers=JSERV_HEADERS, data={}
    ).text
    print("ID is: " + nid)
    # Gets sad
    obj = json.dumps(p.__dict__)
    print(str(obj))
    return response.text(obj)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

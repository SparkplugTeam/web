from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template
from User import User
from Post import Post
from Category import Category
import os

def get_template(name):
    with open("templates" + os.path.sep + name) as f:
        return f.read() 

main = Template(get_template("page.html"))

app = FastAPI(default_response_class=HTMLResponse)

@app.get("/")
async def root():
    u = User("Yeet", "yoink", "hee@hoo.com")
    c = Category("aa", "aaaaaaaa", u)
    p = Post(u, c, "fuck", "shitass")
    return main.render(page="Home", content=p.renderPost())
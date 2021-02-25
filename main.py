from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template

import os

def get_template(name):
    with open("templates" + os.path.sep + name) as f:
        return f.read() 

main = Template(get_template("page.html"))

app = FastAPI(default_response_class=HTMLResponse)

@app.get("/")
async def root():
    print("heehoo")
    return main.render(page="Home", content="Heeho")
from flask import Flask

app = Flask("DRU")

@app.route("/")
def hello():
    return "Hello, World!"
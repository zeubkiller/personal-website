from flask import Flask, render_template

app = Flask("DRU")
app.config['EXPLAIN_TEMPLATE_LOADING']=True

@app.route("/")
@app.route("/index")
def hello():
    user = {"username" : "George"}
    return render_template('index.html', title="Home", user=user)

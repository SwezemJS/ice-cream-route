from flask import Flask, render_template
from markupsafe import escape
from conn import *
import json

app = Flask(__name__)

@app.route("/")
def index():
    rows = all() 
    text = ''
    for i in range(len(rows)):
        text += f"<a href='{rows[i][2]}'>{rows[i][0]}</a><br>"
    return text
    

@app.route("/<id>")
def hello(id):
    data = get_row(id)
    #return 'hi!'
    return render_template('index.html', data = data)

app.run(host='0.0.0.0', port=5000,debug=True)
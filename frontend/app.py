from flask import Flask,render_template
from flask import render_template
import requests,os,json
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)
app.secret_key=os.urandom(16).hex()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<id>")
def personal(id):
    return render_template("index2.html")


if __name__=='__main__':
    app.run(debug=True,port=8000)
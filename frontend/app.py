from flask import Flask,render_template
from flask import Blueprint,render_template,redirect,request,session,flash
import requests,os,json
# from server.decorators import login_required
from oauthlib.oauth2 import WebApplicationClient
from flask_cors import CORS
from dotenv import load_dotenv
from functools import wraps
import datetime
import time
load_dotenv()

app=Flask(__name__)
app.secret_key=os.urandom(16).hex()

# def login_required(a):
#     @wraps(a)
#     def wrap(*args,**kwargs):
#         if 'logged_in' in session and session['logged_in']:
#             return a(*args,**kwargs)
#         else:
#             # flash('請先登入')
#             return redirect('/login')
#     return wrap




# GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")
# GOOGLE_CLIENT_ID=os.environ['GOOGLE_CLIENT_ID']
# GOOGLE_CLIENT_SECRET=os.environ['SECRET']

# client = WebApplicationClient(GOOGLE_CLIENT_ID)
# available_emails=['timothychenpc@gmail.com','tim20060112@gmail.com']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<id>")
def personal(id):
    return render_template("index2.html")

# @app.route('/login')
# def login():
#     if '0' not in request.base_url:
#         request.base_url=request.base_url.replace('http','https')
        
#     print('base',request.base_url)
#     google_provider_cfg = get_google_provider_cfg()
#     authorization_endpoint = google_provider_cfg["authorization_endpoint"]
#     request_uri = client.prepare_request_uri(
#         authorization_endpoint,
#         redirect_uri=request.base_url + "/callback",
#         scope=["openid", "email", "profile"],
#     )
#     return redirect(request_uri)

# @app.route('/logout')
# def logout():
#     del session['logged_in']
#     print(session)
#     return redirect('/')

# @app.route("/login/callback")
# def callback():
#     if '0' not in request.base_url:
#         request.base_url=request.base_url.replace('http','https')
#         request.url=request.url.replace('http','https')
        
#     print(request.url,request.base_url)
#     google_provider_cfg = get_google_provider_cfg()
#     token_endpoint = google_provider_cfg["token_endpoint"]
#     # Get authorization code Google sent back to you
#     code = request.args.get("code")
#     print(code)
#     token_url, headers, body = client.prepare_token_request(token_endpoint,authorization_response=request.url,redirect_url=request.base_url,code=code)
#     token_response = requests.post(token_url,headers=headers,data=body,auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),)
#     client.parse_request_body_response(json.dumps(token_response.json()))

#     userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
#     print(userinfo_endpoint,'','')
#     uri, headers, body = client.add_token(userinfo_endpoint)
#     userinfo_response = requests.get(uri, headers=headers, data=body)
    
#     # Parse the tokens!
#     print(userinfo_response.json())
#     if userinfo_response.json().get("email_verified"):
#         users_email = userinfo_response.json()["email"]
#         if users_email in available_emails:
#             session['logged_in']=userinfo_response.json()
#         return redirect('/')

# def get_google_provider_cfg():
#     return requests.get(GOOGLE_DISCOVERY_URL).json()


if __name__=='__main__':
    app.run(debug=True,port=8000)
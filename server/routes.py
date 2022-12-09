from flask import Blueprint
app_route=Blueprint('app_route',__name__)

@app_route.route('/')
def home():
    pass
from logging import error
from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
import requests
import json

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('login.html' )

@app.route("/authenticate", methods=['POST'])
def authenticate():
    data= request.form
    url = "http://localhost:80/u/Android/v1/userLogin.php"
    payload={'email':data['mail'],
    'password': data['pwd']}
    files=[]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response_obj= json.loads(response.text)
    if(response_obj['error']==False):
        return render_template('panel.html')
    else:
        return render_template('login.html', alert=response_obj['message']) 


@app.route("/register", methods=['POST','GET'])
def register_user():
    if request.method!='POST':
        return render_template('signup.html')
    elif request.method=="POST":
        data=request.form
        x=data['birthdate']
        url = "http://localhost:80/u/Android/v1/registerUser.php"
        payload={'fname': data['fname'],
        'lname': data['lname'],
        'email': data['mail'],
        'password': data['pwd'],
        'dob': data['birthdate']}
        files=[ ]
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        response_obj= json.loads(response.text)
        if(response_obj['error']==False):
            return render_template('login.html', mail=data['mail'])
        else:
            return render_template('signup.html', alert=response_obj['message']) 

@app.route("/panel")
def panel():
    return render_template('panel.html' )

@app.route("/forgot-password",methods=['POST','GET'])
def password_reset():
    if request.method!="POST":
        return render_template('password-reset.html' )
    elif request.method=="POST":
        # handle password reset
        return render_template('password-reset.html' , resp="")


if __name__=="__main__":
    app.run(debug=True)
from flask import Flask,request
from user import User

app = Flask(__name__)
c_user = User()


@app.route('/ping')
def ping():
    return "pong"

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        res = c_user.login(username,password)
        if res == ():
            return "NO"
        else:
            return str(res)
    else:
        return "must be POST method"
@app.route('/get_lomba/<int:id_lomba>')
def get_lomba(id_lomba):
    return "lomba ke %s" % id_lomba
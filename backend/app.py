from flask import Flask,request
app = Flask(__name__)

@app.route('/ping')
def ping():
    return "pong"

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password=="admin":
            return "OK, berhasil"
        else:
            return "username atau password salah"
    else:
        return "must be POST method"
@app.route('/get_lomba/<int:id_lomba>')
def get_lomba(id_lomba):
    return "lomba ke %s" % id_lomba
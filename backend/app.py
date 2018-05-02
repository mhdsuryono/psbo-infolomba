from flask import Flask,request
from user import User
from lomba import Lomba
from chat import Chat

app = Flask(__name__)
c_user = User()
c_lomba = Lomba()
c_chat = Chat()

@app.route('/ping')
def ping():
    return "pong"
# user
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        res = c_user.login(email,password)
        if res == ():
            return "NO"
        else:
            return str(res)
    else:
        return "must be POST method"


@app.route('/buatAkun',methods=['POST','GET'])
def buatAkun():
    if request.method == "POST":
        nama = request.form["nama"]
        jenis_kelamin = request.form["jenis_kelamin"]
        email = request.form["email"]
        password = request.form["password"]
        universitas = request.form["universitas"]
        no_ktm = request.form["no_ktm"]
        res = c_user.buatAkun(nama,jenis_kelamin,email,password,universitas,no_ktm)
        if res:
            return "OK"
        else:
            return "FAIL"
    else:
        return "must be POST method"

@app.route('/hapusAkun',methods=['POST','GET'])
def hapusAkun():
    if request.method == "POST":
        id_user = request.form["id_user"]
        res = c_user.hapusAkun(id_user)
        if res:
            return "OK"
        else:
            return "NO"
    else:
        return "must be POST method"

@app.route('/updateAkun',methods=['POST','GET'])
def updateAKun():
    if request.method == "POST":
        id_user = request.form["id_user"]
        nama = request.form["nama"]
        jenis_kelamin = request.form["jenis_kelamin"]
        email = request.form["email"]
        universitas = request.form["universitas"]
        no_ktm = request.form["no_ktm"]
        password = request.form["password"]
        
        res = c_user.updateAkun(id_user, nama, jenis_kelamin, email, universitas, nomor_ktm, password)
        if res:
            return "OK"
        else:
            return "NO"
    else:
        return "must be POST method"


@app.route('/get_lomba/<int:id_lomba>')
def get_lomba(id_lomba):
    return "lomba ke %s" % id_lomba
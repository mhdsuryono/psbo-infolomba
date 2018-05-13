from __future__ import with_statement
from flask import Flask,request,jsonify
from user import User
from lomba import Lomba
from chat import Chat

app = Flask(__name__)
# c_user = User()
# c_lomba = Lomba()
# c_chat = Chat()

def jsn(val,mess):
    return jsonify(status=str(val),message=str(mess))

@app.route('/')
def  home():
    return "hai, ini backend loh<br>Coba ping dengan /ping<br>login dengan /login, metode=POST, param=(email,password)"

@app.route('/ping')
def ping():
    return "pong"
# user
@app.route('/login',methods=['POST'])
def login():
    with User() as c_user:
        data = request.get_json()
        try:
            email = data["email"]
            password = data["password"]
        except Exception, e:
            return jsn(0,e)
        res = c_user.login(email,password)
        if res == ():
            return jsn(0,"Not Found")
        else:
            return jsn(1,"")


@app.route('/buatAkun',methods=['POST'])
def buatAkun():
    with User() as c_user:
        data = request.get_json()
        nama = data["nama"]
        jenis_kelamin = data["jenis_kelamin"]
        email = data["email"]
        password = data["password"]
        universitas = data["universitas"]
        no_ktm = data["no_ktm"]
        res = c_user.buatAkun(nama,jenis_kelamin,email,password,universitas,no_ktm)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")
            

@app.route('/hapusAkun',methods=['POST'])
def hapusAkun():
    with User() as c_user:
        data = request.get_json()
        id_user = data["id_user"]
        res = c_user.hapusAkun(id_user)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")
        

@app.route('/updateAkun',methods=['POST'])
def updateAKun():
    with User() as c_user:
        data = request.get_json()
        id_user = data["id_user"]
        nama = data["nama"]
        jenis_kelamin = data["jenis_kelamin"]
        email = data["email"]
        universitas = data["universitas"]
        no_ktm = data["no_ktm"]
        password = data["password"]
        
        res = c_user.updateAkun(id_user, nama, jenis_kelamin, email, universitas, nomor_ktm, password)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")


@app.route('/updateLomba',methods=['POST'])
def updateLomba():
    with Lomba() as c_lomba:
        data = request.get_json()
        id_lomba = data["id_lomba"]
        nama_lomba = data["nama_lomba"]
        deskripsi = data["deskripsi"]
        tanggal_dibuat = data["tanggal_dibuat"]
        tanggal_mulai = data["tanggal_mulai"]
        tanggal_ditutup = data["tanggal_ditutup"]
        tempat = data["tempat"]
        biaya = data["biaya"]
        id_user = data["id_user"]
        res = c_lomba.updateLomba(self, id_lomba, nama_lomba, deskripsi, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, tempat, biaya, id_user)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")

@app.route('/hapusLomba',methods=['POST'])
def hapusLomba():
    with Lomba() as c_lomba:
        data = request.get_json()
        id_lomba = data["id_lomba"]
        res = c_lomba.hapusLomba(id_lomba)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")


@app.route('/buatLomba',methods=['POST'])
def buatLomba():
    with Lomba() as c_lomba:
        data = request.get_json()
        nama_lomba = data["nama_lomba"]
        deskripsi = data["deskripsi"]
        tanggal_dibuat = data["tanggal_dibuat"]
        tanggal_mulai = data["tanggal_mulai"]
        tanggal_ditutup = data["tanggal_ditutup"]
        tempat = data["tempat"]
        biaya = data["biaya"]
        id_user = data["id_user"]
        res = c_lomba.buatLomba(self, nama_lomba, deskripsi, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, tempat, biaya, id_user)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")

@app.route('/tambahChat',methods=['POST'])
def tambahChat():
    with Chat() as c_chat:
        data = request.get_json()
        id_pengirim = data["id_pengirim"]
        id_penerima = data["id_penerima"]
        pesan = data["pesan"]
        res = c_chat.tambahChat(self, id_pengirim, id_penerima, pesan)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")

@app.route('/hapusChat',methods=['POST'])
def hapusChat():
    with Chat() as c_chat:
        data = request.get_json()
        id_chat = data["id_chat"]
        res = c_chat.hapusChat(self,id_chat)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")
        

@app.route('/get_lomba/<int:id_lomba>')
def get_lomba(id_lomba):
    return "lomba ke %s" % id_lomba




@app.route('/upload',methods=['POST'])
def uplaod_foto():
    upload_folder = 'uploads'
    if 'file' not in request.files:
        return "no file"
    file = request.files['file']

    # http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
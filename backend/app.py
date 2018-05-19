from __future__ import with_statement
from flask import Flask,request,jsonify
from user import User
from lomba import Lomba
from chat import Chat
from adm_lomba import Adm_lomba
from anggota_lomba import Anggota_lomba
from pembayaran import Pembayaran

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# c_user = User()
# c_lomba = Lomba()
# c_chat = Chat()

def jsn(val,mess):
    return jsonify(status=str(val),message=str(mess))

def jsn_login(val,mess):
    return jsonify(status=str(val),id_user=str(mess))

def jsn_anggota(val,res):
    return jsonify(status=str(val),id_user=res)

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
        if res == None:
            return jsn(0,"Not Found")
        else:
            return jsn_login(1,res[0])


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
            return jsn(1,"sukses")
        else:
            return jsn(0,"")
            

@app.route('/hapusAkun',methods=['POST'])
def hapusAkun():
    with User() as c_user:
        data = request.get_json()
        id_user = data["id_user"]
        res = c_user.hapusAkun(id_user)
        if res:
            return jsn(1,"sukses")
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
        
        res = c_user.updateAkun(id_user, nama, jenis_kelamin, email, universitas, no_ktm, password)
        if res:
            return jsn(1,"sukses")
        else:
            return jsn(0,"")


@app.route('/updateLomba',methods=['POST'])
def updateLomba():
    with Lomba() as c_lomba:
        data = request.get_json()
        id_lomba = data["id_lomba"]
        nama_lomba = data["nama_lomba"]
        deskripsi = data["deskripsi"]
        tanggal_mulai = data["tanggal_mulai"]
        tanggal_ditutup = data["tanggal_ditutup"]
        tempat = data["tempat"]
        biaya = data["biaya"]
        max_anggota = data["max_anggota"]
        kategori = data["kategori"]
        id_user = data["id_user"]
        res = c_lomba.updateLomba( id_lomba, nama_lomba, deskripsi, tanggal_mulai, tanggal_ditutup, tempat, biaya, max_anggota,kategori, id_user)
        if res=="sukses":
            return jsn(1,"sukses")
        else:
            return jsn(0,res)

@app.route('/hapusLomba',methods=['POST'])
def hapusLomba():
    with Lomba() as c_lomba:
        data = request.get_json()
        id_lomba = data["id_lomba"]
        res = c_lomba.hapusLomba(id_lomba)
        if res == "sukses":
            return jsn(1,"sukses")
        else:
            return jsn(0,res[0])


@app.route('/buatLomba',methods=['POST'])
def buatLomba():
    with Lomba() as c_lomba:
        data = request.get_json()
        nama_lomba = data["nama_lomba"]
        deskripsi = data["deskripsi"]
        tanggal_mulai = data["tanggal_mulai"]
        tanggal_ditutup = data["tanggal_ditutup"]
        tempat = data["tempat"]
        biaya = data["biaya"]
        max_anggota = data["max_anggota"]
        kategori = data["kategori"]
        id_user = data["id_user"]
        res = c_lomba.buatLomba(nama_lomba, deskripsi, tanggal_mulai, tanggal_ditutup, tempat, biaya, max_anggota, kategori, id_user)
        if res=="sukses":
            return jsn(1,"sukses")
        else:
            return jsn(0,res)

@app.route('/daftarLomba',methods=['POST'])
def daftarLomba():
    with Adm_lomba() as c_adm:
        data = request.get_json()
        id_ketua = data["id_ketua"]
        id_lomba = data["id_lomba"]
        nama_tim = data["nama_tim"]
        res = c_adm.daftarLomba(id_ketua, id_lomba, nama_tim)
        if res=="sukses":
            return jsn(1,"sukses")
        else:
            return jsn(0,res)

@app.route('/tambahAnggota',methods=['POST'])
def tambahAnggota():
    with Anggota_lomba() as c_anggota:
        data = request.get_json()
        id_adm = data["id_adm"]
        id_anggota = data["id_anggota"]
        res = c_anggota.tambahAnggota(id_adm, id_anggota)
        if res=="sukses":
            return jsn(1,"sukses")
        else:
            return jsn(0,res)

@app.route('/hapusAnggota',methods=['POST'])
def hapusAnggota():
    with Anggota_lomba() as c_anggota:
        data = request.get_json()
        id_adm = data["id_adm"]
        id_anggota = data["id_anggota"]
        res = c_anggota.hapusAnggota(id_adm, id_anggota)
        if res=="sukses":
            return jsn(1,"sukses")
        else:
            return jsn(0,res)

@app.route('/getAnggota',methods=['POST'])
def getAnggota():
    with Anggota_lomba() as c_anggota:
        data = request.get_json()
        id_adm = data["id_adm"]
        res = c_anggota.getAnggota(id_adm)
        
        return jsn_anggota(1,res)
        

@app.route('/updateStatusBayar',methods=['POST'])
def updateStatusBayar():
    with Pembayaran() as pembayaran:
        data = request.get_json()
        id_ketua = data["id_ketua"]
        id_lomba = data["id_lomba"]
        status_pembayaran = data["status_pembayaran"]
        res = pembayaran.updateStatusBayar(id_ketua, id_lomba,status_pembayaran)
        if res=="sukses":
            return jsn(1,"sukses")
        else:
            return jsn(0,res)

@app.route('/getStatusBayar',methods=['POST'])
def getStatusBayar():
    with Pembayaran() as pembayaran:
        data = request.get_json()
        id_ketua = data["id_ketua"]
        id_lomba = data["id_lomba"]
        res = pembayaran.getStatusBayar(id_ketua, id_lomba)
        return jsn(1,res)


@app.route('/getLomba',methods=['POST'])
def getLomba():
    with Lomba() as lomba:
        resp = lomba.getLomba()
        list_lomba = [{"id_lomba":res[0],"nama_lomba":res[1],"deskripsi":res[2],"tanggal_dibuat":res[3],"tanggal_mulai":res[4],"tanggal_ditutup":res[5],"tempat":res[6],"biaya":res[7],"id_user":res[8],"max_anggota":res[9],"kategori":res[10]} for res in resp]
        return jsonify(list_lomba)

@app.route('/getPendaftar',methods=['POST'])
def getPendaftar():
    with Lomba() as lomba:
        data = request.get_json()
        id_lomba = data["id_lomba"]
        resp = lomba.getPendaftar(id_lomba)
        list_info = [{"id_adm":res[0],"id_ketua":res[1]} for res in resp]
        return jsonify(list_info)

@app.route('/tambahChat',methods=['POST'])
def tambahChat():
    with Chat() as c_chat:
        data = request.get_json()
        id_pengirim = data["id_pengirim"]
        id_penerima = data["id_penerima"]
        pesan = data["pesan"]
        res = c_chat.tambahChat( id_pengirim, id_penerima, pesan)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")

@app.route('/hapusChat',methods=['POST'])
def hapusChat():
    with Chat() as c_chat:
        data = request.get_json()
        id_chat = data["id_chat"]
        res = c_chat.hapusChat(id_chat)
        if res:
            return jsn(1,"")
        else:
            return jsn(0,"")


@app.route('/getProfile',methods=['POST'])
def getProfile():
    with User() as c_user:
        data = request.get_json()
        id_user = data["id_user"]
        resp = c_user.getProfile(id_user)

        if resp == None:
            return jsonify(status="0",message="not found")
        return jsonify(id_user=resp[0],nama=resp[1],jenis_kelamin=resp[2],email=resp[3],universitas=resp[4],nomor_ktm=resp[5],status_aktif=resp[6],status_akses=resp[7])

# @app.route('/upload/<jenis_foto>/<id>',methods=['POST'])
# def uplaod_foto(jenis_foto,id):
#     upload_folder = 'uploads'
#     jenis_foto = 
#     if 'file' not in request.files:
#         return "no file"
#     file = request.files['file']
    # buat folder berdasarkan jenis foto


    # http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
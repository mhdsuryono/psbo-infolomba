from __future__ import with_statement
from flask import Flask,request,jsonify,send_file
from user import User
from lomba import Lomba
from chat import Chat
from adm_lomba import Adm_lomba
from anggota_lomba import Anggota_lomba
from pembayaran import Pembayaran

from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = set(['jpg','jpeg'])

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

        resp = c_user.getProfile(str(res[0]))

        return jsonify(id_user=resp[0],nama=resp[1],jenis_kelamin=resp[2],email=resp[3],universitas=resp[4],no_ktm=resp[5],status_aktif=resp[6],status_akses=resp[7],status='1')


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
        email = data["email"]
        universitas = data["universitas"]
        no_ktm = data["no_ktm"]
        
        res = c_user.updateAkun(id_user, nama, "", email, universitas, no_ktm, "")
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

@app.route('/getLombaKategori',methods=['POST'])
def getLombaKategori():
    with Lomba() as lomba:
        data = request.get_json()
        kategori = data["kategori"]
        resp = lomba.getLombaKategori(kategori)
        list_lomba = [{"id_lomba":res[0],"nama_lomba":res[1],"deskripsi":res[2],"tanggal_dibuat":res[3],"tanggal_mulai":res[4],"tanggal_ditutup":res[5],"tempat":res[6],"biaya":res[7],"id_user":res[8],"max_anggota":res[9],"kategori":res[10]} for res in resp]
        return jsonify(list_lomba)

@app.route('/getLombaId',methods=['POST'])
def getLombaId():
    with Lomba() as lomba:
        data = request.get_json()
        id_user = data["id_user"]
        resp = lomba.getLombaId(id_user)
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
        # return status
        if res:
            return jsn(1,"OK")
        else:
            return jsn(0,"ERR")

@app.route('/hapusChat',methods=['POST'])
def hapusChat():
    with Chat() as c_chat:
        data = request.get_json()
        id_chat = data["id_chat"]
        res = c_chat.hapusChat(id_chat)
        if res:
            return jsn(1,"OK")
        else:
            return jsn(0,"ERR")

@app.route('/getChat',methods=['POST'])
def getChat():
    with Chat() as c_chat:
        data = request.get_json()
        id_1 = data["id_1"]
        id_2 = data["id_2"]
        resp = c_chat.getChat(id_1,id_2)
        list_chat = [{"id_chat":res[0],"id_pengirim":res[1],"id_penerima":res[2],"pesan":res[3],"tanggal":res[4],"status_baca":res[5]} for res in resp]
        return jsonify(list_chat)

@app.route('/semuaChat',methods=['POST'])
def semuaChat():
    with Chat() as c_chat:
        data = request.get_json()
        id_user = data["id_user"]
        list_id,list_nama = c_chat.semuaChat(id_user)
        resp = zip(list_id,list_nama)

        return jsonify(status=str(1),id_user=resp)

@app.route('/getProfile',methods=['POST'])
def getProfile():
    with User() as c_user:
        data = request.get_json()
        id_user = data["id_user"]
        resp = c_user.getProfile(id_user)

        if resp == None:
            return jsonify(status="0",message="not found")
        return jsonify(id_user=resp[0],nama=resp[1],jenis_kelamin=resp[2],email=resp[3],universitas=resp[4],no_ktm=resp[5],status_aktif=resp[6],status_akses=resp[7])



@app.route('/ubahPassword',methods=['POST'])
def ubahPassword():
    with User() as c_user:
        data = request.get_json()
        id_user = data["id_user"]
        passlama = data["passlama"]
        passbaru = data["passbaru"]
        
        res = c_user.ubahPassword(id_user, passlama, passbaru)
        if res:
            return jsn(1,"sukses")
        else:
            # berarti passlama salah
            return jsn(0,"")

@app.route('/getLombaSaya',methods=['POST'])
def getLombaSaya():
    with Anggota_lomba() as anggota_lomba:
        data = request.get_json()
        id_user = data["id_anggota"]
        resp = anggota_lomba.getLombaSaya(id_user)
        list_lomba = [{"id_lomba":res[0],"nama_lomba":res[1],"deadline":res[2]} for res in resp]
        return jsonify(list_lomba)


@app.route('/upload/<jenis_foto>/<nama_foto>',methods=['POST'])
def uploadPhoto(jenis_foto,nama_foto):
    upload_folder = 'uploads'
    jenis_foto = str(jenis_foto)
    nama_foto = str(nama_foto)
    if 'img' not in request.files:
        return "no file"
    file_get = request.files['img']
    file_location = upload_folder+"/"+jenis_foto+"/"+nama_foto
    
    if not os.path.exists(os.path.dirname(file_location)):
        os.makedirs(os.path.dirname(file_location))
    if os.path.isfile(file_location):
        os.remove(file_location)
    file_get.save(file_location)

    return jsn(1,"done")
    # buat folder berdasarkan jenis foto

@app.route('/getPhoto/<jenis_foto>/<nama_foto>',methods=['POST','GET'])
def getPhoto(jenis_foto,nama_foto):
    upload_folder = 'uploads'
    file_location = upload_folder+"/"+jenis_foto+"/"+nama_foto
    return send_file(file_location,mimetype='image/jpeg')


    # http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
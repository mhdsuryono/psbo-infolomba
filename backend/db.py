import MySQLdb

from peewee import *

db = MySQLDatabase("lombakampus", host="localhost", user="root", passwd="")

class Database:
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        
    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self,*arg):
        self.cursor.close()


class DB_Anggota_lomba(Model):
    id_adm = IntegerField(primary_key=True)
    id_anggota = IntegerField()

    class Meta:
        database = db
        db_table = 'anggota_lomba'

class DB_Adm_lomba(Model):
    id_adm = IntegerField(primary_key=True)
    id_ketua = IntegerField()
    id_lomba = IntegerField()
    nama_tim = CharField()
    status_penyisihan = IntegerField()

    class Meta:
        database = db
        db_table = 'adm_lomba'

class DB_Chat(Model):
    id_chat = IntegerField(primary_key=True)
    id_pengirim = IntegerField()
    id_penerima = IntegerField()
    pesan = TextField()
    tanggal = DateTimeField()
    status_baca = IntegerField()

    class Meta:
        database = db
        db_table = 'chat'

class DB_Lomba(Model):
    id_lomba = IntegerField(primary_key=True)
    nama_lomba = TextField()
    deskripsi = TextField()
    tanggal_dibuat = DateTimeField()
    tanggal_mulai = DateTimeField()
    tanggal_ditutup = DateTimeField()
    tempat = TextField()
    biaya = IntegerField()
    id_user = IntegerField()
    max_anggota = IntegerField()
    kategori = TextField()
    aturan = TextField()
    hadiah = TextField()

    class Meta:
        database = db
        db_table = 'lomba'

class DB_Pembayaran(Model):
    id_ketua = IntegerField(primary_key=True)
    id_lomba = IntegerField()
    status_pembayaran = IntegerField()

    class Meta:
        database = db
        db_table = 'pembayaran'

class DB_User(Model):
    id_user = IntegerField(primary_key=True)
    nama = CharField()
    jenis_kelamin = IntegerField()
    email = CharField()
    universitas = CharField()
    nomor_ktm = CharField()
    password = CharField()
    status_aktif = IntegerField()
    status_akses = IntegerField()
    no_hp = CharField()

    class Meta:
        database = db
        db_table = 'user'

from __future__ import with_statement

<<<<<<< HEAD
from db import Database
from anggota_lomba import Anggota_lomba

=======
from anggota_lomba import Anggota_lomba


class Adm_lomba:
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        
    def __enter__(self):
        self.cursor = self.db.cursor()
        return self
>>>>>>> 3a9a96438d4eccb2918a02d4505c11549b12887f

class Adm_lomba(Database):

    def daftarLomba(self, id_ketua, id_lomba, nama_tim):
        status_penyisihan = '0'
        nama_tim = '"'+nama_tim+'"';
        list_arg = [id_ketua, id_lomba, nama_tim, status_penyisihan]
        list_arg = [str(x) for x in list_arg]
        val = ','.join(list_arg)
        sql='insert into adm_lomba(id_ketua, id_lomba, nama_tim, status_penyisihan) values ('+val+')' 
        
        # cek duplikat
        self.cursor.execute('select count(*) from adm_lomba where id_ketua="'+str(id_ketua)+'" and id_lomba="'+str(id_lomba)+'"')
        num_count = self.cursor.fetchone()
        num_count = num_count[0]
        if num_count>0:
            return "duplicate ketua"
        try:
            self.cursor.execute(sql)
            self.db.commit()

            self.cursor.close()
            self.cursor = self.db.cursor()
            self.cursor.execute('select id_adm from adm_lomba where id_ketua="'+str(id_ketua)+'" and id_lomba="'+str(id_lomba)+'"') 
            id_adm = self.cursor.fetchone()[0]
            with Anggota_lomba() as c_anggota:
                id_anggota = id_ketua
                res = c_anggota.tambahAnggota(id_adm, id_anggota)
            return self.bayar_init(id_ketua,id_lomba)

        except Exception, e:
            self.db.rollback()
            return e

    def bayar_init(self, id_ketua, id_lomba):
        status_pembayaran = 0
        list_arg = [id_ketua,id_lomba,status_pembayaran]
        list_arg = ",".join(str(x) for x in list_arg)

        sql = 'insert into pembayaran(id_ketua, id_lomba, status_pembayaran) values ('+list_arg+')'
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return 'sukses'
        except Exception, e:
            self.db.rollback()
            return e





# with Adm_lomba() as a:
#     a.daftarLomba(1,1,"sapi team",0)

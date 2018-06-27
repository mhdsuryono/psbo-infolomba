from __future__ import with_statement

from db import *
from anggota_lomba import Anggota_lomba


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



    def updateStatusBayar(self, id_ketua, id_lomba,status_pembayaran):
        sql = 'update pembayaran set status_pembayaran='+str(status_pembayaran)+' where id_ketua='+str(id_ketua)+' and id_lomba='+str(id_lomba)+' ;'

        try:
            self.cursor.execute(sql)
            self.db.commit()
            return "sukses"
        except:
            self.db.rollback()
            return False

    def getStatusBayar(self,id_ketua,id_lomba):
        sql = 'select status_pembayaran from pembayaran where id_ketua='+str(id_ketua)+' and id_lomba='+str(id_lomba)+' ;'
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        return res[0]

# with Adm_lomba() as a:
#     a.daftarLomba(1,1,"sapi team",0)

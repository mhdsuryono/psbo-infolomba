from __future__ import with_statement
import MySQLdb

from lomba import Lomba


class Anggota_lomba:
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        
    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self,*arg):
        self.cursor.close()

    def tambahAnggota(self, id_adm,  id_anggota):
        sql='insert into anggota_lomba(id_adm, id_anggota) values ('+str(id_adm)+','+str(id_anggota)+')'
        self.cursor.execute('select count(*) from anggota_lomba where id_adm='+str(id_adm)+' and id_anggota='+str(id_anggota)+';')
        num_count = self.cursor.fetchone()[0]
        if num_count>0:
            return "duplicate member"
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return 'sukses'
        except Exception, e:
            self.db.rollback()
            return e 
        

    def hapusAnggota(self, id_adm, id_anggota):
        sql='delete from anggota_lomba where id_adm='+str(id_adm)+' and id_anggota='+str(id_anggota)+';'
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return 'sukses'
        except Exception, e:
            self.db.rollback()
            return e 
        

    def getAnggota(self,id_adm):
        sql = 'select id_anggota from anggota_lomba where id_adm='+str(id_adm)+';'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return [str(x[0]) for x in res]

    def getLombaSaya(self,id_anggota):
        sql = 'select id_adm from anggota_lomba where id_anggota='+str(id_anggota)+';'
        self.cursor.execute(sql)
        list_id_adm = self.cursor.fetchall()
        list_id_lomba = []
        hasil = []
        for id_adm in list_id_adm:
            list_id_lomba.append(self.getLombaByAdm(id_adm[0]))
        
        for id_lomba in list_id_lomba:
            with Lomba() as c_lomba:
                res = c_lomba.getLombaIdLomba(id_lomba)[0]
                print "---------------",res
                hasil.append([res[0],res[1],res[5]])
        print hasil
        return hasil


    def getLombaByAdm(self, id_adm):
        sql = 'select id_lomba from adm_lomba where id_adm='+str(id_adm)+';'
        self.cursor.execute(sql)
        res = self.cursor.fetchone()[0]
        return res

# with Anggota_lomba() as ang:
#     ang.getAnggota(4)
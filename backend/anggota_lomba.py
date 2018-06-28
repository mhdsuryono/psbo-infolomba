

from lomba import Lomba

from db import Database

from user import User


class Anggota_lomba(Database,Lomba,User):
    def tambahAnggota(self, id_adm,  email):
        id_anggota = self.getIdByEmail(email)
        if id_anggota == "gagal":
            return "gagal"
        self.cursor.execute('select count(*) from anggota_lomba where id_adm='+str(id_adm)+' and id_anggota='+str(id_anggota)+';')
        num_count = self.cursor.fetchone()[0]
        sql='insert into anggota_lomba(id_adm, id_anggota) values ('+str(id_adm)+','+str(id_anggota)+')'
        
        self.cursor.close()
        self.cursor = self.db.cursor()
        self.cursor.execute('select adm_lomba.id_lomba from adm_lomba inner join anggota_lomba on anggota_lomba.id_adm=adm_lomba.id_adm where anggota_lomba.id_anggota='+str(id_anggota))
        hasil = self.cursor.fetchone()
        # flag = False
        # print 'hasil',hasil
        # try:
        #     hasil = len(hasil)
        #     if hasil != None:
        #         flag = True
        #     if hasil > 0:
        #         flag = True
        # except:
        #     pass
        
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
        sql = 'select anggota_lomba.id_anggota, user.nama from anggota_lomba inner join user on anggota_lomba.id_anggota=user.id_user where anggota_lomba.id_adm='+str(id_adm)+';'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.cursor.close()
        self.cursor = self.db.cursor()
        # sql = 'select id_ketua from adm_lomba where id_adm='+str(id_adm)+';'
        sql = 'select user.nama from user inner join adm_lomba on user.id_user=adm_lomba.id_ketua where adm_lomba.id_adm='+str(id_adm)+';'
        self.cursor.execute(sql)
        res_ketua = self.cursor.fetchone()
        id_ketua = res_ketua[0]
        return res,id_ketua

        # 'select adm_lomba.id_adm,adm_lomba.id_ketua,adm_lomba.nama_tim,adm_lomba.id_lomba,lomba.nama_lomba from adm_lomba inner join lomba on adm_lomba.id_lomba=lomba.id_lomba where adm_lomba.id_lomba='+id_lomba+';'


# with Anggota_lomba() as ang:
#     ang.getAnggota(4)


from lomba import Lomba

from db import Database




class Anggota_lomba(Database,Lomba):
        
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



# with Anggota_lomba() as ang:
#     ang.getAnggota(4)
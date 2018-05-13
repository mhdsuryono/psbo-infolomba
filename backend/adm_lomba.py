from __future__ import with_statement
import MySQLdb

class Adm_lomba:
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        
    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self,*arg):
        self.cursor.close()

    def daftarLomba(self, id_ketua, id_lomba, nama_tim, status_penyisihan):
        status_penyisihan = '0'
        nama_tim = '"'+nama_tim+'"';
        list_arg = [id_ketua, id_lomba, nama_tim, status_penyisihan]
        list_arg = [str(x) for x in list_arg]
        val = ','.join(list_arg)
        sql='insert into adm_lomba(id_ketua, id_lomba, nama_tim, status_penyisihan) values ('+val+')' 
        
        # cek duplikat
        self.cursor.execute('select count(*) from adm_lomba where id_ketua="'+str(id_ketua)+'"')
        num_count = self.cursor.fetchone()[0]
        if num_count>0:
            print "duplikat"
            return False
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception, e:
            self.db.rollback()
            print "gasgal",e
            return False



with Adm_lomba() as a:
    a.daftarLomba(1,1,"sapi team",0)

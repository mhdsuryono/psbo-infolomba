import MySQLdb

class Anggota_lomba:
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        
    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self,*arg):
        self.cursor.close()

    def tambahAnggota(self, id_adm,  id_anggota):


    def hapusAnggota(self, id_adm, id_anggota):


    def getAnggota(id_adm):
        sql = 'select * from anggota_lomba where id_adm='+str(id_adm)+';'
        



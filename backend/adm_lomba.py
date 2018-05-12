import MySQLdb

class Adm_lomba:
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        
    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self,*arg):
        self.cursor.close()

    def daftarLomba(self,)



import MySQLdb

class Database:
    def __init__(self): #Melakukan konseksi ke database
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        
    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self,*arg): #Menutup koneksi dengan database
        self.cursor.close()

import MySQLdb

class Pembayaran:
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        

    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self,*arg):
        self.cursor.close()

    def updateStatusBayar(self, id_ketua, id_lomba,status_pembayaran):
        sql = ''

    def getStatusBayar(self):

from db import Database

class Pembayaran(Database):
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
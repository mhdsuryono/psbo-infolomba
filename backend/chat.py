import MySQLdb
import datetime

class Chat:
    # add db.close() after end
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        self.cursor = self.db.cursor()

    def tambahChat(self, id_pengirim, id_penerima, pesan):
        # tanggal auto
        tanggal = datetime.datetime.now().strftime("timestamp('%Y-%m-%d %H:%M:%S')")
        pesan = "'"+pesan+"'"
        list_arg = [str(id_pengirim), str(id_penerima), pesan, tanggal]
        val = ','.join(list_arg)
        sql='insert into chat(id_pengirim, id_penerima, pesan, tanggal, status_baca) values ('+val+',0)'
        # print sql
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("berhasil")
        except:
            print("error")
            self.db.rollback()
    def hapusCHat(self,id_chat):
        sql='delete from chat where id_chat='+str(id_chat)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("berhasil")
        except:
            print("error")
            self.db.rollback()

coba = Chat()
# coba.tambahChat(3,6,"makan yuk")
coba.hapusCHat(1)
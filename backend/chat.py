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
    def hapusChat(self,id_chat):
        sql='delete from chat where id_chat='+str(id_chat)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("berhasil")
        except:
            print("error")
            self.db.rollback()
    def getChat(self, id1, id2):

        sql='select * from chat where (id_pengirim='+str(id1)+' and id_penerima='+str(id2)+') or (id_pengirim='+str(id2)+' and id_penerima='+str(id1)+');'
        self.cursor.execute(sql)
        for i in self.cursor.fetchall():
            print i

coba = Chat()
# coba.tambahChat(3,4, "wah")
# coba.tambahChat(3,6,"makan yuk")
# coba.tambahChat(6,3,"yuk makan sekarang")
# coba.hapusChat(1)
# coba.getChat(3,6)
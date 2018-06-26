
import datetime
from db import Database
# inherit dari database

from user import User

class Chat(Database):
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
            return True
        except:
            self.db.rollback()
            return False
            
    def hapusChat(self,id_chat):
        sql='delete from chat where id_chat='+str(id_chat)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def getChat(self, id1, id2):

        sql='select * from chat where (id_pengirim='+str(id1)+' and id_penerima='+str(id2)+') or (id_pengirim='+str(id2)+' and id_penerima='+str(id1)+');'
        # tambah cek status, jika == 2 , dibuang
        # otomatis update status baca
        # status 0=unread, 1=read, 2= telah dihapus
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def semuaChat(self,  id_user):

        sql='select id_penerima,id_pengirim from chat where id_pengirim= '+str(id_user)+ ' or id_penerima='+str(id_user)+';'

        # tambah cek status, jika == 2 , dibuang
        # otomatis update status baca
        # status 0=unread, 1=read, 2= telah dihapus
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        set_id = set()
        for i in res:
            set_id.add(int(i[0]))
            set_id.add(int(i[1]))
        list_id = list(set_id)
        list_nama = []
        list_id.remove(int(id_user))
        self.cursor.close()
        self.cursor = self.db.cursor()

        for id_user in list_id:
            with User() as c_user:
                resp = c_user.getProfile(id_user)
                list_nama.append(resp[1])
        return list_id,list_nama

    # def semuaChat(self, id)
        # mengambil semua id2 yang pernah chat dengan kita(id)
        # diurutkan berdasarkan waktu chat terakhir

        # panggi hitungUnread
        # {{id="1",unread=4},{id="2",unerad=6},{}}

coba = Chat()

# coba.tambahChat(3,6,"makan yuk")
# coba.tambahChat(6,3,"yuk makan sekarang")
# coba.hapusChat(1)
# coba.getChat(3,6)
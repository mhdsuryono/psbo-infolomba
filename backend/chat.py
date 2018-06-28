import MySQLdb
import datetime
from db import *
# inherit dari database

from user import User

class Chat(Database,User):
    def tambahChat(self, id_pengirim, id_penerima, pesan):
       # tanggal auto
        tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pesan = "'"+pesan+"'"
        # print sql
        res = DB_Chat.insert(id_pengirim=id_pengirim,id_penerima=id_penerima,pesan=pesan,tanggal=str(tanggal),status_baca=0).execute()
       
        return True
  
    def hapusChat(self,id_chat):
        res = DB_Chat.get(DB_Chat.id_chat==id_chat).delete_instance()
        return "1"

    # not
    def getChat(self, id1, id2):
        res = DB_Chat.select().where((DB_Chat.id_pengirim==str(id1) | (DB_Chat.id_pengirim==str(id2))) & (DB_Chat.id_penerima==str(id1) | (DB_Chat.id_penerima==str(id2))) )
        return res

    def semuaChat(self,  id_kita):

        sql='select id_penerima,id_pengirim from chat where id_pengirim= '+str(id_kita)+ ' or id_penerima='+str(id_kita)+';'

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
        list_resp = []
        list_id.remove(int(id_kita))
        self.cursor.close()
        self.cursor = self.db.cursor()

        for id_user in list_id:
            last = self.lastChat(id_user, id_kita)
            resp = self.getProfile(id_user)
            if resp == None:
                resp = ["",""]
            list_resp.append({'id_user':id_user,'nama':resp[1],'pesan':last[0],'tanggal':last[1],'status_baca':last[2]})
        return list_resp

    # def semuaChat(self, id)
        # mengambil semua id2 yang pernah chat dengan kita(id)
        # diurutkan berdasarkan waktu chat terakhir

        # panggi hitungUnread
        # {{id="1",unread=4},{id="2",unerad=6},{}}

    def lastChat(self, id_1,id_2):
        sql='select pesan, tanggal,status_baca from chat where id_pengirim= '+str(id_1)+ ' and id_penerima='+str(id_2)+' or id_pengirim='+str(id_2)+' and id_penerima='+str(id_1)+' order by tanggal;'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res[-1]

# coba = Chat()

# coba.tambahChat(3,6,"makan yuk")
# coba.tambahChat(6,3,"yuk makan sekarang")
# # coba.hapusChat(1)
# print coba.lastChat(6,3)
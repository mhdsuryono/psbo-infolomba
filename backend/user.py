import MySQLdb

class User:
    # add db.close() after end
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        self.cursor = self.db.cursor()

    def buatAkun(self,nama, jenis_kelamin, email, password, universitas, no_ktm ):
        status_aktif = '1'
        status_akses = '0'
        list_arg = [nama,jenis_kelamin,email,universitas,no_ktm,password,status_aktif,status_akses]
        val = '","'.join(list_arg)
        sql='insert into user(nama,jenis_kelamin,email,universitas,nomor_ktm,password,status_aktif,status_akses) values ("'+val+'")' 
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False



    def hapusAkun(self,id_user):
        sql='update user set status_aktif=0 where id_user='+str(id_user)+';'
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def updateAKun(self,id_user, nama, jenis_kelamin, email, universitas, nomor_ktm, password):
        list_arg=[nama, jenis_kelamin, email, universitas, nomor_ktm, password]
        val_arg=[]
        if list_arg[0]!="":
            val_arg.append("nama='"+nama+"'")
        if list_arg[1]!="":
            val_arg.append("jenis_kelamin='"+jenis_kelamin+"'")
        if list_arg[2]!="":
            val_arg.append("email='"+email+"'")
        if list_arg[3]!="":
            val_arg.append("universitas='"+universitas+"'")
        if list_arg[4]!="":
            val_arg.append("nomor_ktm='"+nomor_ktm+"'")
        if list_arg[5]!="":
            val_arg.append("password='"+password+"'")

        val=','.join(val_arg)
        sql='update user set '+val+' where id_user='+str(id_user)+';'

        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    # def geta(self):
    #     sql='select * from user'
    #     self.cursor.execute(sql)
    #     for i in self.cursor.fetchall():
    #         print i
    def login(self,username,password):
        username = str(username)
        password = str(password)
        sql='select * from user where email="'+username+'" and password="'+password+'" limit 1'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        # if res == ():
        #     print "no"
        # else:
        #     print "ok"
        #     print res
        return res  
# buatAkun("kevin","1","kebin@gmail.com","1234","IPB","G645")
# hapusAkun(2)
# updateAKun(1,"","","","UI","","")
# coba = User()
# coba.login("nino@gmail.com","1234")

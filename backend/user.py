from db import Database

class User(Database):

    def buatAkun(self,nama, jenis_kelamin, email, password, universitas, no_ktm ,no_hp): #Membuat akun
        status_aktif = '1'
        status_akses = '0'

        list_arg = [nama,jenis_kelamin,email,universitas,no_ktm,password,status_aktif,status_akses,str(no_hp)]
        val = '","'.join(list_arg)
        sql='insert into user(nama,jenis_kelamin,email,universitas,nomor_ktm,password,status_aktif,status_akses,no_hp) values ("'+val+'")' 
        
        # cek duplikat
        self.cursor.execute('select count(*) from user where email="'+email+'"')
        num_count = self.cursor.fetchone()[0]
        if num_count>0:
            print num_count
            return False
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False



    def hapusAkun(self,id_user): #Menghapus Akun Kita
        sql='update user set status_aktif=0 where id_user='+str(id_user)+';'
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def updateAkun(self,id_user, nama, jenis_kelamin, email, universitas, no_ktm, password,no_hp): #Update informasi akun
        list_arg=[nama, jenis_kelamin, email, universitas, no_ktm, password,str(no_hp)]
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
            val_arg.append("nomor_ktm='"+no_ktm+"'")
        if list_arg[5]!="":
            val_arg.append("password='"+password+"'")
        if list_arg[6]!="":
            val_arg.append("no_hp='"+str(no_hp)+"'")

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
    def login(self,username,password): #Login kedalam sistem
        username = str(username)
        password = str(password)
        sql='select id_user from user where email="'+username+'" and password="'+password+'" and status_aktif=1;'
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        # if res == ():
        #     print "no"
        # else:
        #     print "ok"
        #     print res
        # print res
        return res

    def getProfile(self,id_user): #Mendapatkan profil untuk ditampilkan
        sql = 'select * from user where id_user='+str(id_user)+';'
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        return res

    def getIdByEmail(self,email): #Mendapatkan ID dari email user
        sql = 'select id_user from user where email="'+str(email)+'" and status_aktif=1 ;'
        try: 
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
        except:
            return "gagal"
        if res == None:
            return "gagal"
        return res[0]

    def ubahPassword(self,id_user, passlama,passbaru): #Ganti password
        sql='select id_user from user where id_user="'+str(id_user)+'" and password="'+passlama+'" and status_aktif=1;'
        self.cursor.execute(sql)
        res = self.cursor.fetchone()

        if res != None:
            sql='update user set password="'+passbaru+'" where id_user='+str(id_user)+';'
            try:
                self.cursor.execute(sql)
                self.db.commit()
                return True
            except:
                print "erro didisini"
                self.db.rollback()
                return False
        else:
            return False


# a = User()
# a.buatAkun("kevin","1","kebin@gmail.com","1234","IPB","G645")
# hapusAkun(2)
# updateAKun(1,"","","","UI","","")
# coba = User()
# coba.login("nino@gmail.com","1234")

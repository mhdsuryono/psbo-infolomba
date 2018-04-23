import MySQLdb

class Lomba:
    # add db.close() after end
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        self.cursor = self.db.cursor()


    def buatLomba(self, nama_lomba, deskripsi, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, tempat, biaya, id_user):

        list_arg = [nama_lomba, deskripsi, tempat ]
        list_arg2 = [tanggal_dibuat, tanggal_mulai, tanggal_ditutup, str(biaya), str(id_user)]
        val = '","'.join(list_arg)+'",' + ','.join(list_arg2)
        sql='insert into lomba(nama_lomba, deskripsi, tempat, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, biaya, id_user) values ("'+val+')' 
        # print sql
        # try:
        self.cursor.execute(sql)
        self.db.commit()
        print("berhasil")
        # except:
        print("error")
        self.db.rollback()

    def hapusLomba(self,id_lomba):
        sql='update lomba set id_user=0 where id_lomba='+str(id_lomba)+';'
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("berhasil")
        except:
            print("error")
            self.db.rollback()

    def updateLomba(self, id_lomba, nama_lomba, deskripsi, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, tempat, biaya, id_user):
        list_arg=[nama_lomba, deskripsi, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, tempat, str(biaya), str(id_user)]
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
            print("berhasil")
        except:
            print("error")
            self.db.rollback()

coba = Lomba()
coba.buatLomba("lomba catur","main catur dan lain-lain","2000/12/12","21/8/1999","22/8/2000","IPB",2000,2)
# belom - semua, error di date
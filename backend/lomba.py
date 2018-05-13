import MySQLdb
import datetime
class Lomba:
    def __init__(self):
        self.db = MySQLdb.connect("localhost","root","","lombakampus")
        

    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self,*arg):
        self.cursor.close()

    def buatLomba(self, nama_lomba, deskripsi, tanggal_mulai, tanggal_ditutup, tempat, biaya, max_anggota, kategori,id_user):
        tanggal_mulai = "timestamp('"+ tanggal_mulai +"')"
        tanggal_dibuat = "timestamp('"+ str(datetime.datetime.now()) +"')"
        tanggal_ditutup = "timestamp('"+ tanggal_ditutup +"')"
        list_arg = [nama_lomba, deskripsi, tempat,kategori ]
        list_arg2 = [tanggal_dibuat, tanggal_mulai, tanggal_ditutup, str(biaya),str(max_anggota), str(id_user)]
        val = '","'.join(list_arg)+'",' + ','.join(list_arg2)
        sql='insert into lomba(nama_lomba, deskripsi, tempat,kategori, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, biaya,max_anggota, id_user) values ("'+val+')' 
        # print sql
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return "sukses"
        except Exception, e:
            self.db.rollback()
            return e

    def hapusLomba(self,id_lomba):
        sql='update lomba set id_user=0 where id_lomba='+str(id_lomba)+';'
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception, e:
            self.db.rollback()
            return e

        # delete anggota juga nanti
        return "sukses"

    def updateLomba(self, id_lomba, nama_lomba, deskripsi, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, tempat, biaya, id_user):
        list_arg=[nama_lomba, deskripsi, tanggal_dibuat, tanggal_mulai, tanggal_ditutup, tempat, str(biaya), str(id_user)]
        val_arg=[]
        if list_arg[0]!="":
            val_arg.append("nama_lomba='"+nama_lomba+"'")
        if list_arg[1]!="":
            val_arg.append("deskripsi='"+deskripsi+"'")
        if list_arg[2]!="":
            tanggal_dibuat = "timestamp('"+ tanggal_dibuat +"')"
            val_arg.append("tanggal_dibuat='"+tanggal_dibuat+"'")
        if list_arg[3]!="":
            tanggal_mulai = "timestamp('"+ tanggal_mulai +"')"
            val_arg.append("tanggal_mulai='"+tanggal_mulai+"'")
        if list_arg[4]!="":
            tanggal_ditutup = "timestamp('"+ tanggal_ditutup +"')"
            val_arg.append("tanggal_ditutup='"+tanggal_ditutup+"'")
        if list_arg[5]!="":
            val_arg.append("tempat='"+tempat+"'")
        if list_arg[6]!="":
            val_arg.append("biaya='"+str(biaya)+"'")
        if list_arg[7]!="":
            val_arg.append("id_user='"+str(id_user)+"'")

        val=','.join(val_arg)
        sql='update lomba set '+val+' where id_lomba='+str(id_lomba)+';'

        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("berhasil")
        except:
            print("error")
            self.db.rollback()

    # administrasi lomba
    def daftarLomba(self, id_lomba, id_ketua):
        id_lomba = str(id_lomba)
        id_ketua = str(id_ketua)
        # sql = 'insert into lomba()'
    def tambahAnggota(self,id_lomba, id_ketua, id_user):
        id_lomba = str(id_lomba)
        id_ketua = str(id_ketua)
        id_user = str(id_user)


# coba = Lomba()
# coba.buatLomba("lomba catur","main catur dan lain-lain","2017-06-15 09:34:21","2017-08-15 09:00:00","2017-06-15","IPB",2000,2)
# coba.updateLomba(8,"lomba programming", "","","","","di rumahku",100,1)
# coba.hapusLomba(8)

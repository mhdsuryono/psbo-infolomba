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

    def updateLomba(self, id_lomba, nama_lomba, deskripsi, tanggal_mulai, tanggal_ditutup, tempat, biaya, max_anggota, kategori, id_user):
        list_arg=[nama_lomba, deskripsi, tanggal_mulai, tanggal_ditutup, tempat, str(biaya),  str(max_anggota), kategori, str(id_user)]
        val_arg=[]
        if list_arg[0]!="":
            val_arg.append("nama_lomba='"+nama_lomba+"'")
        if list_arg[1]!="":
            val_arg.append("deskripsi='"+deskripsi+"'")
        if list_arg[2]!="":
            tanggal_mulai = "timestamp('"+ tanggal_mulai +"')"
            val_arg.append("tanggal_mulai='"+tanggal_mulai+"'")
        if list_arg[3]!="":
            tanggal_ditutup = "timestamp('"+ tanggal_ditutup +"')"
            val_arg.append("tanggal_ditutup='"+tanggal_ditutup+"'")
        if list_arg[4]!="":
            val_arg.append("tempat='"+tempat+"'")
        if list_arg[5]!="":
            val_arg.append("biaya='"+str(biaya)+"'")
        if list_arg[6]!="":
            val_arg.append("max_anggota='"+str(max_anggota)+"'")
        if list_arg[7]!="":
            val_arg.append("kategori='"+kategori+"'")
        if list_arg[8]!="":
            val_arg.append("id_user='"+str(id_user)+"'")

        val=','.join(val_arg)
        sql='update lomba set '+val+' where id_lomba='+str(id_lomba)+';'

        try:
            self.cursor.execute(sql)
            self.db.commit()
            return "sukses"
        except Exception,e:
            self.db.rollback()
            return e

    def getLomba(self):
        tanggal_sekarang = "timestamp('"+ str(datetime.datetime.now()) +"')"
        sql = 'select * from lomba where tanggal_ditutup>'+tanggal_sekarang+';'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def getLombaKategori(self,kategori):
        tanggal_sekarang = "timestamp('"+ str(datetime.datetime.now()) +"')"
        sql = 'select * from lomba where tanggal_ditutup>'+tanggal_sekarang+' and kategori="'+kategori+'";'
        print (sql)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def getLombaId(self,id_user):
        tanggal_sekarang = "timestamp('"+ str(datetime.datetime.now()) +"')"
        sql = 'select * from lomba where id_user='+str(id_user)+';'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def getPendaftar(self,id_lomba):
        sql = 'select id_adm,id_ketua from adm_lomba where id_lomba='+id_lomba+';'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()

        return res

    def getLombaIdLomba(self,id_lomba):
        tanggal_sekarang = "timestamp('"+ str(datetime.datetime.now()) +"')"
        sql = 'select * from lomba where tanggal_ditutup>'+tanggal_sekarang+' and id_lomba="'+str(id_lomba)+'";'
        print "dari sql",sql
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res


# coba = Lomba()
# coba.buatLomba("lomba catur","main catur dan lain-lain","2017-06-15 09:34:21","2017-08-15 09:00:00","2017-06-15","IPB",2000,2)
# coba.updateLomba(8,"lomba programming", "","","","","di rumahku",100,1)
# coba.hapusLomba(8)

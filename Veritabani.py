import sqlite3

vt=sqlite3.connect("PyPara.db")
cursor=vt.cursor()
# komut="""Create table tb_altin(
# id INTEGER NOT NULL UNIQUE,
# zaman NVARCHAR(250) NOT NULL,
# kur REAL NOT NULL,
# PRIMARY KEY(id AUTOINCREMENT)
# )"""

# komut="""Create table tb_dolar(
# id INTEGER NOT NULL UNIQUE,
# zaman NVARCHAR(250) NOT NULL,
# kur REAL NOT NULL,
# PRIMARY KEY(id AUTOINCREMENT)
# )"""

# komut="""Create table tb_euro(
# id INTEGER NOT NULL UNIQUE,
# zaman NVARCHAR(250) NOT NULL,
# kur REAL NOT NULL,
# PRIMARY KEY(id AUTOINCREMENT)
# )"""
# cursor.execute(komut)
# vt.close()


class Veritabani:
    @staticmethod
    def Kaydet(komut):
        vt=sqlite3.connect("PyPara.db")
        try:
            cursor=vt.cursor()
            cursor.execute(komut)
            vt.commit()
            print("Kayit Başarili")
        except:
            print("Kayit Sirasinda Bir Hata Oluştu!!")
        vt.close()

    @staticmethod
    def KurGetir(komut):
        try:
            vt = sqlite3.connect("PyPara.db")
            cursor = vt.cursor()
            cursor.execute(komut)
            listekur=cursor.fetchall()
            listekur.reverse()
            vt.close()
            return listekur
        except:
            print("Kur Çekilirken Bir Hata Oluştu!!")





from tkinter import *
from tkinter.ttk import *
import datetime
from Veritabani import Veritabani
from Grafik import Grafik
import threading
from Kur import Kur


class Doviz:
    pencere=Tk()
    tab_control=Notebook(pencere)
    tab_altin=Frame(tab_control)
    tab_dolar=Frame(tab_control)
    tab_euro=Frame(tab_control)

    tab_control.add(tab_altin,text="Altın")
    tab_control.add(tab_dolar,text="Dolar")
    tab_control.add(tab_euro,text="Euro")

    tab_control.grid(row=0,column=0,ipadx=10,ipady=10)

    @classmethod
    def zamanFormat(cls,zamanStr):
        zamanKisa=[]
        for z in zamanStr:
            zmn=datetime.datetime.strptime(z,"%d.%m.%Y %H:%M:%S")
            zmn=zmn.strftime("%d.%m %H:%M")
            zamanKisa.append(zmn)
        return zamanKisa

    @classmethod
    def tekrar(cls):
        komut="Select zaman,kur from tb_altin order by(zaman) desc"
        altinKur=Veritabani.KurGetir(komut)
        x=[row[0] for row in altinKur] #[(12.12.2021,768.45),(12.12.2021,768.36),(12.12.2021,768.46),]
        xf=cls.zamanFormat(x)
        y=[row[1] for row in altinKur]
        Grafik.Ciz(cls.tab_altin,xf,y,"Altın Kuru")

        komut = "Select zaman,kur from tb_dolar order by(zaman) desc"
        dolarKur = Veritabani.KurGetir(komut)
        x = [row[0] for row in dolarKur]  # [(12.12.2021,768.45),(12.12.2021,768.36),(12.12.2021,768.46),]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in dolarKur]
        Grafik.Ciz(cls.tab_dolar, xf, y, "Dolar Kuru")

        komut = "Select zaman,kur from tb_euro order by(zaman) desc"
        euroKur = Veritabani.KurGetir(komut)
        x = [row[0] for row in euroKur]  # [(12.12.2021,768.45),(12.12.2021,768.36),(12.12.2021,768.46),]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in euroKur]
        Grafik.Ciz(cls.tab_euro, xf, y, "Euro Kuru")


        altin=threading.Thread(target=Kur.Getir,args=["altin"])
        dolar=threading.Thread(target=Kur.Getir,args=["dolar"])
        euro=threading.Thread(target=Kur.Getir,args=["euro"])

        altin.start()
        dolar.start()
        euro.start()

        cls.pencere.after(30000,cls.tekrar)


altin = threading.Thread(target=Kur.Getir, args=["altin"])
dolar = threading.Thread(target=Kur.Getir, args=["dolar"])
euro = threading.Thread(target=Kur.Getir, args=["euro"])

altin.start()
dolar.start()
euro.start()

Doviz.tekrar()
Doviz.pencere.mainloop()
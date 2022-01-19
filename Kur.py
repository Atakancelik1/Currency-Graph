from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Veritabani import Veritabani


class Kur:
    @staticmethod
    def Getir(doviztipi):
        driver_path="chromedriver.exe"
        opsiyonlar=Options()
        opsiyonlar.add_argument("--headless")
        browser = webdriver.Chrome(executable_path=driver_path, options=opsiyonlar)
        browser.get("https://www.haberturk.com/")
        if(doviztipi=="altin"):
            icerik=browser.find_element_by_css_selector("a#gram-altin span:nth-child(2)").text
            print(icerik)
        if (doviztipi == "dolar"):
            icerik = browser.find_element_by_css_selector("a#dolar span:nth-child(2)").text
        if (doviztipi == "euro"):
            icerik = browser.find_element_by_css_selector("a#euro span:nth-child(2)").text

        deger = float(icerik.replace(",","."))
        tablo="tb_"+str(doviztipi)
        zaman = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        komut=f"Insert into {tablo} (zaman,kur) values ('{zaman}','{deger}')"
        Veritabani.Kaydet(komut)
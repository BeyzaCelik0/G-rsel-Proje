from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, \
    QStackedWidget,QMessageBox
from PyQt6.QtGui import QDesktopServices, QIntValidator
from PyQt6.QtCore import QUrl
from pymongo import MongoClient
from anasayfa import anasayfa
from hastagiris import hastagirissayfa
from diyetisyengiris import diyetisyengiris
from diyetisyenanasayfa import diyetisyenanasayfa
from hastakayit import hastakayit
from parolasifirlama import parolasifirlama
from hastaanasayfa import hastaanasayfa
from hesaplama import hesaplama
from diyetornegi1 import diyetornegi1
from randevu import randevu

from vucutkitle import vucutkitle
from bazalmet import bazalmet
from idealkilo import idealkilo
from gunlukkalori import gunlukkalori

import sys
import  resimler

#üsttekileri kendinize göre entegre edin

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['Diyetisyen'] #kendi database isminiz
        self.diyetisyen_collection = self.db['Diyetisyenler']#kendi database koleksiyon isminiz
        self.hasta_collection = self.db['Hastalar']#kendi database koleksiyon isminiz
        self.vlayout = QVBoxLayout(self)
        self.vlayout.setContentsMargins(0, 0, 0, 0) # Sağdan, soldan, yukarıdan veya aşağıdan fark bırakmaması için yapıyoruz yani garip gözükmesin diye
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setContentsMargins(0, 0, 0, 0) # Sağdan, soldan, yukarıdan veya aşağıdan fark bırakmaması için yapıyoruz yani garip gözükmesin diye
        self.vlayout.addWidget(self.stackedWidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(500,500))


        self.anasayfawidget = QWidget()#sayfalarınızın widget isimleri (bunların sıralaması sayfa numaraları olarak kullanılacak örneğin widget 0,mainwidget 1)
        self.hastagiriswidget = QWidget()
        self.diyetisyengiriswidget = QWidget()
        self.diyetisyenanasayfawidget = QWidget()
        self.hastakayitwidget = QWidget()
        self.parolasifirlamawidget = QWidget()
        self.hastaanasayfawidget = QWidget()
        self.hesaplamawidget = QWidget()
        self.vucutkitlewidget = QWidget()
        self.bazalmetwidget = QWidget()
        self.idealkilowidget = QWidget()
        self.gunlukkaloriwidget = QWidget()
        self.diyetornegi1widget = QWidget()
        self.randevuwidget = QWidget()


        self.stackedWidget.addWidget(self.anasayfawidget)#sayfasınız stacked widgeta ekleyin
        self.stackedWidget.addWidget(self.hastagiriswidget)#sayfasınız stacked widgeta ekleyin
        self.stackedWidget.addWidget(self.diyetisyengiriswidget)
        self.stackedWidget.addWidget(self.hastakayitwidget)
        self.stackedWidget.addWidget(self.parolasifirlamawidget)
        self.stackedWidget.addWidget(self.diyetisyenanasayfawidget)
        self.stackedWidget.addWidget(self.hastaanasayfawidget)
        self.stackedWidget.addWidget(self.hesaplamawidget)
        self.stackedWidget.addWidget(self.vucutkitlewidget)
        self.stackedWidget.addWidget(self.bazalmetwidget)
        self.stackedWidget.addWidget(self.idealkilowidget)
        self.stackedWidget.addWidget(self.gunlukkaloriwidget)
        self.stackedWidget.addWidget(self.diyetornegi1widget)
        self.stackedWidget.addWidget(self.randevuwidget)


        self.anasayfapage()#sayfalarınızı kendinize göre isimlendirin
        self.hastagirispage()
        self.diyetisyengirispage()
        self.hastakayitpage()
        self.parolasifirlamapage()
        self.diyetisyenanasayfapage()
        self.hastaanasayfapage()
        self.hesaplamapage()
        self.vucutkitlepage()
        self.bazalmetpage()
        self.idealkilopage()
        self.gunlukkaloripage()
        self.diyetornegi1page()
        self.randevupage()
        self.stackedWidget.setCurrentIndex(0)#hangi sayfadan başlayacağınızı buradan belirliyorsunuz

        #anasayfa
        self.anasayfa_button = None
        self.anasayfa_button2 = None

        self.main_lineedit = None

        # Aşağısı signup kısmı
        self.signup_button = None
        self.signup_lineedit = None

    def anasayfapage(self):#yukarıda oluşturduğumuz sayfaları bu şekilde tek tek ekliyoruz.
        self.anasayfa_form = anasayfa() #x yazan yere yukarıda importladığımız main sayfamızın Ui_formunu ekliyoruz
        self.anasayfa_form.setupUi(self.anasayfawidget) #yukarıda belirttiğimiz widget ismini buraya entegre ediyoruz.
        self.anasayfa_button = self.anasayfa_form.pushButton #qtdesigner ile oluşturduğumuz sayfamızın içindeki butonları yeni oluşturduklarımıza entegre ediyoruz.
        self.anasayfa_button2 = self.anasayfa_form.pushButton_2 #qtdesigner ile oluşturduğumuz sayfamızın içindeki butonları yeni oluşturduklarımıza entegre ediyoruz.
        self.anasayfa_button2.clicked.connect(self.hastagirisgoster)
        self.anasayfa_button.clicked.connect(self.diyetisyengirisgoster)
    def hastagirispage(self):#yukarıda oluşturduğumuz sayfaları bu şekilde tek tek ekliyoruz.
        self.hastagiris_form = hastagirissayfa() #x yazan yere yukarıda importladığımız main sayfamızın Ui_formunu ekliyoruz
        self.hastagiris_form.setupUi(self.hastagiriswidget) #yukarıda belirttiğimiz widget ismini buraya entegre ediyoruz.
        self.hastagiris_form.pushButton_2.clicked.connect(self.hastakayitgoster)
        self.hastagiris_form.pushButton_4.clicked.connect(self.parolasifirlamagoster)
        self.hastagiris_form.pushButton_3.clicked.connect(self.hastagiris)
        self.hastagiris_form.pushButton.clicked.connect(self.sifregoster)

    def sifregoster(self):
        if self.hastagiris_form.lineEdit_7.echoMode() == QLineEdit.EchoMode.Password:
            self.hastagiris_form.lineEdit_7.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.hastagiris_form.lineEdit_7.setEchoMode(QLineEdit.EchoMode.Password)


    def hastagiris(self):
        self.hastakullanici = self.hastagiris_form.lineEdit.text().strip()
        self.hastasifre = self.hastagiris_form.lineEdit_7.text().strip()
        user_data = self.hasta_collection.find_one({"kullanici Adi": self.hastakullanici, "sifre": self.hastasifre})
        if user_data:
            self.stackedWidget.setCurrentIndex(6)
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifrenizi yanlış girdiniz.")

    def hastaanasayfapage(self):
        self.hastaanasayfa_form = hastaanasayfa()
        self.hastaanasayfa_form.setupUi(self.hastaanasayfawidget)
        self.hastaanasayfa_form.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.hastaanasayfa_form.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.diyetornegi1widget))
        self.hastaanasayfa_form.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.randevuwidget))


    def hesaplamapage(self):
        self.hesaplama_form = hesaplama()
        self.hesaplama_form.setupUi(self.hesaplamawidget)
        self.hesaplama_form.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))
        self.hesaplama_form.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.hesaplama_form.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(10))
        self.hesaplama_form.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(11))
        self.hesaplama_form.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))

    def diyetornegi1page(self):
        self.diyetornegi1_form = diyetornegi1()
        self.diyetornegi1_form.setupUi(self.diyetornegi1widget)
        self.diyetornegi1_form.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))

    def randevupage(self):
        self.randevu_form = randevu()
        self.randevu_form.setupUi(self.randevuwidget)
        self.randevu_form.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))


    def vucutkitlepage(self):
        self.vucutkitle_form = vucutkitle()
        self.vucutkitle_form.setupUi((self.vucutkitlewidget))
        self.vucutkitle_form.pushButton_3.clicked.connect(self.vucutkitlehesapla)
        self.vucutkitle_form.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex((7)))

    def vucutkitlehesapla(self):
        kilo = float(self.vucutkitle_form.lineEdit_7.text().strip())
        boy = float(self.vucutkitle_form.lineEdit.text().strip())
        QMessageBox.information(self, "Hesaplama Sonucunuz", f"{kilo/boy*100*2 }")
    def bazalmetpage(self):
        self.bazalmet_form = bazalmet()
        self.bazalmet_form.setupUi(self.bazalmetwidget)
        self.bazalmet_form.pushButton_2.clicked.connect(self.bazalmethesapla)
        self.bazalmet_form.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex((7)))

    def bazalmethesapla(self):
        kilo = float(self.bazalmet_form.lineEdit_3.text().strip())
        boy = float(self.bazalmet_form.lineEdit_4.text().strip())
        cinsiyet = self.bazalmet_form.comboBox.currentText().strip()
        yas = int(self.bazalmet_form.lineEdit_6.text().strip())


        if cinsiyet == "Kadın":
            QMessageBox.information(self, "Hesaplama Sonucunuz", f"{655.10 + (9.56* kilo) + (1.85*boy)-(4.68*yas)}")
        elif cinsiyet == "Erkek":
            QMessageBox.information(self, "Hesaplama Sonucunuz", f"{66.47 + (13.75* kilo) + (5*boy)-(6.76*yas)}")

    def idealkilopage(self):
        self.idealkilo_form = idealkilo()
        self.idealkilo_form.setupUi(self.idealkilowidget)
        self.idealkilo_form.pushButton_2.clicked.connect(self.idealkilohesapla)
        self.idealkilo_form.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex((7)))

    def idealkilohesapla(self):
        boy = float(self.idealkilo_form.lineEdit_4.text().strip())
        cinsiyet = self.idealkilo_form.comboBox.currentText().strip()

        if cinsiyet == "Kadın":
            QMessageBox.information(self,"Hesaplama Sonucunuz", f"{45.5+2.3*((boy/2.54) -60)}")
        elif cinsiyet == "Erkek":
            QMessageBox.information(self, "Hesaplama Sonucunuz", f"{50 + 2.3*((boy/ 2.54) - 60)}")
    def gunlukkaloripage(self):
        self.gunlukkalori_form = gunlukkalori()
        self.gunlukkalori_form.setupUi(self.gunlukkaloriwidget)
        self.gunlukkalori_form.pushButton_2.clicked.connect(self.gunlukkalorihesapla)
        self.gunlukkalori_form.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex((7)))

    def gunlukkalorihesapla(self):
        kilo = float(self.gunlukkalori_form.lineEdit_3.text().strip())
        boy = float(self.gunlukkalori_form.lineEdit_4.text().strip())
        cinsiyet = self.gunlukkalori_form.comboBox.currentText().strip()
        yas = int(self.gunlukkalori_form.lineEdit_6.text().strip())

        if cinsiyet == "Kadın":
            QMessageBox.information(self, "Hesaplama Sonucunuz", f"{10*kilo+6.25*boy-5*yas-161}")
        elif cinsiyet == "Erkek":
            QMessageBox.information(self, "Hesaplama Sonucunuz",f"{10*kilo+6.25*boy-5*yas+5}")

    def diyetisyengirispage(self):
        self.diyetisyengiris_form = diyetisyengiris()
        self.diyetisyengiris_form.setupUi(self.diyetisyengiriswidget)
        self.diyetisyengiris_form.sifremiUnuttumBT.clicked.connect(self.parolasifirlamagoster)
        self.diyetisyengiris_form.girisButonu.clicked.connect(self.diyetisyengiris)
        self.diyetisyengiris_form.sifreGoster.clicked.connect(self.sifregoster)

    def sifregoster(self):
        if self.diyetisyengiris_form.sifreLE.echoMode() == QLineEdit.EchoMode.Password:
            self.diyetisyengiris_form.sifreLE.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.diyetisyengiris_form.sifreLE.setEchoMode(QLineEdit.EchoMode.Password)

    def diyetisyenanasayfapage(self):
        self.diyetisyenanasayfa_form = diyetisyenanasayfa()
        self.diyetisyenanasayfa_form.setupUi(self.diyetisyenanasayfawidget)


    def diyetisyengiris(self):
        kullaniciAdi = self.diyetisyengiris_form.kullaciAdiLE.text().strip()
        sifre= self.diyetisyengiris_form.sifreLE.text().strip()
        user_data = self.diyetisyen_collection.find_one({"kullanici Adi": kullaniciAdi, "sifre": sifre})
        if user_data:
            self.stackedWidget.setCurrentIndex(5)
        else:
            QMessageBox.warning(self, "Yanlış Şifre", "Kullanıcı adı veya şifrenizi yanlış girdiniz.")

    def hastakayitpage(self):#yukarıda oluşturduğumuz sayfaları bu şekilde tek tek ekliyoruz.
        self.hastakayit_form = hastakayit() #x yazan yere yukarıda importladığımız main sayfamızın Ui_formunu ekliyoruz
        self.hastakayit_form.setupUi(self.hastakayitwidget)
        self.kayitButonu = self.hastakayit_form.kaydolBT
        self.kayitButonu.clicked.connect(self.kaydol)

    def kaydol(self):
        self.tc = self.hastakayit_form.tcLE.text().strip()
        self.ad = self.hastakayit_form.adLE.text().strip()
        self.soyad = self.hastakayit_form.soyadLE.text().strip()
        self.email = self.hastakayit_form.emailLE.text().strip()
        self.dogumtarihi = self.hastakayit_form.dogumTarihiLE.text().strip()
        self.cinsiyet = self.hastakayit_form.cinsiyetCB.currentText().strip()
        self.parola = self.hastakayit_form.parolaLE.text().strip()
        user_data = self.hasta_collection.find_one({"$or":[{"kullanici Adi": self.tc}, {"email": self.email}]})
        #if not self.tc or not self.ad or not self.soyad or not self.email or not self.dogumtarihi or not self.parola:
         #   QMessageBox.warning(self, "Hata", "Bütün bilgilerinizi girdiğinize emin olun.")
        if self.tc == "":
            QMessageBox.warning(self, "Hata", "TC bilgisi eksik.")
        elif self.ad == "":
            QMessageBox.warning(self, "Hata", "Ad bilgisi eksik.")
        elif self.soyad == "":
            QMessageBox.warning(self, "Hata", "Soyad bilgisi eksik.")
        elif self.email == "":
            QMessageBox.warning(self, "Hata", "E-mail bilgisi eksik.")
        elif self.dogumtarihi == "":
            QMessageBox.warning(self, "Hata", "Doğum tarihi bilgisi eksik.")
        elif self.parola == "":
            QMessageBox.warning(self, "Hata", "Parola bilgisi eksik.")
        elif user_data:
            QMessageBox.warning(self, "Hata", "Aynı email adresine veya T.C. kimlik numarasıyla kayıtlı bir hasta var.")
        else:
            self.hasta_collection.insert_one({"kullanici Adi": self.tc, "ad": self.ad, "soyad": self.soyad, "email": self.email, "dogumtarihi": self.dogumtarihi, "cinsiyet": self.cinsiyet, "sifre": self.parola})
            self.stackedWidget.setCurrentIndex(6)
    def parolasifirlamapage(self):  # yukarıda oluşturduğumuz sayfaları bu şekilde tek tek ekliyoruz.
        self.parolasifirlama_form = parolasifirlama()  # x yazan yere yukarıda importladığımız main sayfamızın Ui_formunu ekliyoruz
        self.parolasifirlama_form.setupUi(self.parolasifirlamawidget)
    def hastagirisgoster(self):
        self.stackedWidget.setCurrentIndex(1)
    def diyetisyengirisgoster(self):
        self.stackedWidget.setCurrentIndex(2)

    def hastakayitgoster(self):
        self.stackedWidget.setCurrentIndex(3)

    def parolasifirlamagoster(self):
        self.stackedWidget.setCurrentIndex(4)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
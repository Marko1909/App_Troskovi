from PyQt5 import QtWidgets, QtGui, QtCore, QtChart
import sys
import sqlite3

from utilities import login_provjera, signup_provjera, provjera_unosa_troskova
from enumeratori import Kategorije

con = sqlite3.connect("troskoviDB.db")
cur = con.cursor()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('App_troškovi')
        self.setGeometry(600, 100, 540, 600)
        self.initUI()

    def initUI(self):
        self.fontSmall = QtGui.QFont('Arial', 8)
        self.fontButton = QtGui.QFont('Times New Roman', 14)
        self.font = QtGui.QFont('Times New Roman', 12)

# Login Screen
        # Frame login screen
        self.frame_login = QtWidgets.QFrame(self)
        self.frame_login.setGeometry(QtCore.QRect(145, 80, 250, 350))
        self.frame_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_login.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Raised)

        self.g_layout_login = QtWidgets.QGridLayout(self.frame_login)
        self.g_layout_login.setContentsMargins(10, 0, 10, 10)

        # label login
        self.label_login = QtWidgets.QLabel(self)
        self.label_login.setFont(self.fontButton)
        self.label_login.setText(' Login')
        self.label_login.setMinimumSize(200, 40)
        self.g_layout_login.addWidget(self.label_login, 0, 0, 1, 1)

        # label email
        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setFont(self.fontSmall)
        self.label_email.setText(' Email')
        self.label_email.setMaximumSize(100, 10)
        self.g_layout_login.addWidget(self.label_email, 2, 0, 1, 1)
        # Text unos email-a
        self.text_email = QtWidgets.QLineEdit(self)
        self.text_email.setMinimumSize(200, 30)
        self.g_layout_login.addWidget(self.text_email, 3, 0, 1, 1)

        # Label password
        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setFont(self.fontSmall)
        self.label_password.setText(' Password')
        self.label_password.setMaximumSize(100, 10)
        self.g_layout_login.addWidget(self.label_password, 4, 0, 1, 1)
        # Text unos password-a
        self.text_password = QtWidgets.QLineEdit(self)
        self.text_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_password.setMinimumSize(200, 30)
        self.g_layout_login.addWidget(self.text_password, 5, 0, 1, 1)

        # Label neispravan email ili password
        self.label_error_login = QtWidgets.QLabel(self)
        self.label_error_login.setFont(self.fontSmall)
        self.label_error_login.setStyleSheet('color: red;')
        self.label_error_login.setContentsMargins(30, 0, 0, 0)
        self.label_error_login.setMaximumSize(200, 15)
        self.g_layout_login.addWidget(self.label_error_login, 6, 0, 1, 1)

        # Button log-in
        self.button_login = QtWidgets.QPushButton(self)
        self.button_login.setMinimumSize(180, 40)
        self.button_login.setFont(self.fontButton)
        self.button_login.setText('Ulogiraj me')
        self.button_login.setStyleSheet("*{background-color: rgb(80,170,255)}")
        self.button_login.clicked.connect(self.login)
        self.g_layout_login.addWidget(self.button_login, 7, 0, 1, 1)

        self.g_layout_login.setRowMinimumHeight(8, 50)

        # Label sing-in opis
        self.label_signup_opis = QtWidgets.QLabel(self)
        self.label_signup_opis.setFont(self.fontSmall)
        self.label_signup_opis.setText(' Nemate korisnički račun, izradite novi!')
        self.label_signup_opis.setMaximumSize(230, 10)
        self.g_layout_login.addWidget(self.label_signup_opis, 9, 0, 1, 1)

        # Button sing-in
        self.button_signup = QtWidgets.QPushButton(self)
        self.button_signup.setMinimumSize(180, 40)
        self.button_signup.setFont(self.font)
        self.button_signup.setText('Kreiraj račun')
        self.button_signup.setStyleSheet("*{background-color: rgb(200,200,200)}")
        self.button_signup.clicked.connect(self.signup)
        self.g_layout_login.addWidget(self.button_signup, 10, 0, 1, 1)


# Frame za prikaz prozora izrade korisničkog računa
        self.frame_signup = QtWidgets.QFrame(self)
        self.frame_signup.setGeometry(QtCore.QRect(145, 60, 250, 440))
        self.frame_signup.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_signup.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_signup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup.hide()

        # Grid layout za prozor izrade korisničkog računa
        self.g_layout_signup = QtWidgets.QGridLayout(self.frame_signup)
        self.g_layout_signup.setContentsMargins(10, 10, 10, 25)

        # Label naslov signup
        self.label_signup = QtWidgets.QLabel(self)
        self.label_signup.setFont(self.fontButton)
        self.label_signup.setText(' Signup')
        self.label_signup.setMinimumSize(200, 30)
        self.g_layout_signup.addWidget(self.label_signup, 0, 0, 1, 1)

        # Button povratak u login prikaz
        self.button_back = QtWidgets.QToolButton(self)
        self.button_back.setMaximumSize(30, 30)
        self.button_back.setArrowType(3)
        self.button_back.setStyleSheet("*{background-color: rgb(200,200,200)}")
        self.button_back.clicked.connect(self.close_signup)
        self.g_layout_signup.addWidget(self.button_back, 0, 0, QtCore.Qt.AlignRight)

        self.g_layout_signup.setRowMinimumHeight(1, 20)

        # Label Ime
        self.label_ime_signup = QtWidgets.QLabel(self)
        self.label_ime_signup.setFont(self.fontSmall)
        self.label_ime_signup.setText(' Ime')
        self.label_ime_signup.setMaximumSize(100, 10)
        self.g_layout_signup.addWidget(self.label_ime_signup, 2, 0, 1, 1)
        # Text unos imena
        self.text_ime_signup = QtWidgets.QLineEdit(self)
        self.text_ime_signup.setMinimumSize(200, 30)
        self.g_layout_signup.addWidget(self.text_ime_signup, 3, 0, 1, 1)

        # Label prezime
        self.label_prezime_signup = QtWidgets.QLabel(self)
        self.label_prezime_signup.setFont(self.fontSmall)
        self.label_prezime_signup.setText(' Prezime')
        self.label_prezime_signup.setMaximumSize(100, 10)
        self.g_layout_signup.addWidget(self.label_prezime_signup, 4, 0, 1, 1)
        # Text unos prezimena
        self.text_prezime_signup = QtWidgets.QLineEdit(self)
        self.text_prezime_signup.setMinimumSize(200, 30)
        self.g_layout_signup.addWidget(self.text_prezime_signup, 5, 0, 1, 1)

        # Label email
        self.label_email_signup = QtWidgets.QLabel(self)
        self.label_email_signup.setFont(self.fontSmall)
        self.label_email_signup.setText(' Email')
        self.label_email_signup.setMaximumSize(100, 10)
        self.g_layout_signup.addWidget(self.label_email_signup, 6, 0, 1, 1)
        # Text unos email-a
        self.text_email_signup = QtWidgets.QLineEdit(self)
        self.text_email_signup.setMinimumSize(200, 30)
        self.g_layout_signup.addWidget(self.text_email_signup, 7, 0, 1, 1)

        # Label password
        self.label_password_signup = QtWidgets.QLabel(self)
        self.label_password_signup.setFont(self.fontSmall)
        self.label_password_signup.setText(' Password')
        self.label_password_signup.setMaximumSize(100, 10)
        self.g_layout_signup.addWidget(self.label_password_signup, 8, 0, 1, 1)
        # Text unos password-a
        self.text_password_signup = QtWidgets.QLineEdit(self)
        self.text_password_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_password_signup.setMinimumSize(200, 30)
        self.g_layout_signup.addWidget(self.text_password_signup, 9, 0, 1, 1)

        # Label potvrdi password
        self.label_potvrda_password_signup = QtWidgets.QLabel(self)
        self.label_potvrda_password_signup.setFont(self.fontSmall)
        self.label_potvrda_password_signup.setText(' Potvrdi password')
        self.label_potvrda_password_signup.setMaximumSize(120, 10)
        self.g_layout_signup.addWidget(self.label_potvrda_password_signup, 10, 0, 1, 1)
        # Text unos potvrde password-a
        self.text_potvrda_password_signup = QtWidgets.QLineEdit(self)
        self.text_potvrda_password_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_potvrda_password_signup.setMinimumSize(200, 30)
        self.g_layout_signup.addWidget(self.text_potvrda_password_signup, 11, 0, 1, 1)

        # Label error pri izradi korisnika
        self.label_error_signup = QtWidgets.QLabel(self)
        self.label_error_signup.setFont(self.fontSmall)
        self.label_error_signup.setStyleSheet('color: red;')
        self.label_error_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_signup.setContentsMargins(30, 0, 0, 0)
        self.label_error_signup.setMaximumSize(200, 30)
        self.g_layout_signup.addWidget(self.label_error_signup, 12, 0, 1, 1)

        # Button kreiraj korisnički račun
        self.button_prijava = QtWidgets.QPushButton(self)
        self.button_prijava.setMinimumSize(180, 40)
        self.button_prijava.setFont(self.fontButton)
        self.button_prijava.setText('Kreiraj račun')
        self.button_prijava.setStyleSheet("*{background-color: rgb(80,170,255)}")
        self.button_prijava.clicked.connect(self.prijava)
        self.g_layout_signup.addWidget(self.button_prijava, 13, 0, 1, 1)


# Glavni layout za display
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 540, 80))
        self.horizontalLayoutWidget.hide()

        # Label korisnik
        self.label_korisnik = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_korisnik.setFont(self.font)
        self.label_korisnik.setGeometry(5, 0, 200, 30)
        self.label_korisnik.setMaximumSize(200, 30)

        # Button logout, odjavi korisnika
        self.button_logout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_logout.setGeometry(470, 0, 70, 30)
        self.button_logout.setFont(self.font)
        self.button_logout.setText('Odjava')
        self.button_logout.setStyleSheet("*{background-color: rgb(200,200,200)}")
        self.button_logout.clicked.connect(self.logout)

        # Layout za glavne buttone
        self.h_layout_main_button = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.h_layout_main_button.setContentsMargins(0, 31, 0, 0)

        # Button prikaz displaya s unosom potrosnja
        self.button_display_unosa = QtWidgets.QPushButton(self)
        self.button_display_unosa.setMinimumSize(180, 50)
        self.button_display_unosa.setFont(self.fontButton)
        self.button_display_unosa.setText('Unos')
        self.button_display_unosa.setStyleSheet("*{background-color: rgb(0,255,100)}")
        self.button_display_unosa.clicked.connect(self.display_unos)
        self.h_layout_main_button.addWidget(self.button_display_unosa)

        # Button prikaz displaya s unesenim potrosnjama
        self.button_display_unesenih = QtWidgets.QPushButton(self)
        self.button_display_unesenih.setMinimumSize(180, 50)
        self.button_display_unesenih.setFont(self.fontButton)
        self.button_display_unesenih.setText('Pregled')
        self.button_display_unesenih.setStyleSheet("*{background-color: rgb(0,255,100)}")
        self.button_display_unesenih.clicked.connect(self.display_uneseni)
        self.h_layout_main_button.addWidget(self.button_display_unesenih)

        # Button prikaz displaya s grafickim prikazom
        self.button_display_grafikon = QtWidgets.QPushButton(self)
        self.button_display_grafikon.setMinimumSize(180, 50)
        self.button_display_grafikon.setFont(self.fontButton)
        self.button_display_grafikon.setText('Usporedba')
        self.button_display_grafikon.setStyleSheet("*{background-color: rgb(0,255,100)}")
        self.button_display_grafikon.clicked.connect(self.display_grafikon)
        self.h_layout_main_button.addWidget(self.button_display_grafikon)


# 1. Display
        # Frame unosa troskova
        self.frame_unos = QtWidgets.QFrame(self)
        self.frame_unos.setGeometry((QtCore.QRect(0, 100, 540, 500)))
        self.frame_unos.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_unos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_unos.hide()

        # Grid Layout za unosu troskova
        self.g_layout_unosi = QtWidgets.QGridLayout(self.frame_unos)
        self.g_layout_unosi.setContentsMargins(50, 20, 50, 5)

        # label dnevna potrosnja
        self.label_dnevna_potrosnja = QtWidgets.QLabel(self)
        self.label_dnevna_potrosnja.setFont(self.font)
        self.label_dnevna_potrosnja.setText(' Dnevni troskovi')
        self.label_dnevna_potrosnja.setMinimumSize(200, 40)
        self.label_dnevna_potrosnja.setStyleSheet(
            "*{background: rgb(200,120,200); border: 1px solid black; border-radius: 15px;}")
        self.g_layout_unosi.addWidget(self.label_dnevna_potrosnja, 0, 0, 1, 1)
        # Text unos dnevne potrosnje
        self.text_dnevna_potrosnja = QtWidgets.QLineEdit(self)
        self.text_dnevna_potrosnja.setFont(self.font)
        self.text_dnevna_potrosnja.setMinimumSize(200,30)
        self.text_dnevna_potrosnja.setStyleSheet("*{background: white; border: 1px solid black;}")
        self.g_layout_unosi.addWidget(self.text_dnevna_potrosnja, 0, 1, 1, 1)

        # Label namirnice
        self.label_namirnice = QtWidgets.QLabel(self)
        self.label_namirnice.setFont(self.font)
        self.label_namirnice.setText(' Namirnice')
        self.label_namirnice.setMinimumSize(200, 40)
        self.label_namirnice.setStyleSheet(
            "*{background: rgb(45,135,215); border: 1px solid black; border-radius: 15px;}")
        self.g_layout_unosi.addWidget(self.label_namirnice, 1, 0, 1, 1)
        # Text unos placenog racuna za namirnice
        self.text_namirnice = QtWidgets.QLineEdit(self)
        self.text_namirnice.setFont(self.font)
        self.text_namirnice.setMinimumSize(200, 30)
        self.text_namirnice.setStyleSheet("*{background: white; border: 1px solid black;}")
        self.g_layout_unosi.addWidget(self.text_namirnice, 1, 1, 1, 1)

        # Label struja
        self.label_struja = QtWidgets.QLabel(self)
        self.label_struja.setFont(self.font)
        self.label_struja.setText(' Struja')
        self.label_struja.setMinimumSize(200, 40)
        self.label_struja.setStyleSheet(
            "*{background: rgb(220,225,100); border: 1px solid black; border-radius: 15px;}")
        self.g_layout_unosi.addWidget(self.label_struja, 2, 0, 1, 1)
        # Text unos placenog racuna za struje
        self.text_struja = QtWidgets.QLineEdit(self)
        self.text_struja.setFont(self.font)
        self.text_struja.setMinimumSize(200, 30)
        self.text_struja.setStyleSheet("*{background: white; border: 1px solid black;}")
        self.g_layout_unosi.addWidget(self.text_struja, 2, 1, 1, 1)

        # Label plin
        self.label_plin = QtWidgets.QLabel(self)
        self.label_plin.setFont(self.font)
        self.label_plin.setText(' Plin')
        self.label_plin.setMinimumSize(200, 40)
        self.label_plin.setStyleSheet(
            "*{background: rgb(85,230,230); border: 1px solid black; border-radius: 15px;}")
        self.g_layout_unosi.addWidget(self.label_plin, 3, 0, 1, 1)
        # Text unos placenog racuna za plina
        self.text_plin = QtWidgets.QLineEdit(self)
        self.text_plin.setFont(self.font)
        self.text_plin.setMinimumSize(200, 30)
        self.text_plin.setStyleSheet("*{background: white; border: 1px solid black;}")
        self.g_layout_unosi.addWidget(self.text_plin, 3, 1, 1, 1)

        # Label telefon/internet
        self.label_telefon_internet = QtWidgets.QLabel(self)
        self.label_telefon_internet.setFont(self.font)
        self.label_telefon_internet.setText(' Tel/Internet')
        self.label_telefon_internet.setMinimumSize(200, 40)
        self.label_telefon_internet.setStyleSheet(
            "*{background: rgb(225,180,95); border: 1px solid black; border-radius: 15px;}")
        self.g_layout_unosi.addWidget(self.label_telefon_internet, 4, 0, 1, 1)
        # Text unos placenog racuna za telefon/internet
        self.text_telefon_internet = QtWidgets.QLineEdit(self)
        self.text_telefon_internet.setFont(self.font)
        self.text_telefon_internet.setMinimumSize(200, 30)
        self.text_telefon_internet.setStyleSheet("*{background: white; border: 1px solid black;}")
        self.g_layout_unosi.addWidget(self.text_telefon_internet, 4, 1, 1, 1)

        # label tv
        self.label_tv = QtWidgets.QLabel(self)
        self.label_tv.setFont(self.font)
        self.label_tv.setText(' Tv')
        self.label_tv.setMinimumSize(200, 40)
        self.label_tv.setStyleSheet(
            "*{background: rgb(235,85,90); border: 1px solid black; border-radius: 15px;}")
        self.g_layout_unosi.addWidget(self.label_tv, 5, 0, 1, 1)
        # Text unos placenog racuna za tv-a
        self.text_tv = QtWidgets.QLineEdit(self)
        self.text_tv.setFont(self.font)
        self.text_tv.setMinimumSize(200, 30)
        self.text_tv.setStyleSheet("*{background: white; border: 1px solid black;}")
        self.g_layout_unosi.addWidget(self.text_tv, 5, 1, 1, 1)

        # Label komunalno
        self.label_komunalno = QtWidgets.QLabel(self)
        self.label_komunalno.setFont(self.font)
        self.label_komunalno.setText(' Komunalno')
        self.label_komunalno.setMinimumSize(200, 40)
        self.label_komunalno.setStyleSheet(
            "*{background: rgb(120,200,125); border: 1px solid black; border-radius: 15px;}")
        self.g_layout_unosi.addWidget(self.label_komunalno, 6, 0, 1, 1)
        # Text unos placenog racuna za komunalno
        self.text_komunalno = QtWidgets.QLineEdit(self)
        self.text_komunalno.setFont(self.font)
        self.text_komunalno.setMinimumSize(200, 30)
        self.text_komunalno.setStyleSheet("*{background: white; border: 1px solid black;}")
        self.g_layout_unosi.addWidget(self.text_komunalno, 6, 1, 1, 1)

        # Label kredit
        self.label_kredit = QtWidgets.QLabel(self)
        self.label_kredit.setFont(self.font)
        self.label_kredit.setText(' Kredit')
        self.label_kredit.setMinimumSize(200, 40)
        self.label_kredit.setStyleSheet(
            "*{background: rgb(240,110,215); border: 1px solid black; border-radius: 15px;}")
        self.g_layout_unosi.addWidget(self.label_kredit, 7, 0, 1, 1)
        # Text unos placenog racuna za kredit
        self.text_kredit = QtWidgets.QLineEdit(self)
        self.text_kredit.setFont(self.font)
        self.text_kredit.setMinimumSize(200, 30)
        self.text_kredit.setStyleSheet("*{background: white; border: 1px solid black;}")
        self.g_layout_unosi.addWidget(self.text_kredit, 7, 1, 1, 1)

        self.g_layout_unosi.setRowMinimumHeight(8, 10)

        # label error pri potvrdi unesenih troskova
        self.label_error_unosa = QtWidgets.QLabel(self)
        self.label_error_unosa.setFont(self.fontSmall)
        self.label_error_unosa.setStyleSheet('color: red;')
        self.label_error_unosa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_unosa.setContentsMargins(30, 0, 0, 0)
        self.label_error_unosa.setMaximumSize(400, 20)
        self.g_layout_unosi.addWidget(self.label_error_unosa, 9, 0, 1, 2)

        # Button za potvrdu unesenih troškova
        self.button_potvrda_unosa = QtWidgets.QPushButton(self)
        self.button_potvrda_unosa.setMinimumSize(190, 40)
        self.button_potvrda_unosa.setFont(self.fontButton)
        self.button_potvrda_unosa.setText('Potvrda unosa')
        self.button_potvrda_unosa.setStyleSheet("*{background-color: rgb(80,170,255)}")
        self.button_potvrda_unosa.clicked.connect(self.potvrdi_unos)
        self.g_layout_unosi.addWidget(self.button_potvrda_unosa, 10, 0, 0, 2, QtCore.Qt.AlignCenter)

        # Label datum
        self.label_date = QtWidgets.QLabel(self)
        self.label_date.setFont(self.font)
        self.label_date.setText('Datum')
        self.label_date.setContentsMargins(0, 0, 0, 0)
        self.g_layout_unosi.addWidget(self.label_date, 10, 0, 1, 1)

        # Date ispis danasnjeg datuma
        date = QtCore.QDate.currentDate()
        self.datum = QtWidgets.QLabel(self)
        self.datum.setContentsMargins(0, 29, 0, 0)
        self.datum.setText(f'{date.toString("dd.MM.yyyy.")}')
        self.g_layout_unosi.addWidget(self.datum, 10, 0, 1, 1)


# 2. Display
        # Frame za prikaz unesenih troskova
        self.frame_ispis = QtWidgets.QFrame(self)
        self.frame_ispis.setGeometry(QtCore.QRect(0, 90, 540, 520))
        self.frame_ispis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ispis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ispis.hide()

        # List ispis unesenih troskova za ScrollArea
        self.list_ispis = QtWidgets.QListWidget(self)
        self.list_ispis.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Scroolarea za prikaz unesenih troskova
        self.scrollarea_ispis = QtWidgets.QScrollArea(self.frame_ispis)
        self.scrollarea_ispis.setGeometry(QtCore.QRect(10, 70, 520, 400))
        self.scrollarea_ispis.setWidgetResizable(True)
        self.scrollarea_ispis.setWidget(self.list_ispis)

        # Combobox za izbor kategorije unesenih troskova
        self.kategorije_ispisa = QtWidgets.QComboBox(self.frame_ispis)
        self.kategorije_ispisa.setFont(self.font)

        for kategorija in Kategorije:
            self.kategorije_ispisa.addItem(str(kategorija.value))

        #self.kategorije_ispisa.currentTextChanged.connect(self.combobox_uneseni_troskovi)
        self.kategorije_ispisa.setGeometry(QtCore.QRect(10, 20, 180, 30))

        # Text pretraga specificnog troska
        self.text_pretraga = QtWidgets.QLineEdit(self.frame_ispis)
        self.text_pretraga.setGeometry(QtCore.QRect(250, 20, 180, 30))

        # Button potvrda pretrage iz text_pretraga
        self.button_potvrda_pretrage = QtWidgets.QPushButton(self.frame_ispis)
        self.button_potvrda_pretrage.setGeometry(QtCore.QRect(440, 20, 90, 30))
        self.button_potvrda_pretrage.setText('Pretraži')
        self.button_potvrda_pretrage.clicked.connect(self.pretrazi_listu)

# 3. Display
        # Frame za prikaz grafa
        self.frame_grafikon = QtWidgets.QFrame(self)
        self.frame_grafikon.setGeometry(QtCore.QRect(0, 90, 540, 520))
        self.frame_grafikon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grafikon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grafikon.hide()

        # Gridlayput za graficki prikaz
        self.g_layout_graf = QtWidgets.QGridLayout(self.frame_grafikon)
        self.g_layout_graf.setContentsMargins(9, 9, 9, 0)

        # Combobox izbor kategorije za prikaz na grafu
        self.kategorije_grafa = QtWidgets.QComboBox(self)
        self.kategorije_grafa.setFont(self.font)

        for kategorija in Kategorije:
            self.kategorije_grafa.addItem(str(kategorija.value))

        self.kategorije_grafa.setMaximumSize(180, 30)
        self.g_layout_graf.addWidget(self.kategorije_grafa, 0, 0, 1, 1)

        # Button za potvrdu izbora kategorije i prikaz
        self.button_potvrda_grafikona = QtWidgets.QPushButton(self)
        self.button_potvrda_grafikona.setMinimumSize(90, 30)
        self.button_potvrda_grafikona.setText('Prikaži')
        self.button_potvrda_grafikona.clicked.connect(self.prikazi_graf)
        self.g_layout_graf.addWidget(self.button_potvrda_grafikona, 0, 1, 1, 1, QtCore.Qt.AlignRight)

        #  X os grafa
        self.os_x = QtChart.QValueAxis(self)
        self.os_x.setRange(0, 12)
        self.os_x.setLabelFormat("%d")
        self.os_x.TickType.TicksFixed

        # Y os grafa
        self.os_y = QtChart.QValueAxis(self)
        self.os_y.setRange(0, 1)
        self.os_y.setTickCount(10)
        self.os_y.applyNiceNumbers()
        self.os_y.setLabelFormat("%.2f")
        self.os_y.TickType.TicksFixed

        # Izrada grafa
        self.graf = QtChart.QChart()
        self.graf.setAxisX(self.os_x)
        self.graf.setAxisY(self.os_y)
        self.graf.legend().hide()
        self.graf.setTitle('Grafički prikaz troškova')
        self.graf.setTitleFont(self.fontButton)

        # Grafički prikaz
        self.graficki_prikaz = QtChart.QChartView(self.graf)
        self.graficki_prikaz.setContentsMargins(0, 0, 0, 0)
        self.graficki_prikaz.setMinimumSize(520, 440)
        self.graficki_prikaz.setMaximumSize(520, 440)
        self.graficki_prikaz.setRenderHint(QtGui.QPainter.Antialiasing)
        self.g_layout_graf.addWidget(self.graficki_prikaz, 1, 0, 1, 2)

    # Funkcija za prijavu korisnika
    def login(self):
        # Provjera ispravnosti emaila i passworda
        error_login = login_provjera(self.text_email.text(), self.text_password.text())

        if error_login is None:
            self.label_error_login.setText('Neispravan email ili lozinka!')

        # Uspješno ulogiran, prikaz displaya i ispis prijašnjih troškova
        elif error_login != None:
            self.frame_login.hide()
            self.horizontalLayoutWidget.show()
            self.frame_unos.show()
            self.label_error_login.setText('')
            self.label_korisnik.setText(f'{error_login[1]} {error_login[2]}')

            # Ispis spremljenih troskova u listu
            query = f""" 
                        SELECT datum, ime, prezime, naziv, cijena FROM trosak
                        LEFT JOIN korisnik ON korisnik.id = trosak.id_korisnika
                        LEFT JOIN kategorija ON kategorija.id = trosak.id_kategorije
                        WHERE korisnik.id = {error_login[0]}
                    """

            spremljeni_troskovi = cur.execute(query).fetchall()

            for ispis_troska in spremljeni_troskovi:
                self.list_ispis.insertItem(0, f'{ispis_troska[0]}       {ispis_troska[1]} {ispis_troska[2]}       '
                                                f'{ispis_troska[4]}       {ispis_troska[3]}')

    # Funkcija za odjavu korisnika
    def logout(self):
        if self.frame_unos.isVisible():
            self.frame_unos.hide()

        elif self.frame_ispis.isVisible():
            self.frame_ispis.hide()

        elif self.frame_grafikon.isVisible():
            self.frame_grafikon.hide()

        self.horizontalLayoutWidget.hide()
        self.frame_login.show()
        self.text_password.setText('')
        self.list_ispis.clear()
        self.graf.removeAllSeries()
        self.kategorije_ispisa.setCurrentIndex(0)
        self.kategorije_grafa.setCurrentIndex(0)
        self.text_pretraga.setText('')

    # Funkcija za prijelaz u signup screen
    def signup(self):
        self.frame_login.hide()
        self.frame_signup.show()

    # Funkcija za povratak iz signup-a u login screen
    def close_signup(self):
        self.frame_signup.hide()
        self.frame_login.show()
        self.text_ime_signup.setText('')
        self.text_prezime_signup.setText('')
        self.text_email_signup.setText('')
        self.text_password_signup.setText('')
        self.text_potvrda_password_signup.setText('')

    # Funkcija za kreiranje i spremanje novog korisnika
    def prijava(self):
        # Provjera unesenih podataka
        error_signup = signup_provjera(self.text_ime_signup.text(), self.text_prezime_signup.text(),
                                       self.text_email_signup.text(), self.text_password_signup.text(),
                                       self.text_potvrda_password_signup.text())

        # Ako su podaci dobri, izradi račun i spremi podatke
        if error_signup is None:
            query = f"""
                        INSERT INTO korisnik (ime, prezime, email, password)
                        VALUES ('{self.text_ime_signup.text()}', '{self.text_prezime_signup.text()}', 
                                '{self.text_email_signup.text()}', '{self.text_password_signup.text()}')
                    """

            cur.execute(query)
            con.commit()

            self.text_ime_signup.setText('')
            self.text_prezime_signup.setText('')
            self.text_email_signup.setText('')
            self.text_password_signup.setText('')
            self.text_potvrda_password_signup.setText('')
            self.label_error_signup.setText('Uspješno kreiran račun!')

        else:
            self.label_error_signup.setText(error_signup)



    # Funkcija za prikaz displaya s unosom troskiva
    def display_unos(self):
        if self.frame_ispis.isVisible():
            self.frame_ispis.hide()
            self.frame_unos.show()

        elif self.frame_grafikon.isVisible():
            self.frame_grafikon.hide()
            self.frame_unos.show()

        else:
            return

    # Funkcija za prikaz displaya s unesenim troskovima
    def display_uneseni(self):
        if self.frame_unos.isVisible():
            self.frame_unos.hide()
            self.frame_ispis.show()

        elif self.frame_grafikon.isVisible():
            self.frame_grafikon.hide()
            self.frame_ispis.show()

        else:
            return

    # Funkcija za prikaz displaya s grafom
    def display_grafikon(self):
        if self.frame_unos.isVisible():
            self.frame_unos.hide()
            self.frame_grafikon.show()

        elif self.frame_ispis.isVisible():
            self.frame_ispis.hide()
            self.frame_grafikon.show()

        else:
            return

    # Provjera id-a korisnika i spremanje unesenih podataka
    def potvrdi_unos(self):
        # Uzimanje podataka korisnika i provjera trenutno ulogiranog korisnika
        query_id_korisnika = """
                           SELECT id, ime, prezime, email FROM korisnik
                       """

        data = cur.execute(query_id_korisnika).fetchall()

        for d in data:
            if d[3] == self.text_email.text():
                id_korisnik = d[0]
                ime_korisnik = d[1]
                prezime_korsinik = d[2]

        # Provjera unesenih vrijednosti troškova i spremanje
        lista_troskova = [self.text_dnevna_potrosnja.text(), self.text_namirnice.text(), self.text_struja.text(),
                          self.text_plin.text(), self.text_telefon_internet.text(), self.text_tv.text(),
                          self.text_komunalno.text(), self.text_kredit.text()]

        error_unosa = provjera_unosa_troskova(lista_troskova)

        if error_unosa is None:
            for i, trosak in enumerate(lista_troskova, start=1):
                if trosak != '':
                    query = f"""
                                INSERT INTO trosak (datum, id_korisnika, id_kategorije, cijena)
                                VALUES ('{self.datum.text()}', '{id_korisnik}', 
                                        '{i}', '{lista_troskova[i-1]}')
                            """

                    cur.execute(query)
                    con.commit()

                    # Ispis novo upisanih troškova u listu
                    for j, kategorija in enumerate(Kategorije):
                        if j == i:
                            potrebna_kategorija = kategorija.value

                    self.list_ispis.insertItem(0, f'{self.datum.text()}       {ime_korisnik} {prezime_korsinik}       '
                                                  f'{lista_troskova[i-1]}       {potrebna_kategorija}')

            self.text_dnevna_potrosnja.setText('')
            self.text_namirnice.setText('')
            self.text_struja.setText('')
            self.text_plin.setText('')
            self.text_telefon_internet.setText('')
            self.text_tv.setText('')
            self.text_komunalno.setText('')
            self.text_kredit.setText('')
            self.label_error_unosa.setText('')

        else:
            self.label_error_unosa.setText(error_unosa)

    # Funkcija za pretraživanje liste upisanih opodataka
    def pretrazi_listu(self):
        # Pronalazak id-a za trenutnog korisnika
        query_id = f"""
                    SELECT id, email FROM KORISNIK
                """

        id = cur.execute(query_id).fetchall()

        for i in id:
            if i[1] == self.text_email.text():
                id_korisnika = i[0]

        # Uzimanje podataka o troškovima za ulogiranog korisnika
        query = f"""
                    SELECT datum, ime, prezime, naziv, cijena FROM trosak
                    LEFT JOIN korisnik ON korisnik.id = trosak.id_korisnika
                    LEFT JOIN kategorija ON kategorija.id = trosak.id_kategorije
                    WHERE id_korisnika = {id_korisnika}
                """

        data = cur.execute(query).fetchall()

        # Pretraga liste preko dropboxa
        if self.kategorije_ispisa.currentText() != '...' and self.text_pretraga.text() == '':
            self.list_ispis.clear()
            for d in data:
                if d[3] == self.kategorije_ispisa.currentText():
                    self.list_ispis.insertItem(0, f'{d[0]}       {d[1]} {d[2]}       '
                                                  f'{d[4]}       {d[3]}')

        # Ispis svih podataka u listu
        elif self.kategorije_ispisa.currentText() == '...' and self.text_pretraga.text() == '':
            self.list_ispis.clear()
            for d in data:
                self.list_ispis.insertItem(0, f'{d[0]}       {d[1]} {d[2]}       '
                                              f'{d[4]}       {d[3]}')

        # Pretraga liste po unosu teksta
        elif self.kategorije_ispisa.currentText() == '...' and self.text_pretraga.text() != '':
            self.list_ispis.clear()
            for d in data:
                if d[0] == self.text_pretraga.text() or d[0][3:5] == self.text_pretraga.text() or \
                   d[0][3:11] == self.text_pretraga.text() or d[0][6:10] == self.text_pretraga.text():

                    self.list_ispis.insertItem(0, f'{d[0]}       {d[1]} {d[2]}       '
                                                  f'{d[4]}       {d[3]}')

                elif d[3] == self.text_pretraga.text():
                    self.list_ispis.insertItem(0, f'{d[0]}       {d[1]} {d[2]}       '
                                                  f'{d[4]}       {d[3]}')

        # Pretraga liste po dropboxu i unosu teksta
        elif self.kategorije_ispisa.currentText() != '...' and self.text_pretraga.text() != '':
            self.list_ispis.clear()
            for d in data:
                if d[3] == self.kategorije_ispisa.currentText() and (d[0] == self.text_pretraga.text() or
                   d[0][3:5] == self.text_pretraga.text() or d[0][3:10] == self.text_pretraga.text()
                        or d[0][6:10] == self.text_pretraga.text()):

                    self.list_ispis.insertItem(0, f'{d[0]}       {d[1]} {d[2]}       '
                                                  f'{d[4]}       {d[3]}')

                elif d[3] == self.text_pretraga.text():
                    self.list_ispis.insertItem(0, f'{d[0]}       {d[1]} {d[2]}       '
                                                  f'{d[4]}       {d[3]}')

    def prikazi_graf(self):
        # Pronalazak id-a za trenutnog korisnika
        query_id = f"""
                            SELECT id, email FROM KORISNIK
                        """

        id = cur.execute(query_id).fetchall()

        for i in id:
            if i[1] == self.text_email.text():
                id_korisnika = i[0]

        # Uzimanje podataka o troškovima
        query = f"""
                            SELECT datum, naziv, cijena FROM trosak
                            LEFT JOIN kategorija ON kategorija.id = trosak.id_kategorije
                            WHERE id_korisnika = {id_korisnika}
                        """

        data = cur.execute(query).fetchall()

        # Prazan prikaz
        if self.kategorije_grafa.currentText() == '...':
            self.linije_prazne = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            self.os_x.setRange(0, 12)
            self.os_y.setRange(0, 1)
            for i in range(1, 13):
                self.linije_prazne.append(i, 0)
            self.graf.addSeries(self.linije_prazne)

        # Grafički prikaz dnevne potrošnje
        elif self.kategorije_grafa.currentText() == 'Dnevni troskovi':
            self.linije_dnevni_troskovi = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            max_y = 0
            min_y = 0
            i = 1
            for d in data:
                if self.kategorije_grafa.currentText() == d[1]:
                    self.linije_dnevni_troskovi.append(i, d[2])
                    i += 1

                    if max_y < d[2]:
                        max_y = d[2]

                    if min_y > d[2] or min_y == 0:
                        min_y = d[2]

            self.os_x.setRange(1, i - 1)
            self.os_x.setTickCount(i - 1)
            self.os_y.setRange(min_y, max_y)
            self.graf.addSeries(self.linije_dnevni_troskovi)

        # Grafički prikaz troškova za namirnice
        elif self.kategorije_grafa.currentText() == 'Namirnice':
            self.linije_namirnice = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            max_y = 0
            min_y = 0
            i = 1
            for d in data:
                if self.kategorije_grafa.currentText() == d[1]:
                    self.linije_namirnice.append(i, d[2])
                    i += 1

                    if max_y < d[2]:
                        max_y = d[2]

                    if min_y > d[2] or min_y == 0:
                        min_y = d[2]

            self.os_x.setRange(1, i - 1)
            self.os_x.setTickCount(i - 1)
            self.os_y.setRange(min_y, max_y)
            self.graf.addSeries(self.linije_namirnice)

        # Grafički prikaz troškova za struju
        elif self.kategorije_grafa.currentText() == 'Struja':
            self.linije_struja = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            max_y = 0
            min_y = 0
            i = 1
            for d in data:
                if self.kategorije_grafa.currentText() == d[1]:
                    self.linije_struja.append(i, d[2])
                    i += 1

                    if max_y < d[2]:
                        max_y = d[2]

                    if min_y > d[2] or min_y == 0:
                        min_y = d[2]

            self.os_x.setRange(1, i - 1)
            self.os_x.setTickCount(i - 1)
            self.os_y.setRange(min_y, max_y)
            self.graf.addSeries(self.linije_struja)

        # Grafički prikaz troškova za plin
        elif self.kategorije_grafa.currentText() == 'Plin':
            self.linije_plin = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            max_y = 0
            min_y = 0
            i = 1
            for d in data:
                if self.kategorije_grafa.currentText() == d[1]:
                    self.linije_plin.append(i, d[2])
                    i += 1

                    if max_y < d[2]:
                        max_y = d[2]

                    if min_y > d[2] or min_y == 0:
                        min_y = d[2]

            self.os_x.setRange(1, i - 1)
            self.os_x.setTickCount(i - 1)
            self.os_y.setRange(min_y, max_y)
            self.graf.addSeries(self.linije_plin)

        # Grafički prikaz troškova za telefon i internet
        elif self.kategorije_grafa.currentText() == 'Telefon_internet':
            self.linije_tel_internet = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            max_y = 0
            min_y = 0
            i = 1
            d_ispis = 0
            for d in data:
                if self.kategorije_grafa.currentText() == d[1]:
                    self.linije_tel_internet.append(i, d[2])
                    i += 1
                    d_ispis = d[2]

                    if max_y < d[2]:
                        max_y = d[2]

                    if min_y > d[2] or min_y == 0:
                        min_y = d[2]

            self.linije_tel_internet.append(i - 1, d_ispis + 0.01)  # Potrebno umetnuti, kako bi se iscrtao graf, pošto
            self.linije_tel_internet.append(i - 1, d_ispis - 0.01)  # su troškovi iste vrijednosti
            self.os_x.setRange(1, i - 1)
            self.os_x.setTickCount(i - 1)
            self.os_y.setRange(min_y-1, max_y+1)
            self.graf.addSeries(self.linije_tel_internet)

        # Grafički prikaz troškova za tv
        elif self.kategorije_grafa.currentText() == 'Tv':
            self.linije_tv = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            max_y = 0
            min_y = 0
            i = 1
            d_ispis = 0
            for d in data:
                if self.kategorije_grafa.currentText() == d[1]:
                    self.linije_tv.append(i, d[2])
                    i += 1
                    d_ispis = d[2]

                    if max_y < d[2]:
                        max_y = d[2]

                    if min_y > d[2] or min_y == 0:
                        min_y = d[2]

            self.linije_tv.append(i-1, d_ispis+0.01)    # Potrebno umetnuti, kako bi se iscrtao graf, pošto su troškovi
            self.linije_tv.append(i-1, d_ispis-0.01)    # iste vrijednosti
            self.os_x.setRange(1, i - 1)
            self.os_x.setTickCount(i - 1)
            self.os_y.setRange(min_y-1, max_y+1)
            self.graf.addSeries(self.linije_tv)

        # Grafički prikaz troškova za komunalno
        elif self.kategorije_grafa.currentText() == 'Komunalno':
            self.linije_komunalno = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            max_y = 0
            min_y = 0
            i = 1
            d_ispis = 0
            for d in data:
                if self.kategorije_grafa.currentText() == d[1]:
                    self.linije_komunalno.append(i, d[2])
                    i += 1
                    d_ispis = d[2]

                    if max_y < d[2]:
                        max_y = d[2]

                    if min_y > d[2] or min_y == 0:
                        min_y = d[2]

            self.linije_komunalno.append(i - 1, d_ispis + 0.01)  # Potrebno umetnuti, kako bi se iscrtao graf, pošto su
            self.linije_komunalno.append(i - 1, d_ispis - 0.01)  # troškovi iste vrijednosti
            self.os_x.setRange(1, i - 1)
            self.os_x.setTickCount(i - 1)
            self.os_y.setRange(min_y-1, max_y+1)
            self.graf.addSeries(self.linije_komunalno)

        # Grafički prikaz troškova za kredit
        elif self.kategorije_grafa.currentText() == 'Kredit':
            self.linije_kredit = QtChart.QLineSeries(self)
            self.graf.removeAllSeries()
            max_y = 0
            min_y = 0
            i = 1
            for d in data:
                if self.kategorije_grafa.currentText() == d[1]:
                    self.linije_kredit.append(i, d[2])
                    i += 1

                    if max_y < d[2]:
                        max_y = d[2]

                    if min_y > d[2] or min_y == 0:
                        min_y = d[2]

            self.os_x.setRange(1, i - 1)
            self.os_x.setTickCount(i - 1)
            self.os_y.setRange(min_y, max_y)
            self.graf.addSeries(self.linije_kredit)


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())

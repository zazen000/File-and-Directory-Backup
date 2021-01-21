import PyQt5
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
        QApplication,
        QWidget,
        QLabel,
        QPushButton,
        QLineEdit,
    )


def qblack(self):
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setGeometry(self.left,self.top,self.width,self.height)
    self.setAutoFillBackground(True)
    p = self.palette()
    p.setColor(self.backgroundRole(), Qt.black)
    self.setPalette(p)


def qbutton(self):
    return "QPushButton {color: rgba(80,130,255,255); background-color: black;}"


def qbutton_dim(self):
    return "QPushButton {color: rgba(54, 136, 200, 250); background-color: black; }"

def qbutton_red(self):
    return "QPushButton {color: rgba(236, 28, 36, 200); background-color: rgba(20, 21, 29, 150);}"

def qbutton_green(self):
    return "QPushButton {color: rgba(6, 186, 39, 250); background-color: rgba(20, 21, 29, 150);}"

def qbutton_blue(self):
    return "QPushButton {color: rgba(54, 136, 200, 250); background-color: rgba(20, 21, 29, 150);}"

def qlabel(self):
    return "QLabel {color: rgba(80,130,255,255); background-color: black;}"

def qlabel_gray(self):
    return "QLabel {color: green; background-color: black;}"


def qledit(self):
    return "QLineEdit {background-color: black; font: normal; color: rgba(162,201,229,255); border: black;}"


def menu_timer(self: object,time: object) -> object:
    self.thread = PyQt5.QtCore.QThread()
    self.thread.start()
    self.timer.start(time)
    self.thread.exit()


def qtframe(self, name, x,y,w,h):
#    self.name = QFrame(self)
    self.name.setFrameShape(QFrame.NoFrame)
    self.name.setGeometry(QRect(x, y, w, h))
    self.name.setStyleSheet('background-color:black')


def qtbutton(self, name, x, y, w, h, style, font, title, connection):
    self.name = QPushButton(self)
    self.name.setStyleSheet(style)
    self.name.setFont(font)
    self.name.setText(title)
    self.name.setGeometry(x, y, w, h)
    self.name.clicked.connect(connection)


def qtlabel(self, name, x, y, w, h, style, font, align,):
    name.setStyleSheet(style)
    name.setAlignment(align)
    name.setFont(font)
    name.setGeometry(x, y, w, h)


def qttimer(self, name, connection):
    self.name.timeout.connect(self.connection)
    self.connection()


def db(database_name, num=1):
    client = MongoClient('localhost',27017)
    db = client[database_name]
    coll = col+num
    for n in num:
        coll = db[coll]
    return


import csv
import sys
import random
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication
from game import Game
from records import Records


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # Итнерфейс из QtDesigner
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setFixedSize(600, 700)
        Main.setWindowIcon(QtGui.QIcon('data/pictures/logo_2048.png'))
        self.centralwidget = QtWidgets.QWidget(parent=Main)
        self.centralwidget.setObjectName("centralwidget")

        self.title_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_image.setGeometry(QtCore.QRect(180, 10, 241, 91))
        self.title_image.setText("")
        self.title_image.setPixmap(
            QtGui.QPixmap("data/pictures/title.jpg"))
        self.title_image.setScaledContents(True)
        self.title_image.setObjectName("title_image")

        self.button_play = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(250, 530, 91, 91))
        self.button_play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/pictures/play.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_play.setIcon(icon)
        self.button_play.setIconSize(QtCore.QSize(80, 80))
        self.button_play.setObjectName("button_play")
        self.button_play.clicked.connect(self.open_window_game)

        self.button_records = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_records.setGeometry(QtCore.QRect(430, 530, 91, 91))
        self.button_records.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data/pictures/records.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_records.setIcon(icon1)
        self.button_records.setIconSize(QtCore.QSize(80, 80))
        self.button_records.setObjectName("button_records")
        self.button_records.clicked.connect(self.open_window_records)

        self.image_4x4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_4x4.setGeometry(QtCore.QRect(70, 110, 181, 181))
        self.image_4x4.setText("")
        self.image_4x4.setPixmap(QtGui.QPixmap("data/pictures/4x4.jpg"))
        self.image_4x4.setScaledContents(True)
        self.image_4x4.setObjectName("image_4x4")

        self.image_5x5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_5x5.setGeometry(QtCore.QRect(340, 110, 181, 181))
        self.image_5x5.setText("")
        self.image_5x5.setPixmap(QtGui.QPixmap("data/pictures/5x5.jpg"))
        self.image_5x5.setScaledContents(True)
        self.image_5x5.setObjectName("image_5x5")

        self.image_6x6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_6x6.setGeometry(QtCore.QRect(70, 320, 181, 181))
        self.image_6x6.setText("")
        self.image_6x6.setPixmap(QtGui.QPixmap("data/pictures/6x6.jpg"))
        self.image_6x6.setScaledContents(True)
        self.image_6x6.setObjectName("image_6x6")

        self.image_8x8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_8x8.setGeometry(QtCore.QRect(340, 320, 181, 181))
        self.image_8x8.setText("")
        self.image_8x8.setPixmap(QtGui.QPixmap("data/pictures/8x8.jpg"))
        self.image_8x8.setScaledContents(True)
        self.image_8x8.setObjectName("image_8x8")

        self.main_radio_buttons = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_radio_buttons.setGeometry(QtCore.QRect(260, 90, 111, 441))
        self.main_radio_buttons.setObjectName("main_radio_buttons")
        self.choose_field = QtWidgets.QGridLayout(self.main_radio_buttons)
        self.choose_field.setContentsMargins(0, 0, 0, 0)
        self.choose_field.setObjectName("choose_field")

        self.choose_4x4 = QtWidgets.QRadioButton(
            parent=self.main_radio_buttons)
        self.choose_4x4.setText("")
        self.choose_4x4.setIconSize(QtCore.QSize(16, 16))
        self.choose_4x4.setObjectName("choose_4x4")
        self.choose_4x4.setChecked(True)
        self.choose_field.addWidget(self.choose_4x4, 0, 0, 1, 1)

        self.choose_5x5 = QtWidgets.QRadioButton(
            parent=self.main_radio_buttons)
        self.choose_5x5.setText("")
        self.choose_5x5.setObjectName("choose_5x5")
        self.choose_field.addWidget(self.choose_5x5, 0, 1, 1, 1)

        self.choose_6x6 = QtWidgets.QRadioButton(
            parent=self.main_radio_buttons)
        self.choose_6x6.setText("")
        self.choose_6x6.setObjectName("choose_6x6")
        self.choose_field.addWidget(self.choose_6x6, 1, 0, 1, 1)

        self.choose_8x8 = QtWidgets.QRadioButton(
            parent=self.main_radio_buttons)
        self.choose_8x8.setText("")
        self.choose_8x8.setObjectName("choose_8x8")
        self.choose_field.addWidget(self.choose_8x8, 1, 1, 1, 1)

        self.text_4x4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text_4x4.setGeometry(QtCore.QRect(130, 290, 71, 31))
        self.text_4x4.setObjectName("text_4x4")

        self.text_5x5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text_5x5.setGeometry(QtCore.QRect(400, 280, 71, 51))
        self.text_5x5.setObjectName("text_5x5")

        self.text_6x6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text_6x6.setGeometry(QtCore.QRect(130, 500, 71, 31))
        self.text_6x6.setObjectName("text_6x6")

        self.text_8x8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text_8x8.setGeometry(QtCore.QRect(400, 500, 71, 31))
        self.text_8x8.setObjectName("text_8x8")

        self.text_play = QtWidgets.QLabel(parent=self.centralwidget)
        self.text_play.setGeometry(QtCore.QRect(260, 620, 81, 31))
        self.text_play.setObjectName("text_play")

        self.text_records = QtWidgets.QLabel(parent=self.centralwidget)
        self.text_records.setGeometry(QtCore.QRect(430, 620, 111, 31))
        self.text_records.setObjectName("text_records")

        self.text_exit = QtWidgets.QLabel(parent=self.centralwidget)
        self.text_exit.setGeometry(QtCore.QRect(100, 620, 71, 31))
        self.text_exit.setObjectName("text_exit")

        self.button_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(90, 530, 91, 91))
        self.button_exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("data/pictures/exit.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_exit.setIcon(icon2)
        self.button_exit.setIconSize(QtCore.QSize(80, 80))
        self.button_exit.setObjectName("button_exit")
        self.button_exit.clicked.connect(self.close)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Игра 2048:Главное окно"))
        self.text_4x4.setText(_translate(
            "Main", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">4 на 4</span></p></body></html>"))
        self.text_6x6.setText(_translate(
            "Main", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">6 на 6</span></p></body></html>"))
        self.text_5x5.setText(_translate(
            "Main", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">5 на 5</span></p></body></html>"))
        self.text_8x8.setText(_translate(
            "Main", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">8 на 8</span></p></body></html>"))
        self.text_play.setText(_translate(
            "Main", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">Играть</span></p></body></html>"))
        self.text_records.setText(_translate(
            "Main", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">Рекорды</span></p></body></html>"))
        self.text_exit.setText(_translate(
            "Main", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">Выйти</span></p></body></html>"))

    # Открытие других окон
    def open_window_game(self):
        if self.choose_4x4.isChecked():
            choose = '4x4'
        elif self.choose_5x5.isChecked():
            choose = '5x5'
        elif self.choose_6x6.isChecked():
            choose = '6x6'
        elif self.choose_8x8.isChecked():
            choose = '8x8'
        self.game_window = Game(choose)
        ex.hide()
        self.game_window.show()

    def open_window_records(self):
        self.records_window = Records()
        self.records_window.show()
        ex.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())

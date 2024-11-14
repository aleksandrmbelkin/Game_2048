import os
import csv
import random

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication


class Game(QMainWindow):
    def __init__(self, choose):
        super().__init__()
        # Обозначение переменных
        self.choose = choose
        self.move_back_flag = False

        # Функции старта
        self.setupUi(self)
        self.restart_hide()
        self.start()

    # Итнерфейс из QtDesigner
    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.setFixedSize(600, 700)
        Game.setWindowIcon(QtGui.QIcon('data/pictures/logo_2048.png'))

        self.game_back_button = QtWidgets.QPushButton(parent=Game)
        self.game_back_button.setGeometry(QtCore.QRect(20, 10, 71, 71))
        self.game_back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/pictures/back.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_back_button.setIcon(icon)
        self.game_back_button.setIconSize(QtCore.QSize(70, 70))
        self.game_back_button.setObjectName("game_back_button")
        self.game_back_button.clicked.connect(self.open_window_main)

        self.game_back_text = QtWidgets.QLabel(parent=Game)
        self.game_back_text.setGeometry(QtCore.QRect(10, 70, 101, 61))
        self.game_back_text.setObjectName("game_back_text")

        self.game_restart_button = QtWidgets.QPushButton(parent=Game)
        self.game_restart_button.setGeometry(QtCore.QRect(490, 610, 61, 61))
        self.game_restart_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data/pictures/restart.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_restart_button.setIcon(icon1)
        self.game_restart_button.setIconSize(QtCore.QSize(60, 60))
        self.game_restart_button.setObjectName("game_restart_button")
        self.game_restart_button.clicked.connect(self.restart_show)

        self.game_restart_text = QtWidgets.QLabel(parent=Game)
        self.game_restart_text.setGeometry(QtCore.QRect(470, 650, 111, 61))
        self.game_restart_text.setObjectName("game_restart_text")

        self.game_move_back_text = QtWidgets.QLabel(parent=Game)
        self.game_move_back_text.setGeometry(QtCore.QRect(20, 650, 131, 61))
        self.game_move_back_text.setObjectName("game_move_back_text")

        self.game_move_back_button = QtWidgets.QPushButton(parent=Game)
        self.game_move_back_button.setGeometry(QtCore.QRect(50, 610, 61, 61))
        self.game_move_back_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("data/pictures/move_back.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_move_back_button.setIcon(icon2)
        self.game_move_back_button.setIconSize(QtCore.QSize(60, 60))
        self.game_move_back_button.setObjectName("game_move_back_button")
        self.game_move_back_button.clicked.connect(self.move_back)

        self.game_record_text = QtWidgets.QLabel(parent=Game)
        self.game_record_text.setGeometry(QtCore.QRect(140, 10, 101, 61))
        self.game_record_text.setObjectName("game_record_text")

        self.game_record_line_edit = QtWidgets.QLineEdit(parent=Game)
        self.game_record_line_edit.setGeometry(QtCore.QRect(252, 29, 301, 31))
        self.game_record_line_edit.setObjectName("game_record_line_edit")
        self.game_record_line_edit.setReadOnly(True)
        with open(f'data/records/{self.choose}.csv', encoding="utf8") as csvfile:
            reader = sorted([i for i in csv.DictReader(
                csvfile, delimiter=';', quotechar='"')], key=lambda x: int(x['score']), reverse=True)
            if len(reader) > 0:
                self.game_record_line_edit.setText(reader[0]['score'])
            else:
                self.game_record_line_edit.setText('Это ваша первая игра')

        self.game_score_text = QtWidgets.QLabel(parent=Game)
        self.game_score_text.setGeometry(QtCore.QRect(170, 60, 71, 61))
        self.game_score_text.setObjectName("game_score_text")

        self.game_score_line_edit = QtWidgets.QLineEdit(parent=Game)
        self.game_score_line_edit.setGeometry(QtCore.QRect(250, 80, 301, 31))
        self.game_score_line_edit.setObjectName("game_score_line_edit")
        self.game_score_line_edit.setReadOnly(True)

        self.game_up_button = QtWidgets.QPushButton(parent=Game)
        self.game_up_button.setGeometry(QtCore.QRect(270, 620, 61, 31))
        self.game_up_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("data/pictures/up.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_up_button.setIcon(icon3)
        self.game_up_button.setIconSize(QtCore.QSize(40, 40))
        self.game_up_button.setObjectName("game_up_button")
        self.game_up_button.clicked.connect(self.move_up)

        self.game_right_button = QtWidgets.QPushButton(parent=Game)
        self.game_right_button.setGeometry(QtCore.QRect(340, 620, 61, 61))
        self.game_right_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("data/pictures/left.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_right_button.setIcon(icon4)
        self.game_right_button.setIconSize(QtCore.QSize(60, 60))
        self.game_right_button.setObjectName("game_right_button")
        self.game_right_button.clicked.connect(self.move_right)

        self.game_left_button = QtWidgets.QPushButton(parent=Game)
        self.game_left_button.setGeometry(QtCore.QRect(200, 620, 61, 61))
        self.game_left_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("data/pictures/right.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_left_button.setIcon(icon5)
        self.game_left_button.setIconSize(QtCore.QSize(60, 60))
        self.game_left_button.setObjectName("game_left_button")
        self.game_left_button.clicked.connect(self.move_left)

        self.game_down_button = QtWidgets.QPushButton(parent=Game)
        self.game_down_button.setGeometry(QtCore.QRect(270, 650, 61, 31))
        self.game_down_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("data/pictures/down.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_down_button.setIcon(icon6)
        self.game_down_button.setIconSize(QtCore.QSize(40, 40))
        self.game_down_button.setObjectName("game_down_button")
        self.game_down_button.clicked.connect(self.move_down)

        self.game_yes_button = QtWidgets.QPushButton(parent=Game)
        self.game_yes_button.setGeometry(QtCore.QRect(410, 630, 31, 31))
        self.game_yes_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("data/pictures/yes.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_yes_button.setIcon(icon7)
        self.game_yes_button.setIconSize(QtCore.QSize(30, 30))
        self.game_yes_button.setObjectName("game_yes_button")
        self.game_yes_button.clicked.connect(self.start)

        self.game_no_button = QtWidgets.QPushButton(parent=Game)
        self.game_no_button.setGeometry(QtCore.QRect(450, 630, 31, 31))
        self.game_no_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("data/pictures/no.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_no_button.setIcon(icon8)
        self.game_no_button.setIconSize(QtCore.QSize(30, 30))
        self.game_no_button.setObjectName("game_no_button")
        self.game_no_button.clicked.connect(self.restart_hide)

        self.gridLayoutWidget = QtWidgets.QWidget(parent=Game)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 130, 501, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.game_field = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.game_field.setContentsMargins(0, 0, 0, 0)
        self.game_field.setObjectName("game_field")

        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate("Game", "Игра 2048:Игра"))
        self.game_back_text.setText(_translate(
            "Game", "<html><head/><body><p><span style=\" \
font-size:22pt; font-weight:600; color:#896b62;\">Назад</span></p></body></html>"))
        self.game_restart_text.setText(_translate(
            "Game", "<html><head/><body><p><span style=\" \
font-size:18pt; font-weight:600; color:#896b62;\">Сначала</span></p></body></html>"))
        self.game_move_back_text.setText(_translate(
            "Game", "<html><head/><body><p><span style=\" \
font-size:18pt; font-weight:600; color:#896b62;\">Ход назад</span></p></body></html>"))
        self.game_record_text.setText(_translate(
            "Game", "<html><head/><body><p><span style=\" \
font-size:18pt; font-weight:600; color:#896b62;\">Рекорд:</span></p></body></html>"))
        self.game_score_text.setText(_translate(
            "Game", "<html><head/><body><p><span style=\" \
font-size:18pt; font-weight:600; color:#896b62;\">Счёт:</span></p></body></html>"))
        self.game_score_line_edit.setText(_translate("Game", "0"))

    # Открытие окна main
    def open_window_main(self):
        Game.close(self)
        os.system(r'python src/python_files/main.py')

    # Запуск игры
    def start(self):
        self.restart_hide()
        print(self.choose)

    # Работа с перезапуском
    def restart_hide(self):
        self.game_yes_button.hide()
        self.game_no_button.hide()

    def restart_show(self):
        self.game_yes_button.show()
        self.game_no_button.show()

    # Шаг назад
    def move_back(self):
        if self.move_back_flag:
            print('Шаг назад')
            self.move_back_flag = False

    # Перемещение
    def move_up(self):
        self.move_back_flag = True
        print('Вверх')

    def move_down(self):
        self.move_back_flag = True
        print('Вниз')

    def move_left(self):
        self.move_back_flag = True
        print('Влево')

    def move_right(self):
        self.move_back_flag = True
        print('Вправо')

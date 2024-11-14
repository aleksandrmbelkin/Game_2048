import os
import csv

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget


class Records(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # Итнерфейс из QtDesigner
    def setupUi(self, Records):
        Records.setObjectName("Records")
        Records.setFixedSize(600, 700)
        Records.setWindowIcon(QtGui.QIcon('data/pictures/logo_2048.png'))

        self.title_records = QtWidgets.QLabel(parent=Records)
        self.title_records.setGeometry(QtCore.QRect(130, 0, 341, 131))
        self.title_records.setObjectName("title_records")

        self.text_records_4x4 = QtWidgets.QLabel(parent=Records)
        self.text_records_4x4.setGeometry(QtCore.QRect(110, 120, 71, 41))
        self.text_records_4x4.setObjectName("text_records_4x4")

        self.text_records_5x5 = QtWidgets.QLabel(parent=Records)
        self.text_records_5x5.setGeometry(QtCore.QRect(410, 120, 71, 41))
        self.text_records_5x5.setObjectName("text_records_5x5")

        self.text_records_6x6 = QtWidgets.QLabel(parent=Records)
        self.text_records_6x6.setGeometry(QtCore.QRect(110, 390, 71, 31))
        self.text_records_6x6.setObjectName("text_records_6x6")

        self.text_records_8x8 = QtWidgets.QLabel(parent=Records)
        self.text_records_8x8.setGeometry(QtCore.QRect(410, 390, 71, 31))
        self.text_records_8x8.setObjectName("text_records_8x8")

        self.records_image_1 = QtWidgets.QLabel(parent=Records)
        self.records_image_1.setGeometry(QtCore.QRect(30, 20, 101, 101))
        self.records_image_1.setText("")
        self.records_image_1.setPixmap(
            QtGui.QPixmap("data/pictures/records.png"))
        self.records_image_1.setScaledContents(True)
        self.records_image_1.setObjectName("records_image_1")

        self.records_image_2 = QtWidgets.QLabel(parent=Records)
        self.records_image_2.setGeometry(QtCore.QRect(470, 20, 101, 101))
        self.records_image_2.setText("")
        self.records_image_2.setPixmap(
            QtGui.QPixmap("data/pictures/records.png"))
        self.records_image_2.setScaledContents(True)
        self.records_image_2.setObjectName("records_image_2")

        self.records_4x4 = QtWidgets.QListWidget(parent=Records)
        self.records_4x4.setGeometry(QtCore.QRect(10, 160, 271, 181))
        self.records_4x4.setObjectName("records_4x4")

        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        item.setFont(font)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_4x4.addItem(item)

        self.records_5x5 = QtWidgets.QListWidget(parent=Records)
        self.records_5x5.setGeometry(QtCore.QRect(310, 160, 271, 181))
        self.records_5x5.setObjectName("records_5x5")

        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        item.setFont(font)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_5x5.addItem(item)

        self.records_6x6 = QtWidgets.QListWidget(parent=Records)
        self.records_6x6.setGeometry(QtCore.QRect(10, 420, 271, 181))
        self.records_6x6.setObjectName("records_6x6")

        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        item.setFont(font)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_6x6.addItem(item)

        self.records_8x8 = QtWidgets.QListWidget(parent=Records)
        self.records_8x8.setGeometry(QtCore.QRect(310, 420, 271, 181))
        self.records_8x8.setObjectName("records_8x8")

        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        item.setFont(font)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.records_8x8.addItem(item)

        self.records_back_button = QtWidgets.QPushButton(parent=Records)
        self.records_back_button.setGeometry(QtCore.QRect(20, 610, 91, 81))
        self.records_back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/pictures/back.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.records_back_button.setIcon(icon)
        self.records_back_button.setIconSize(QtCore.QSize(80, 80))
        self.records_back_button.setObjectName("records_back_button")
        self.records_back_button.clicked.connect(self.open_window_main)

        self.records_back_text = QtWidgets.QLabel(parent=Records)
        self.records_back_text.setGeometry(QtCore.QRect(120, 620, 131, 61))
        self.records_back_text.setObjectName("records_back_text")

        self.retranslateUi(Records)
        QtCore.QMetaObject.connectSlotsByName(Records)

    def retranslateUi(self, Records):
        _translate = QtCore.QCoreApplication.translate
        Records.setWindowTitle(_translate("Records", "Игра 2048:Рекорды"))
        self.title_records.setText(_translate(
            "Records", "<html><head/><body><p align=\"center\"><span style=\" \
font-size:48pt; font-weight:600; color:#fac437;\">Рекорды</span></p></body></html>"))

        self.text_records_4x4.setText(_translate(
            "Records", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">4 на 4</span></p></body></html>"))
        self.text_records_5x5.setText(_translate(
            "Records", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">5 на 5</span></p></body></html>"))
        self.text_records_6x6.setText(_translate(
            "Records", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">6 на 6</span></p></body></html>"))
        self.text_records_8x8.setText(_translate(
            "Records", "<html><head/><body><p><span style=\" font-size:16pt; \
font-weight:600;\">8 на 8</span></p></body></html>"))

        with open('data/records/4x4.csv', encoding="utf8") as csvfile:
            __sortingEnabled = self.records_4x4.isSortingEnabled()
            self.records_4x4.setSortingEnabled(False)

            reader = sorted(sorted([i for i in csv.DictReader(
                csvfile, delimiter=';', quotechar='"')], key=lambda x: x['user_name']), key=lambda x: (int(x['score'])), reverse=True)
            if len(reader) > 0:
                for i in range(len(reader)):
                    if i > 9:
                        break
                    self.records_4x4.item(i).setText(
                        f"{reader[i]['user_name']} - {reader[i]['score']}")

            else:
                item = self.records_4x4.item(0)
                item.setText(_translate("Records", "Пока что здесь пусто :("))
                item = self.records_4x4.item(1)
                item.setText(_translate(
                    "Records", "Начните играть, чтобы здесь что-то появилось"))
                self.records_4x4.setSortingEnabled(__sortingEnabled)

        with open('data/records/5x5.csv', encoding="utf8") as csvfile:
            reader = sorted(sorted([i for i in csv.DictReader(
                csvfile, delimiter=';', quotechar='"')], key=lambda x: x['user_name']), key=lambda x: (int(x['score'])), reverse=True)
            if len(reader) > 0:
                for i in range(len(reader)):
                    if i > 9:
                        break
                    self.records_5x5.item(i).setText(
                        f"{reader[i]['user_name']} - {reader[i]['score']}")
            else:
                __sortingEnabled = self.records_5x5.isSortingEnabled()
                self.records_5x5.setSortingEnabled(False)
                item = self.records_5x5.item(0)
                item.setText(_translate("Records", "Пока что здесь пусто :("))
                item = self.records_5x5.item(1)
                item.setText(_translate(
                    "Records", "Начните играть, чтобы здесь что-то появилось"))
                self.records_5x5.setSortingEnabled(__sortingEnabled)

        with open('data/records/6x6.csv', encoding="utf8") as csvfile:
            reader = sorted(sorted([i for i in csv.DictReader(
                csvfile, delimiter=';', quotechar='"')], key=lambda x: x['user_name']), key=lambda x: (int(x['score'])), reverse=True)
            if len(reader) > 0:
                for i in range(len(reader)):
                    if i > 9:
                        break
                    self.records_6x6.item(i).setText(
                        f"{reader[i]['user_name']} - {reader[i]['score']}")
            else:
                __sortingEnabled = self.records_6x6.isSortingEnabled()
                self.records_6x6.setSortingEnabled(False)
                item = self.records_6x6.item(0)
                item.setText(_translate("Records", "Пока что здесь пусто :("))
                item = self.records_6x6.item(1)
                item.setText(_translate(
                    "Records", "Начните играть, чтобы здесь что-то появилось"))
                self.records_6x6.setSortingEnabled(__sortingEnabled)

        with open('data/records/8x8.csv', encoding="utf8") as csvfile:
            __sortingEnabled = self.records_8x8.isSortingEnabled()
            self.records_8x8.setSortingEnabled(False)

            reader = sorted(sorted([i for i in csv.DictReader(
                csvfile, delimiter=';', quotechar='"')], key=lambda x: x['user_name']), key=lambda x: (int(x['score'])), reverse=True)
            if len(reader) > 0:
                for i in range(len(reader)):
                    if i > 9:
                        break
                    self.records_8x8.item(i).setText(
                        f"{reader[i]['user_name']} - {reader[i]['score']}")
            else:
                item = self.records_8x8.item(0)
                item.setText(_translate("Records", "Пока что здесь пусто :("))
                item = self.records_8x8.item(1)
                item.setText(_translate(
                    "Records", "Начните играть, чтобы здесь что-то появилось"))
                self.records_8x8.setSortingEnabled(__sortingEnabled)

        self.records_back_text.setText(_translate(
            "Records", "<html><head/><body><p><span style=\" \
font-size:28pt; font-weight:600; color:#896b62;\">Назад</span></p></body></html>"))

    # Открытие окна main
    def open_window_main(self):
        Records.close(self)
        os.system(r'python src/python_files/main.py')

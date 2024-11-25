import os
import csv
import random
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QWidget


class Game(QWidget):
    def __init__(self, choose):
        super().__init__()
        # Обозначение переменных
        self.choose = choose
        self.side_length = int(self.choose[0])
        self.cell_size = int(481 / self.side_length -
                             481 / self.side_length * 0.05)
        self.record = 0
        self.in_game_flag = True
        self._translate = QtCore.QCoreApplication.translate
        self.matrix_copy = []

        # Переменные
        self.score = 0
        self.last_score = 0
        self.was_win = False
        self.move_back_flag = False

        # Функции старта
        self.setupUi(self)
        self.start()

    # Итнерфейс из QtDesigner
    def setupUi(self, Game):
        # Настройки окна
        Game.setObjectName("Game")
        Game.setFixedSize(600, 700)
        Game.setWindowIcon(QtGui.QIcon('data/pictures/design/logo_2048.png'))

        # Разные кнопки
        self.game_back_button = QtWidgets.QPushButton(parent=Game)
        self.game_back_button.setGeometry(QtCore.QRect(20, 10, 71, 71))
        self.game_back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/pictures/buttons/back.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_back_button.setIcon(icon)
        self.game_back_button.setIconSize(QtCore.QSize(70, 70))
        self.game_back_button.setObjectName("game_back_button")
        self.game_back_button.clicked.connect(self.exit_)

        self.game_back_text = QtWidgets.QLabel(parent=Game)
        self.game_back_text.setGeometry(QtCore.QRect(10, 70, 101, 61))
        self.game_back_text.setObjectName("game_back_text")

        self.game_restart_button = QtWidgets.QPushButton(parent=Game)
        self.game_restart_button.setGeometry(QtCore.QRect(490, 610, 61, 61))
        self.game_restart_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data/pictures/buttons/restart.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_restart_button.setIcon(icon1)
        self.game_restart_button.setIconSize(QtCore.QSize(60, 60))
        self.game_restart_button.setObjectName("game_restart_button")
        self.game_restart_button.clicked.connect(self.restart_choice_show)

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
        icon2.addPixmap(QtGui.QPixmap("data/pictures/buttons/move_back.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_move_back_button.setIcon(icon2)
        self.game_move_back_button.setIconSize(QtCore.QSize(60, 60))
        self.game_move_back_button.setObjectName("game_move_back_button")
        self.game_move_back_button.clicked.connect(self.move_back)

        # Рекорд и очки
        self.game_record_text = QtWidgets.QLabel(parent=Game)
        self.game_record_text.setGeometry(QtCore.QRect(140, 10, 101, 61))
        self.game_record_text.setObjectName("game_record_text")

        self.game_record_line_edit = QtWidgets.QLineEdit(parent=Game)
        self.game_record_line_edit.setGeometry(QtCore.QRect(252, 29, 301, 31))
        self.game_record_line_edit.setObjectName("game_record_line_edit")
        self.game_record_line_edit.setReadOnly(True)
        with open(f'data/records/rec_{self.choose}.csv', encoding="utf8") as csvfile:
            self.reader = sorted([i for i in csv.DictReader(
                csvfile, delimiter=';', quotechar='"')], key=lambda x: int(x['score']), reverse=True)
            if len(self.reader) > 0:
                self.record = int(self.reader[0]['score'])
                self.game_record_line_edit.setText(str(self.record))
            else:
                self.game_record_line_edit.setText('Это ваша первая игра')

        self.game_score_text = QtWidgets.QLabel(parent=Game)
        self.game_score_text.setGeometry(QtCore.QRect(170, 60, 71, 61))
        self.game_score_text.setObjectName("game_score_text")

        self.game_score_line_edit = QtWidgets.QLineEdit(parent=Game)
        self.game_score_line_edit.setGeometry(QtCore.QRect(250, 80, 301, 31))
        self.game_score_line_edit.setObjectName("game_score_line_edit")
        self.game_score_line_edit.setReadOnly(True)

        # Кнопки управления
        self.game_up_button = QtWidgets.QPushButton(parent=Game)
        self.game_up_button.setGeometry(QtCore.QRect(270, 620, 61, 31))
        self.game_up_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("data/pictures/buttons/up.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_up_button.setIcon(icon3)
        self.game_up_button.setIconSize(QtCore.QSize(40, 40))
        self.game_up_button.setObjectName("game_up_button")
        self.game_up_button.clicked.connect(self.move_up)

        self.game_right_button = QtWidgets.QPushButton(parent=Game)
        self.game_right_button.setGeometry(QtCore.QRect(340, 620, 61, 61))
        self.game_right_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("data/pictures/buttons/left.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_right_button.setIcon(icon4)
        self.game_right_button.setIconSize(QtCore.QSize(60, 60))
        self.game_right_button.setObjectName("game_right_button")
        self.game_right_button.clicked.connect(self.move_right)

        self.game_left_button = QtWidgets.QPushButton(parent=Game)
        self.game_left_button.setGeometry(QtCore.QRect(200, 620, 61, 61))
        self.game_left_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("data/pictures/buttons/right.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_left_button.setIcon(icon5)
        self.game_left_button.setIconSize(QtCore.QSize(60, 60))
        self.game_left_button.setObjectName("game_left_button")
        self.game_left_button.clicked.connect(self.move_left)

        self.game_down_button = QtWidgets.QPushButton(parent=Game)
        self.game_down_button.setGeometry(QtCore.QRect(270, 650, 61, 31))
        self.game_down_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("data/pictures/buttons/down.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_down_button.setIcon(icon6)
        self.game_down_button.setIconSize(QtCore.QSize(40, 40))
        self.game_down_button.setObjectName("game_down_button")
        self.game_down_button.clicked.connect(self.move_down)

        # Кнопки да/нет
        self.game_yes_button = QtWidgets.QPushButton(parent=Game)
        self.game_yes_button.setGeometry(QtCore.QRect(410, 630, 31, 31))
        self.game_yes_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("data/pictures/buttons/yes.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_yes_button.setIcon(icon7)
        self.game_yes_button.setIconSize(QtCore.QSize(30, 30))
        self.game_yes_button.setObjectName("game_yes_button")
        self.game_yes_button.clicked.connect(self.start)

        self.game_no_button = QtWidgets.QPushButton(parent=Game)
        self.game_no_button.setGeometry(QtCore.QRect(450, 630, 31, 31))
        self.game_no_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("data/pictures/buttons/no.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_no_button.setIcon(icon8)
        self.game_no_button.setIconSize(QtCore.QSize(30, 30))
        self.game_no_button.setObjectName("game_no_button")
        self.game_no_button.clicked.connect(self.start_hide)

        # Создание игрового поля
        # -----------------------------------

        # Таблица поля
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Game)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 130, 481, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.game_field = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.game_field.setContentsMargins(0, 0, 0, 0)
        self.game_field.setObjectName("game_field")

        # Добавление клеток
        for i in range(self.side_length):
            for j in range(self.side_length):
                cell = QtWidgets.QLabel(parent=Game)
                cell.setFixedSize(self.cell_size, self.cell_size)
                cell.setObjectName(f"cell_{i}_{j}")
                cell.setStyleSheet(
                    'background-color: #bfbfbf;')
                self.game_field.addWidget(cell, j, i)

        # Конец игры
        self.game_end = QtWidgets.QLabel(parent=Game)
        self.game_end.setGeometry(QtCore.QRect(110, 140, 371, 61))
        self.game_end.setObjectName("game_end")

        self.game_end_new_record = QtWidgets.QLabel(parent=Game)
        self.game_end_new_record.setGeometry(QtCore.QRect(200, 190, 191, 61))
        self.game_end_new_record.setObjectName("game_end_new_record")

        self.game_end_user_text = QtWidgets.QLabel(parent=Game)
        self.game_end_user_text.setGeometry(QtCore.QRect(210, 310, 171, 61))
        self.game_end_user_text.setObjectName("game_end_user_text")

        self.game_end_user_input = QtWidgets.QLineEdit(parent=Game)
        self.game_end_user_input.setGeometry(QtCore.QRect(190, 360, 221, 31))
        self.game_end_user_input.setObjectName("game_end_user_input")
        self.game_end_user_input.setMaxLength(20)

        self.game_restart_button_end = QtWidgets.QPushButton(parent=Game)
        self.game_restart_button_end.setGeometry(
            QtCore.QRect(430, 470, 71, 71))
        self.game_restart_button_end.setText("")
        self.game_restart_button_end.setIcon(icon1)
        self.game_restart_button_end.setIconSize(QtCore.QSize(70, 70))
        self.game_restart_button_end.setObjectName("game_restart_button_end")
        self.game_restart_button_end.clicked.connect(self.end_restart_button)

        self.game_restart_text_end = QtWidgets.QLabel(parent=Game)
        self.game_restart_text_end.setGeometry(QtCore.QRect(410, 530, 111, 61))
        self.game_restart_text_end.setObjectName("game_restart_text_end")

        self.game_back_button_end = QtWidgets.QPushButton(parent=Game)
        self.game_back_button_end.setGeometry(QtCore.QRect(100, 470, 71, 71))
        self.game_back_button_end.setText("")
        self.game_back_button_end.setIcon(icon)
        self.game_back_button_end.setIconSize(QtCore.QSize(70, 70))
        self.game_back_button_end.setObjectName("game_back_button_end")
        self.game_back_button_end.clicked.connect(self.open_window_main_end)

        self.game_back_text_end = QtWidgets.QLabel(parent=Game)
        self.game_back_text_end.setGeometry(QtCore.QRect(90, 530, 101, 61))
        self.game_back_text_end.setObjectName("game_back_text_end")

        self.game_end_error = QtWidgets.QLabel(parent=Game)
        self.game_end_error.setGeometry(QtCore.QRect(160, 410, 281, 61))
        self.game_end_error.setObjectName("game_end_error")

        # Достижение 2048
        self.game_win_text = QtWidgets.QLabel(parent=Game)
        self.game_win_text.setGeometry(QtCore.QRect(60, 170, 481, 161))
        self.game_win_text.setObjectName("game_win_text")

        self.game_continue_button = QtWidgets.QPushButton(parent=Game)
        self.game_continue_button.setGeometry(QtCore.QRect(190, 330, 221, 41))
        self.game_continue_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("data/pictures/buttons/play.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.game_continue_button.setIcon(icon9)
        self.game_continue_button.setIconSize(QtCore.QSize(40, 40))
        self.game_continue_button.setObjectName("game_continue_button")
        self.game_continue_button.clicked.connect(self.close_win_game)

        self.game_continue_text = QtWidgets.QLabel(parent=Game)
        self.game_continue_text.setGeometry(QtCore.QRect(210, 360, 191, 61))
        self.game_continue_text.setObjectName("game_continue_text")

        # Декор
        self.game_win_image_1 = QtWidgets.QLabel(parent=Game)
        self.game_win_image_1.setGeometry(QtCore.QRect(10, 590, 101, 101))
        self.game_win_image_1.setText("")
        self.game_win_image_1.setPixmap(
            QtGui.QPixmap("data/pictures/buttons/records.png"))
        self.game_win_image_1.setScaledContents(True)
        self.game_win_image_1.setObjectName("game_win_image_1")

        self.game_win_image_2 = QtWidgets.QLabel(parent=Game)
        self.game_win_image_2.setGeometry(QtCore.QRect(490, 590, 101, 101))
        self.game_win_image_2.setText("")
        self.game_win_image_2.setPixmap(
            QtGui.QPixmap("data/pictures/buttons/records.png"))
        self.game_win_image_2.setScaledContents(True)
        self.game_win_image_2.setObjectName("game_win_image_2")

        self.game_win_image_3 = QtWidgets.QLabel(parent=Game)
        self.game_win_image_3.setGeometry(QtCore.QRect(490, 10, 101, 101))
        self.game_win_image_3.setText("")
        self.game_win_image_3.setPixmap(
            QtGui.QPixmap("data/pictures/buttons/records.png"))
        self.game_win_image_3.setScaledContents(True)
        self.game_win_image_3.setObjectName("game_win_image_3")

        self.game_win_image_4 = QtWidgets.QLabel(parent=Game)
        self.game_win_image_4.setGeometry(QtCore.QRect(10, 10, 101, 101))
        self.game_win_image_4.setText("")
        self.game_win_image_4.setPixmap(
            QtGui.QPixmap("data/pictures/buttons/records.png"))
        self.game_win_image_4.setScaledContents(True)
        self.game_win_image_4.setObjectName("game_win_image_4")

        # Подключение retranslateUi
        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        Game.setWindowTitle(self._translate("Game", "Игра 2048:Игра"))
        self.game_back_text.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:22pt; font-weight:600; color:#896b62;\">Назад</span></p></body></html>"))
        self.game_restart_text.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:18pt; font-weight:600; color:#896b62;\">Сначала</span></p></body></html>"))
        self.game_move_back_text.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:18pt; font-weight:600; color:#896b62;\">Ход назад</span></p></body></html>"))
        self.game_record_text.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:18pt; font-weight:600; color:#896b62;\">Рекорд:</span></p></body></html>"))
        self.game_score_text.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:18pt; font-weight:600; color:#896b62;\">Счёт:</span></p></body></html>"))
        self.game_score_line_edit.setText(
            self._translate("Game", str(self.score)))
        self.game_end.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:36pt; font-weight:600; color:#896b62;\">Игра окончена</span></p></body></html>"))
        self.game_end_new_record.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:18pt; font-weight:600; color:#896b62;\">Новый рекорд!</span></p></body></html>"))
        self.game_restart_text_end.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:22pt; font-weight:600; color:#896b62;\">Заново</span></p></body></html>"))
        self.game_back_text_end.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:22pt; font-weight:600; color:#896b62;\">Назад</span></p></body></html>"))
        self.game_end_error.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:18pt; font-weight:600; color:#896b62;\">Сначала введите имя!</span></p></body></html>"))
        self.game_end_user_text.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:18pt; font-weight:600; color:#896b62;\">Введите имя:</span></p></body></html>"))
        self.game_win_text.setText(self._translate(
            "Game", "<html><head/><body><p align=\"center\"><span style=\" \
                font-size:36pt; font-weight:600; color:#896b62;\">Победа!</span></p><p align=\"center\"><span style=\" \
                font-size:36pt; font-weight:600; color:#896b62;\">Вы дошли до 2048!</span></p></body></html>"))
        self.game_continue_text.setText(self._translate(
            "Game", "<html><head/><body><p><span style=\" \
                font-size:22pt; font-weight:600; color:#896b62;\">Продолжить</span></p></body></html>"))

    # Функции
    # -------------------

    # Открытие окна main
    def open_window_main(self):
        Game.close(self)
        os.system(r'python src/python_files/main.py')

    def open_window_main_end(self):
        if self.game_end_user_input.text().strip() != '':
            self.save_records()
            self.open_window_main()
        else:
            self.game_end_error.show()

    # Запуск игры
    def start(self):
        with open(f'data/saves/variables/var_{self.choose}', 'r', encoding="utf8") as f:
            variables = f.read()
            if variables == '':
                self.score = 0
                self.last_score = 0
                self.was_win = False
                self.move_back_flag = False
            else:
                variables_lines = variables.split('\n')
                self.score = int(variables_lines[0])
                self.last_score = int(variables_lines[1])
                self.was_win = bool(int(variables_lines[2]))
                self.move_back_flag = bool(int(variables_lines[3]))

        with open(f'data/records/rec_{self.choose}.csv', encoding="utf8") as csvfile:
            self.reader = sorted([i for i in csv.DictReader(
                csvfile, delimiter=';', quotechar='"')], key=lambda x: int(x['score']), reverse=True)
            if len(self.reader) > 0:
                self.record = int(self.reader[0]['score'])
                self.game_record_line_edit.setText(str(self.record))
            else:
                self.game_record_line_edit.setText('Это ваша первая игра')

        self.game_score_line_edit.setText(
            self._translate("Game", str(self.score)))

        with open(f'data/saves/locations/loc_now_{self.choose}', 'r', encoding="utf8") as f_now:
            locations = f_now.read()
            if locations == '':
                with open(f'data/saves/locations/loc_last_{self.choose}', 'w', encoding="utf8") as f_last:
                    f_last.write('')
                with open(f'data/saves/variables/var_{self.choose}', 'w', encoding="utf8") as f:
                    f.write('')
                self.game_field_matrix = [
                    ['None'] * self.side_length for _ in range(self.side_length)]
                self.game_field_matrix_last = [
                    ['None'] * self.side_length for _ in range(self.side_length)]
                self.generate_random_cell()
                self.generate_random_cell()
                self.move_back_flag = False
            else:
                self.game_field_matrix = []
                locations_lines = locations.split('\n')
                for _ in range(self.side_length):
                    self.game_field_matrix.append([])
                for i in range(self.side_length):
                    for j in locations_lines[i].split(';'):
                        if j == 'None':
                            self.game_field_matrix[i].append('None')
                        else:
                            self.game_field_matrix[i].append(int(j))

                with open(f'data/saves/locations/loc_last_{self.choose}', 'r', encoding="utf8") as f_last:
                    locations = f_last.read()
                    if locations == '':
                        self.update_matrix_last()
                    else:
                        self.game_field_matrix_last = []
                        locations_lines = locations.split('\n')
                        for _ in range(self.side_length):
                            self.game_field_matrix_last.append([])
                        for i in range(self.side_length):
                            for j in locations_lines[i].split(';'):
                                if j == 'None':
                                    self.game_field_matrix_last[i].append(
                                        'None')
                                else:
                                    self.game_field_matrix_last[i].append(
                                        int(j))

        self.game_score_text.setGeometry(QtCore.QRect(170, 60, 71, 61))
        self.game_score_line_edit.setGeometry(
            QtCore.QRect(250, 80, 301, 31))
        self.start_hide()
        self.start_show()
        self.update_field()

    def start_show(self):
        self.game_back_button.show()
        self.game_back_text.show()
        self.game_restart_button.show()
        self.game_restart_text.show()
        self.game_move_back_text.show()
        self.game_move_back_button.show()
        self.game_record_text.show()
        self.game_record_line_edit.show()
        self.game_up_button.show()
        self.game_right_button.show()
        self.game_left_button.show()
        self.game_down_button.show()
        self.game_score_text.show()
        self.game_score_line_edit.show()
        for i in range(self.side_length ** 2):
            self.game_field.itemAt(i).widget().show()

    def start_hide(self):
        self.game_yes_button.hide()
        self.game_no_button.hide()
        self.game_end.hide()
        self.game_end_new_record.hide()
        self.game_end_user_text.hide()
        self.game_end_user_input.hide()
        self.game_restart_button_end.hide()
        self.game_restart_text_end.hide()
        self.game_back_button_end.hide()
        self.game_back_text_end.hide()
        self.game_end_error.hide()
        self.game_win_text.hide()
        self.game_continue_button.hide()
        self.game_continue_text.hide()
        self.game_win_image_1.hide()
        self.game_win_image_2.hide()
        self.game_win_image_3.hide()
        self.game_win_image_4.hide()

    def restart_choice_show(self):
        self.game_yes_button.show()
        self.game_no_button.show()

    # Шаг назад
    def move_back(self):
        if self.move_back_flag:
            self.move_back_flag = False
            self.game_field_matrix = []

            for i in self.game_field_matrix_last:
                self.game_field_matrix.append(i[::])
            self.update_field()
            self.score = self.last_score

            self.game_score_line_edit.setText(
                self._translate("Game", str(self.last_score)))

            find_2048 = False
            for i in range(self.side_length):
                for j in range(self.side_length):
                    if isinstance(self.game_field_matrix[i][j], int):
                        if self.game_field_matrix[i][j] >= 2048:
                            self.was_win = True
                            find_2048 = True
                            break
            if not find_2048:
                self.was_win = False

    # Перемещение
    def move_up(self):
        self.matrix_copy = self.copy_field()

        for x in range(self.side_length):
            for y in range(1, self.side_length):
                cell_y = y
                while True:
                    if cell_y == 0:
                        break

                    cell = self.game_field_matrix[cell_y][x]
                    if cell != 'None':
                        cell_up = self.game_field_matrix[cell_y - 1][x]
                        if cell_up != cell and cell_up != 'None' or cell_up == 32768:
                            break

                        elif cell_up == 'None':
                            self.game_field_matrix[cell_y - 1][x] = cell
                            self.game_field_matrix[cell_y][x] = cell_up

                        elif cell_up == cell:
                            if isinstance(cell_up, str):
                                if 'united' in cell_up:
                                    break
                            self.game_field_matrix[cell_y -
                                                   1][x] = f'{cell * 2}united'
                            self.game_field_matrix[cell_y][x] = 'None'
                            self.last_score = self.score
                            self.score += cell * 2

                    cell_y -= 1

        self.post_processing()
        if self.game_field_matrix != self.matrix_copy:
            self.update_matrix_last()

    def move_down(self):
        self.matrix_copy = self.copy_field()

        for x in range(self.side_length):
            for y in range(self.side_length - 2, -1, -1):
                cell_y = y
                while True:
                    if cell_y == self.side_length - 1:
                        break

                    cell = self.game_field_matrix[cell_y][x]
                    if cell != 'None':
                        cell_down = self.game_field_matrix[cell_y + 1][x]
                        if cell_down != cell and cell_down != 'None' or cell_down == 32768:
                            break

                        elif cell_down == 'None':
                            self.game_field_matrix[cell_y + 1][x] = cell
                            self.game_field_matrix[cell_y][x] = cell_down

                        elif cell_down == cell:
                            if isinstance(cell_down, str):
                                if 'united' in cell_down:
                                    break
                            self.game_field_matrix[cell_y +
                                                   1][x] = f'{cell * 2}united'
                            self.game_field_matrix[cell_y][x] = 'None'
                            self.last_score = self.score
                            self.score += cell * 2

                    cell_y += 1

        self.post_processing()
        if self.game_field_matrix != self.matrix_copy:
            self.update_matrix_last()

    def move_left(self):
        self.matrix_copy = self.copy_field()

        for x in range(1, self.side_length):
            for y in range(self.side_length):
                cell_x = x
                while True:
                    if cell_x == 0:
                        break

                    cell = self.game_field_matrix[y][cell_x]
                    if cell != 'None':
                        cell_left = self.game_field_matrix[y][cell_x - 1]
                        if cell_left != cell and cell_left != 'None' or cell_left == 32768:
                            break

                        elif cell_left == 'None':
                            self.game_field_matrix[y][cell_x - 1] = cell
                            self.game_field_matrix[y][cell_x] = cell_left

                        elif cell_left == cell:
                            if isinstance(cell_left, str):
                                if 'united' in cell_left:
                                    break
                            self.game_field_matrix[y][cell_x -
                                                      1] = f'{cell * 2}united'
                            self.game_field_matrix[y][cell_x] = 'None'
                            self.last_score = self.score
                            self.score += cell * 2

                    cell_x -= 1

        self.post_processing()
        if self.game_field_matrix != self.matrix_copy:
            self.update_matrix_last()

    def move_right(self):
        self.matrix_copy = self.copy_field()

        for x in range(self.side_length - 2, -1, -1):
            for y in range(self.side_length):
                cell_x = x
                while True:
                    if cell_x == self.side_length - 1:
                        break

                    cell = self.game_field_matrix[y][cell_x]
                    if cell != 'None':
                        cell_right = self.game_field_matrix[y][cell_x + 1]
                        if cell_right != cell and cell_right != 'None' or cell_right == 32768:
                            break

                        elif cell_right == 'None':
                            self.game_field_matrix[y][cell_x + 1] = cell
                            self.game_field_matrix[y][cell_x] = cell_right

                        elif cell_right == cell:
                            if isinstance(cell_right, str):
                                if 'united' in cell_right:
                                    break
                            self.game_field_matrix[y][cell_x +
                                                      1] = f'{cell * 2}united'
                            self.game_field_matrix[y][cell_x] = 'None'
                            self.last_score = self.score
                            self.score += cell * 2

                    cell_x += 1

        self.post_processing()
        if self.game_field_matrix != self.matrix_copy:
            self.update_matrix_last()

    def keyPressEvent(self, event):
        if self.in_game_flag:
            if str(event.key()) == '87':  # W
                self.move_up()
            elif str(event.key()) == '83':  # S
                self.move_down()
            elif str(event.key()) == '65':  # A
                self.move_left()
            elif str(event.key()) == '68':  # D
                self.move_right()

            elif str(event.key()) == '1062':  # Ц
                self.move_up()
            elif str(event.key()) == '1067':  # Ы
                self.move_down()
            elif str(event.key()) == '1060':  # Ф
                self.move_left()
            elif str(event.key()) == '1042':  # В
                self.move_right()

            elif str(event.key()) == '90':  # Z
                self.move_up()
                self.move_down()
                self.move_left()
                self.move_right()

    # Достижение 2048
    def win_game(self):
        self.in_game_flag = False
        self.end_hide()
        self.game_win_text.show()
        self.game_continue_button.show()
        self.game_continue_text.show()
        self.game_score_text.hide()
        self.game_score_line_edit.hide()
        self.decor_show()

    def close_win_game(self):
        self.in_game_flag = True
        self.start_hide()
        self.start_show()

    # Конец игры
    def end_game(self):
        self.in_game_flag = False
        self.end_hide()
        self.end_show()
        self.decor_show()
        self.game_score_text.setGeometry(QtCore.QRect(100, 250, 71, 61))
        self.game_score_line_edit.setGeometry(QtCore.QRect(180, 270, 301, 31))

        with open(f'data/saves/locations/loc_now_{self.choose}', 'w', encoding="utf8") as f_now:
            f_now.write('')
        with open(f'data/saves/locations/loc_last_{self.choose}', 'w', encoding="utf8") as f_last:
            f_last.write('')
        with open(f'data/saves/variables/var_{self.choose}', 'w', encoding="utf8") as f:
            f.write('')

    def end_hide(self):
        self.game_back_button.hide()
        self.game_back_text.hide()
        self.game_restart_button.hide()
        self.game_restart_text.hide()
        self.game_move_back_text.hide()
        self.game_move_back_button.hide()
        self.game_record_text.hide()
        self.game_record_line_edit.hide()
        self.game_up_button.hide()
        self.game_right_button.hide()
        self.game_left_button.hide()
        self.game_down_button.hide()
        for i in range(self.side_length ** 2):
            self.game_field.itemAt(i).widget().hide()

    def end_show(self):
        self.game_end.show()
        if self.score >= self.record:
            self.game_end_new_record.show()
        self.game_end_user_text.show()
        self.game_end_user_input.show()
        self.game_restart_button_end.show()
        self.game_restart_text_end.show()
        self.game_back_button_end.show()
        self.game_back_text_end.show()

    def end_restart_button(self):
        if self.game_end_user_input.text().strip() != '':
            self.save_records()
            self.start()
        else:
            self.game_end_error.show()

    def decor_show(self):
        self.game_win_image_1.show()
        self.game_win_image_2.show()
        self.game_win_image_3.show()
        self.game_win_image_4.show()

    # Сохранить рекорды
    def save_records(self):
        with open(f'data/records/rec_{self.choose}.csv', 'a', encoding="utf8") as csvfile:
            new_record = f'{self.game_end_user_input.text().strip()};{self.game_score_line_edit.text()}\n'
            csvfile.write(new_record)
        self.game_end_user_input.setText('')

    # Генерация числа для случайной клетки
    def generate_random_cell(self):
        while True:
            randomizer1 = random.randint(0, self.side_length - 1)
            randomizer2 = random.randint(0, self.side_length - 1)
            x, y = randomizer1, randomizer2
            if self.game_field_matrix[y][x] == 'None':
                break

        randomizer = random.randint(1, 10)
        if randomizer < 10:
            number = 2
        else:
            number = 4

        self.game_field_matrix[y][x] = number

    # Обновление изображений на поле
    def update_field(self):
        for y in range(self.side_length):
            for x in range(self.side_length):
                number = self.game_field_matrix[y][x]
                if self.game_field_matrix[y][x] != 'None':
                    self.game_field.itemAt(x * self.side_length + y).widget().setPixmap(
                        QtGui.QPixmap(f"data/pictures/cells/cell_{number}.png").scaledToWidth(self.cell_size))
                else:
                    self.game_field.itemAt(
                        x * self.side_length + y).widget().setText(' ')

    def check_record(self):
        if self.score > self.record:
            self.game_record_line_edit.setText(str(self.score))

    def post_processing(self):
        for i in range(self.side_length):
            for j in range(self.side_length):
                if isinstance(self.game_field_matrix[i][j], str):
                    if 'united' in self.game_field_matrix[i][j]:
                        self.game_field_matrix[i][j] = int(
                            self.game_field_matrix[i][j].replace('united', ''))

        if self.game_field_matrix != self.matrix_copy:
            self.game_score_line_edit.setText(
                self._translate("Game", str(self.score)))
            self.check_record()
            self.move_back_flag = True
            self.generate_random_cell()
            self.update_field()

        if not self.check_end_game():
            if not self.was_win:
                for i in range(self.side_length):
                    if not self.was_win:
                        for j in range(self.side_length):
                            if self.game_field_matrix[i][j] == 2048:
                                self.was_win = True
                                self.win_game()
                                break

        if self.check_end_game():
            self.end_game()

    # Копии
    def update_matrix_last(self):
        self.game_field_matrix_last = []
        for i in self.matrix_copy:
            self.game_field_matrix_last.append(i[::])

    def copy_field(self):
        matrix = []
        for i in self.game_field_matrix:
            matrix.append(i[::])
        return matrix

    # Сохранение игры
    def save_game(self):
        with open(f'data/saves/variables/var_{self.choose}', 'w', encoding="utf8") as f:
            variables = f'{self.score}\n{self.last_score}\n{int(self.was_win)}\n{int(self.move_back_flag)}'
            f.write(variables)

        with open(f'data/saves/locations/loc_now_{self.choose}', 'w', encoding="utf8") as f:
            field = ''
            for i in range(self.side_length):
                for j in self.game_field_matrix[i]:
                    field += f'{j};'
                field = field[:-1]
                field += '\n'
            field = field[:-1]
            f.write(field)

        with open(f'data/saves/locations/loc_last_{self.choose}', 'w', encoding="utf8") as f:
            field = ''
            for i in range(self.side_length):
                for j in self.game_field_matrix_last[i]:
                    field += f'{j};'
                field = field[:-1]
                field += '\n'
            field = field[:-1]
            f.write(field)

    # Выход с сохранением
    def exit_(self):
        self.save_game()
        self.open_window_main()

    # Проверка на конец игры
    def check_end_game(self):
        for x in range(self.side_length):
            for y in range(1, self.side_length):
                cell = self.game_field_matrix[y][x]
                cell_up = self.game_field_matrix[y - 1][x]
                if cell_up == 'None' or cell_up == cell and cell_up != 32768:
                    return False

        for x in range(self.side_length):
            for y in range(self.side_length - 2, -1, -1):
                cell = self.game_field_matrix[y][x]
                cell_down = self.game_field_matrix[y + 1][x]
                if cell_down == 'None' or cell_down == cell and cell_down != 32768:
                    return False

        for x in range(1, self.side_length):
            for y in range(self.side_length):
                cell = self.game_field_matrix[x][y]
                cell_right = self.game_field_matrix[x - 1][y]
                if cell_right == 'None' or cell_right == cell and cell_right != 32768:
                    return False

        for x in range(self.side_length - 2, -1, -1):
            for y in range(self.side_length):
                cell = self.game_field_matrix[x][y]
                cell_left = self.game_field_matrix[x + 1][y]
                if cell_left == 'None' or cell_left == cell and cell_left != 32768:
                    return False

        return True

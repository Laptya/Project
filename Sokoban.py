from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QGridLayout, QPushButton, QMessageBox, QApplication, QWidget, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class Game_Form(QWidget):
    def __init__(self):
        super().__init__()

    def start(self, file_number):
        self.setFixedSize(800, 600)
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        self.setWindowTitle('Game')

        self.current_levelnumber = file_number
        self.game_files = [file for file in os.listdir('./Levels') if file.endswith(".txt")]
        with open('./Levels/'+self.game_files[self.current_levelnumber], 'r') as file:
            self.matrix = []
            position_box = []
            location = []
            position_player = []
            a = ''
            while '\n' not in a:
                a += file.read(1)
            self.y = int(a)

            a = ''
            while '\n' not in a:
                a += file.read(1)
            self.x = int(a)

            for i in range(self.y):
                line = ''
                for j in range(self.x):
                    a = file.read(1)
                    line += a
                    if a == 'B':
                        position_box.append([i, j])
                    elif a == 'H':
                        position_player.append([i, j])
                    elif a == 'L':
                        location.append([i, j])
                file.read(1)
                self.matrix.append([*line])





        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setAlignment(Qt.AlignCenter)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.But_Up = QtWidgets.QPushButton(self)
        self.But_Up.setGeometry(QtCore.QRect(360, 490, 81, 23))

        self.But_Left = QtWidgets.QPushButton(self)
        self.But_Left.setGeometry(QtCore.QRect(300, 520, 81, 23))

        self.But_Right = QtWidgets.QPushButton(self)
        self.But_Right.setGeometry(QtCore.QRect(420, 520, 81, 23))

        self.But_Down = QtWidgets.QPushButton(self)
        self.But_Down.setGeometry(QtCore.QRect(360, 550, 81, 23))

        self.But_Exit = QtWidgets.QPushButton(self)
        self.But_Exit.setGeometry(QtCore.QRect(5, 5, 80, 60))
        self.But_Restart = QtWidgets.QPushButton(self)
        self.But_Restart.setGeometry(QtCore.QRect(5, 75, 80, 60))

        self.But_Up.setText("↑")
        self.But_Left.setText("←")
        self.But_Right.setText("→")
        self.But_Down.setText("↓")
        self.But_Exit.setText("Меню")
        self.But_Restart.setText("Заново")

        self.position_box = []
        self.location = []
        self.position_player = []
        self.ready = True

        for i in range(self.y):
            for j in range(self.x):
                if self.matrix[i][j] == 'B':
                    label = QLabel()
                    pixmap = QPixmap('images/crate1.png')
                    label.setPixmap(pixmap)
                    self.position_box.append([i, j])
                    self.gridLayout.addWidget(label, i, j)

                elif self.matrix[i][j] == 'W':
                    label = QLabel()
                    pixmap = QPixmap('images/wall.png')
                    label.setPixmap(pixmap)
                    self.gridLayout.addWidget(label, i, j)

                elif self.matrix[i][j] == 'H':
                    label = QLabel()
                    pixmap = QPixmap('images/hero.png')
                    label.setPixmap(pixmap)
                    self.position_player.append([i,j])
                    self.gridLayout.addWidget(label, i, j)

                elif self.matrix[i][j] == 'Q':
                    label = QLabel()
                    pixmap = QPixmap('images/crate2.png')
                    label.setPixmap(pixmap)
                    self.gridLayout.addWidget(label, i, j)

                elif self.matrix[i][j] == 'L':
                    label = QLabel()
                    pixmap = QPixmap('images/loc.png')
                    label.setPixmap(pixmap)
                    self.location.append([i, j])
                    self.gridLayout.addWidget(label, i, j)
        self.gridLayout.setSpacing(0)

        self.game()

    def game(self):
        if self.ready == True:
            self.But_Up.clicked.connect(lambda: self.check(0,-1))
            self.But_Down.clicked.connect(lambda: self.check(0,1))
            self.But_Right.clicked.connect(lambda: self.check(1,0))
            self.But_Left.clicked.connect(lambda: self.check(-1,0))
            self.But_Exit.clicked.connect(lambda: self.Menu())
            self.But_Restart.clicked.connect(lambda: self.Restart())

    def Restart(self):
        self.close()
        self.NewForm = Game_Form()
        self.NewForm.start(self.current_levelnumber)
        self.NewForm.show()

    def Menu(self):
        self.close()
        self.newwForm = Menu()
        self.newwForm.show()

    def check(self, x, y):
        self.ready = False
        if (self.matrix[self.position_player[0][0] + y][self.position_player[0][1] + x] == '.' or
                self.matrix[self.position_player[0][0] + y][self.position_player[0][1] + x] == 'L'):
            self.matrix[self.position_player[0][0]][self.position_player[0][1]] = '.'
            self.position_player[0][0] = self.position_player[0][0] + y
            self.position_player[0][1] = self.position_player[0][1] + x

        elif (self.matrix[self.position_player[0][0] + y][self.position_player[0][1] + x] == 'B' or
              self.matrix[self.position_player[0][0] + y][self.position_player[0][1] + x] == 'Q') and (
                self.matrix[self.position_player[0][0] + y * 2][self.position_player[0][1] + x * 2] == '.' or
                self.matrix[self.position_player[0][0] + y * 2][self.position_player[0][1] + x * 2] == 'L'):
            for i in range(len(self.position_box)):
                if (self.position_player[0][0] + y == self.position_box[i][0]) and (
                        self.position_player[0][1] + x == self.position_box[i][1]):
                    self.matrix[self.position_box[i][0]][self.position_box[i][1]] = '.'
                    self.position_box[i][0] = self.position_box[i][0] + y
                    self.position_box[i][1] = self.position_box[i][1] + x

        self.update()

    def update(self):

        self.count = 0

        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().deleteLater()

        for i in range(len(self.location)):
            self.matrix[self.location[i][0]][self.location[i][1]] = 'L'

        for i in range(len(self.position_box)):
            self.matrix[self.position_box[i][0]][self.position_box[i][1]] = 'B'

        for i in range(len(self.location)):
            if self.matrix[self.location[i][0]][self.location[i][1]] == 'B':
                self.count += 1
                self.matrix[self.location[i][0]][self.location[i][1]] = 'Q'

        self.matrix[self.position_player[0][0]][self.position_player[0][1]] = 'H'

        for i in range(self.y):
            for j in range(self.x):
                if self.matrix[i][j] == 'B':
                    self.label = QLabel()
                    self.pixmap = QPixmap('images/crate1.png')
                    self.label.setPixmap(self.pixmap)
                    self.gridLayout.addWidget(self.label, i, j)

                elif self.matrix[i][j] == 'W':
                    self.label = QLabel()
                    self.pixmap = QPixmap('images/wall.png')
                    self.label.setPixmap(self.pixmap)
                    self.gridLayout.addWidget(self.label, i, j)

                elif self.matrix[i][j] == 'H':
                    self.label = QLabel()
                    self.pixmap = QPixmap('images/hero.png')
                    self.label.setPixmap(self.pixmap)
                    self.gridLayout.addWidget(self.label, i, j)

                elif self.matrix[i][j] == 'Q':
                    self.label = QLabel()
                    self.pixmap = QPixmap('images/crate2.png')
                    self.label.setPixmap(self.pixmap)
                    self.gridLayout.addWidget(self.label, i, j)

                elif self.matrix[i][j] == 'L':
                    self.label = QLabel()
                    self.pixmap = QPixmap('images/loc.png')
                    self.label.setPixmap(self.pixmap)
                    self.gridLayout.addWidget(self.label, i, j)
        self.ready = True

        if self.count == len(self.location):
            self.victory()

    def victory(self):
        self.New_Form = NextLevel()
        self.New_Form.start(self.current_levelnumber)
        self.New_Form.show()
        self.close()

class Level_Choose(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Level_Choose')
        self.initUI()

    def initUI(self):
        self.game_files = [file for file in os.listdir('./Levels') if file.endswith(".txt")]
        self.setFixedSize(800, 600)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        scroll_area.setWidget(content_widget)

        vbox = QVBoxLayout(content_widget)

        for file_name in self.game_files:
            button = QPushButton(file_name)
            button.clicked.connect(lambda checked, fn=file_name: self.Level(fn))
            vbox.addWidget(button)
            vbox.setSpacing(10)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)


    def Level(self, file_name):
        file_number = self.game_files.index(file_name)
        self.New_Form = Game_Form()
        self.New_Form.start(file_number)
        self.New_Form.show()
        self.close()

class NextLevel(QWidget):
    def __init__(self):
        super().__init__()

    def start(self, level_number):
        self.setFixedSize(800, 600)
        self.level_number = level_number
        self.game_files = [file for file in os.listdir('./Levels') if file.endswith(".txt")]
        self.Title = QLabel(self)
        self.Title.setText('Уровень пройден')
        self.Title.setAlignment(QtCore.Qt.AlignHCenter)
        font = QtGui.QFont()
        font.setPointSize(62)
        self.Title.setFont(font)
        self.Title.setGeometry(0, 0, 800, 600)
        self.Menu = QPushButton(self)
        self.Menu.setText('Меню')
        self.Menu.setGeometry(QtCore.QRect(250, 225, 300, 100))
        if self.level_number + 1 == len(self.game_files):
            self.Title2 = QLabel(self)
            self.Title2.setText('Последний уровень')
        else:
            self.nextlevel = QPushButton(self)
            self.nextlevel.setText('Следующий уровень')
            self.nextlevel.setGeometry(QtCore.QRect(250, 380, 300, 100))
            self.nextlevel.clicked.connect(lambda: self.NewLevel())

        self.Menu.clicked.connect(lambda: self.ShowMenu())

    def ShowMenu(self):
        self.NewForm = Menu()
        self.NewForm.show()
        self.close()
    def NewLevel(self):
        self.NewForm = Game_Form()
        self.NewForm.start(self.level_number + 1)
        self.NewForm.show()
        self.close()

class Menu(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle('Menu')
        self.setFixedSize(800, 600)

        Title = QLabel(self)
        Title.setText('Sokoban')
        Title.setAlignment(QtCore.Qt.AlignHCenter)
        Title.setGeometry(0,0,800,600)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(96)
        Title.setFont(font)
        Title.move(0,50)

        self.Menu = QPushButton(self)
        self.Menu.setGeometry(QtCore.QRect(250, 225, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.Menu.setFont(font)
        self.Menu.setText('Выбор уровня')


        self.Exit = QPushButton(self)
        self.Exit.setGeometry(QtCore.QRect(250, 380, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.Exit.setFont(font)
        self.Exit.setText('Выход')

        self.button_clicks()

    def button_clicks(self):
        self.Exit.clicked.connect(lambda: exit())
        self.Menu.clicked.connect(self.change_form)

    def change_form(self):
        self.close()
        self.NewForm = Level_Choose()
        self.NewForm.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = Menu()
    Form.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QGridLayout, QPushButton, QMessageBox, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os



class Game_Form(QWidget):

    def __init__(self):
        super().__init__()
    def importa(self, matrix,x,y):
        self.matrix = matrix
        self.x = x
        self.y = y



    def start(self):
        self.setFixedSize(800, 600)
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        self.setWindowTitle('Game')

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

        self.But_Up.setText("↑")
        self.But_Left.setText("←")
        self.But_Right.setText("→")
        self.But_Down.setText("↓")

        self.position_box = []
        self.location = []
        self.position_player = []
        self.ready = True


        for i in range(self.y):
            for j in range(self.x):
                if self.matrix[i][j] == 'B':
                    label = QLabel()
                    pixmap = QPixmap('images/crate9.png')
                    label.setPixmap(pixmap)
                    self.position_box.append([i, j])
                    self.gridLayout.addWidget(label, i, j)

                elif self.matrix[i][j] == 'W':
                    label = QLabel()
                    pixmap = QPixmap('images/wall2.png')
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
                    pixmap = QPixmap('images/crate10.png')
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
            self.But_Up.clicked.connect(lambda: self.check_up())
            self.But_Down.clicked.connect(lambda: self.check_down())
            self.But_Right.clicked.connect(lambda: self.check_right())
            self.But_Left.clicked.connect(lambda: self.check_left())

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
                    label = QLabel()
                    pixmap = QPixmap('images/crate1.png')
                    label.setPixmap(pixmap)
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
                    self.gridLayout.addWidget(label, i, j)
        self.ready = True

        if self.count == len(self.location):
            self.victory()


    def check_up(self):
        self.ready = False
        if (self.matrix[self.position_player[0][0] - 1][self.position_player[0][1]] == '.' or
                self.matrix[self.position_player[0][0] - 1][
                    self.position_player[0][1]] == 'L'):
            self.matrix[self.position_player[0][0]][self.position_player[0][1]] = '.'
            self.position_player[0][0] = self.position_player[0][0] - 1

        elif (self.matrix[self.position_player[0][0] - 1][self.position_player[0][1]] == 'B' or
              self.matrix[self.position_player[0][0] - 1][
                  self.position_player[0][1]] == 'Q') and (
                self.matrix[self.position_player[0][0] - 2][self.position_player[0][1]] == '.' or
                self.matrix[self.position_player[0][0] - 2][
                    self.position_player[0][1]] == 'L'):
            for i in range(len(self.position_box)):
                if (self.position_player[0][0] - 1 == self.position_box[i][0]) and (
                        self.position_player[0][1] == self.position_box[i][1]):
                    self.matrix[self.position_box[i][0]][self.position_box[i][1]] = '.'
                    self.position_box[i][0] = self.position_box[i][0] - 1
        self.update()

    def check_down(self):
        self.ready = False
        if (self.matrix[self.position_player[0][0] + 1][self.position_player[0][1]] == '.' or
                self.matrix[self.position_player[0][0] + 1][
                    self.position_player[0][1]] == 'L'):
            self.matrix[self.position_player[0][0]][self.position_player[0][1]] = '.'
            self.position_player[0][0] = self.position_player[0][0] + 1

        elif (self.matrix[self.position_player[0][0] + 1][self.position_player[0][1]] == 'B' or
              self.matrix[self.position_player[0][0] + 1][
                  self.position_player[0][1]] == 'Q') and (
                self.matrix[self.position_player[0][0] + 2][self.position_player[0][1]] == '.' or
                self.matrix[self.position_player[0][0] + 2][
                    self.position_player[0][1]] == 'L'):
            for i in range(len(self.position_box)):
                if self.position_player[0][0] + 1 == self.position_box[i][0] and self.position_player[0][1] == \
                        self.position_box[i][1]:
                    self.matrix[self.position_box[i][0]][self.position_box[i][1]] = '.'
                    self.position_box[i][0] = self.position_box[i][0] + 1
        self.update()

    def check_left(self):
        self.ready = False
        if (self.matrix[self.position_player[0][0]][self.position_player[0][1] - 1] == '.' or
                self.matrix[self.position_player[0][0]][
                    self.position_player[0][1] - 1] == 'L'):
            self.matrix[self.position_player[0][0]][self.position_player[0][1]] = '.'
            self.position_player[0][1] = self.position_player[0][1] - 1

        elif (self.matrix[self.position_player[0][0]][self.position_player[0][1] - 1] == 'B' or
              self.matrix[self.position_player[0][0]][
                  self.position_player[0][1] - 1] == 'Q') and (
                self.matrix[self.position_player[0][0]][self.position_player[0][1] - 2] == '.' or
                self.matrix[self.position_player[0][0]][
                    self.position_player[0][1] - 2] == 'L'):
            for i in range(len(self.position_box)):
                if self.position_player[0][0] == self.position_box[i][0] and self.position_player[0][1] - 1 == \
                        self.position_box[i][1]:
                    self.matrix[self.position_box[i][0]][self.position_box[i][1]] = '.'
                    self.position_box[i][1] = self.position_box[i][1] - 1
        self.update()

    def check_right(self):
        self.ready = False
        if (self.matrix[self.position_player[0][0]][self.position_player[0][1] + 1] == '.' or
                self.matrix[self.position_player[0][0]][
                    self.position_player[0][1] + 1] == 'L'):
            self.matrix[self.position_player[0][0]][self.position_player[0][1]] = '.'
            self.position_player[0][1] = self.position_player[0][1] + 1

        elif (self.matrix[self.position_player[0][0]][self.position_player[0][1] + 1] == 'B' or
              self.matrix[self.position_player[0][0]][
                  self.position_player[0][1] + 1] == 'Q') and (
                self.matrix[self.position_player[0][0]][self.position_player[0][1] + 2] == '.' or
                self.matrix[self.position_player[0][0]][
                    self.position_player[0][1] + 2] == 'L'):
            for i in range(len(self.position_box)):
                if self.position_player[0][0] == self.position_box[i][0] and self.position_player[0][1] + 1 == \
                        self.position_box[i][1]:
                    self.matrix[self.position_box[i][0]][self.position_box[i][1]] = '.'
                    self.position_box[i][1] = self.position_box[i][1] + 1

        self.update()


    def victory(self):
        msg = QMessageBox()
        msg.setWindowTitle("Название окна")
        msg.setText("Описание")
        msg.setIcon(QMessageBox.Warning)
        msg.exec()
        exit()


class Level_Choose(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Level_Change')
        self.initUI()

    def initUI(self):
        self.game_files = [file for file in os.listdir('./Levels') if file.endswith(".txt")]
        print(self.game_files)
        self.setFixedSize(800, 600)
        vbox = QVBoxLayout(self)

        for file_name in self.game_files:
            button = QPushButton(file_name)
            button.clicked.connect(lambda checked, fn=file_name: self.Level(fn))
            vbox.addWidget(button)
            vbox.setSpacing(2)

    def Level(self, file_name):
        with open('./Levels/'+file_name, 'r') as file:
            matrix = []
            position_box = []
            location = []
            position_player = []
            a = ''
            while '\n' not in a:
                a += file.read(1)
            y = int(a)

            a = ''
            while '\n' not in a:
                a += file.read(1)
            x = int(a)

            for i in range(y):
                line = ''
                for j in range(x):
                    a = file.read(1)
                    line += a
                    if a == 'B':
                        position_box.append([i, j])
                    elif a == 'H':
                        position_player.append([i, j])
                    elif a == 'L':
                        location.append([i, j])
                file.read(1)
                matrix.append([*line])
            New_Form = Game_Form()
            New_Form.importa(matrix, x, y)
            New_Form.start()
            New_Form.show()
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
        font.setFamily("Pristina")
        font.setPointSize(72)
        Title.setFont(font)
        Title.move(0,50)

        self.Menu = QPushButton(self)
        self.Menu.setGeometry(QtCore.QRect(250, 225, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.Menu.setFont(font)
        self.Menu.setText('Меню')


        self.Exit = QPushButton(self)
        self.Exit.setGeometry(QtCore.QRect(250, 380, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.Exit.setFont(font)
        self.Exit.setText('Выход')

        self.button_clicks()

    def button_clicks(self):
        self.Exit.clicked.connect(lambda: exit())
        self.Menu.clicked.connect(self.change_form)

    def change_form(self):
        self.close()
        NewForm = Level_Choose()
        NewForm.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = Menu()
    Form.show()
    sys.exit(app.exec_())

import os


def start():
    q = '.'
    os.system('cls')
    print('Sokoban')
    print('1. Начать игру.')
    print('2. Выход.')
    while q != 1 or q != 2:
        print('Vvod v starte')
        q = int(input())
        if q == 1:
            menu()
        elif q == 2:
            exit()


def menu():
    os.system('cls')
    for i in range(len(files)):
        print(i + 1, '.', files[i])
    print(0, '. Назад.')
    print('Vvod v menu')
    q = int(input())
    if q == 0:
        start()
    else:
        if q-1 in range(len(files)):
            body(q-1)


def body(filecount):
    os.system('cls')

    f = open('./Levels/'+files[filecount])
    print('Запущен ',files[filecount])
    matrix = []
    position_box = []
    location = []
    position_player = []
    a = ''
    while '\n' not in a:
        a += f.read(1)
    y = int(a)

    a = ''
    while '\n' not in a:
        a += f.read(1)
    x = int(a)

    for i in range(y):
        line = ''
        for j in range(x):
            a = f.read(1)
            line += a
            if a == 'B':
                position_box.append([i, j])
            elif a == 'H':
                position_player.append([i,j])
            elif a == 'L':
                location.append([i, j])
        f.read(1)
        matrix.append([*line])
    print(len(files))

    a = ' '
    q = ''

    while a != 'END':
        count = 0
        for i in range(len(location)):
            matrix[location[i][0]][location[i][1]] = 'L'

        for i in range(len(position_box)):
            matrix[position_box[i][0]][position_box[i][1]] = 'B'

        for i in range(len(location)):
            if matrix[location[i][0]][location[i][1]] == 'B':
                count += 1
                matrix[location[i][0]][location[i][1]] = 'Q'

        matrix[position_player[0][0]][position_player[0][1]] = 'H'



        if count == len(location):
            a = 'END'
            print('Victory')
            if filecount+1 != len(files):
                print('1. Следующий уровень.')
                print('0. Меню.')
                while (q != 0) and (q != 1):
                    q = int(input())
                if q == 1:
                    body(filecount+1)
                elif q == 0:
                    menu()
            else:
                print('Последний уровень.')
                print('0. Меню.')
                while q != 0:
                    q = int(input())
                if q == 0:
                    menu()
        for i in range(len(matrix)):
            print(*matrix[i])
        print('Vvod')

        a = input()

        if (a == 'W') and (
                matrix[position_player[0][0] - 1][position_player[0][1]] == '.' or matrix[position_player[0][0] - 1][
            position_player[0][1]] == 'L'):
            matrix[position_player[0][0]][position_player[0][1]] = '.'
            position_player[0][0] = position_player[0][0] - 1
            os.system('cls')
        elif (a == 'W'
              and (matrix[position_player[0][0] - 1][position_player[0][1]] == 'B' or matrix[position_player[0][0] - 1][
                    position_player[0][1]] == 'Q')
              and (matrix[position_player[0][0] - 2][position_player[0][1]] == 'B' or matrix[position_player[0][0] - 2][
                    position_player[0][1]] == 'Q')):
            os.system('cls')
            continue
        elif (a == 'W' and (
                matrix[position_player[0][0] - 1][position_player[0][1]] == 'B' or matrix[position_player[0][0] - 1][
            position_player[0][1]] == 'Q')
              and matrix[position_player[0][0] - 2][position_player[0][1]] != 'W'):
            for i in range(len(position_box)):
                if position_player[0][0] == position_box[i][0] + 1 and position_player[0][1] == position_box[i][1]:
                    matrix[position_box[i][0]][position_box[i][1]] = '.'
                    position_box[i][0] = position_box[i][0] - 1
                    os.system('cls')
                    break
        else:
            os.system('cls')

        if (a == 'S') and (
                matrix[position_player[0][0] + 1][position_player[0][1]] == '.' or matrix[position_player[0][0] + 1][
            position_player[0][1]] == 'L'):
            matrix[position_player[0][0]][position_player[0][1]] = '.'
            position_player[0][0] = position_player[0][0] + 1
            os.system('cls')
        elif (a == 'S'
              and (matrix[position_player[0][0] + 1][position_player[0][1]] == 'B' or matrix[position_player[0][0] + 1][
                    position_player[0][1]] == 'Q')
              and (matrix[position_player[0][0] + 2][position_player[0][1]] == 'B' or matrix[position_player[0][0] + 2][
                    position_player[0][1]] == 'Q')):
            os.system('cls')
            continue
        elif (a == 'S' and (
                matrix[position_player[0][0] + 1][position_player[0][1]] == 'B' or matrix[position_player[0][0] + 1][
            position_player[0][1]] == 'Q')
              and matrix[position_player[0][0] + 2][position_player[0][1]] != 'W'):
            for i in range(len(position_box)):
                if position_player[0][0] == position_box[i][0] - 1 and position_player[0][1] == position_box[i][1]:
                    matrix[position_box[i][0]][position_box[i][1]] = '.'
                    position_box[i][0] = position_box[i][0] + 1
                    os.system('cls')
                    break
        else:
            os.system('cls')

        if (a == 'D') and (
                matrix[position_player[0][0]][position_player[0][1] + 1] == '.' or matrix[position_player[0][0]][
            position_player[0][1] + 1] == 'L'):
            matrix[position_player[0][0]][position_player[0][1]] = '.'
            position_player[0][1] = position_player[0][1] + 1
            os.system('cls')
        elif (a == 'D'
              and (matrix[position_player[0][0]][position_player[0][1] + 1] == 'B' or matrix[position_player[0][0]][
                    position_player[0][1] + 1] == 'Q')
              and (matrix[position_player[0][0]][position_player[0][1] + 2] == 'B' or matrix[position_player[0][0]][
                    position_player[0][1] + 2] == 'Q')):
            os.system('cls')
            continue
        elif (a == 'D' and (
                matrix[position_player[0][0]][position_player[0][1] + 1] == 'B' or matrix[position_player[0][0]][
            position_player[0][1] + 1] == 'Q')
              and matrix[position_player[0][0]][position_player[0][1] + 2] != 'W'):
            for i in range(len(position_box)):
                if position_player[0][0] == position_box[i][0] and position_player[0][1] == position_box[i][1] - 1:
                    matrix[position_box[i][0]][position_box[i][1]] = '.'
                    position_box[i][1] = position_box[i][1] + 1
                    os.system('cls')
                    break
        else:
            os.system('cls')

        if (a == 'A') and (
                matrix[position_player[0][0]][position_player[0][1] - 1] == '.' or matrix[position_player[0][0]][
            position_player[0][1] - 1] == 'L'):
            matrix[position_player[0][0]][position_player[0][1]] = '.'
            position_player[0][1] = position_player[0][1] - 1
            os.system('cls')
        elif (a == 'A'
              and (matrix[position_player[0][0]][position_player[0][1] - 1] == 'B' or matrix[position_player[0][0]][
                    position_player[0][1] - 1] == 'Q')
              and (matrix[position_player[0][0]][position_player[0][1] - 2] == 'B' or matrix[position_player[0][0]][
                    position_player[0][1] - 2] == 'Q')):
            os.system('cls')
            continue
        elif (a == 'A' and (
                matrix[position_player[0][0]][position_player[0][1] - 1] == 'B' or matrix[position_player[0][0]][
            position_player[0][1] - 1] == 'Q')
              and matrix[position_player[0][0]][position_player[0][1] - 2] != 'W'):
            for i in range(len(position_box)):
                if position_player[0][0] == position_box[i][0] and position_player[0][1] == position_box[i][1] + 1:
                    matrix[position_box[i][0]][position_box[i][1]] = '.'
                    position_box[i][1] = position_box[i][1] - 1
                    os.system('cls')
                    break
        else:
            os.system('cls')



        os.system('cls')

directory = './Levels'
files = os.listdir(directory)
start()
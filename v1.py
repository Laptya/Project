import os
matrix = []
stroka = []
position_box = [[4, 2], [3, 4]]
location = [[3, 2], [3, 3]]
position_player = [[1, 1]]
x = 7
y = 8

for i in range(x):
    for j in range(y):
        if (i == 0) or (i == x - 1) or (j == 0) or (j == y - 1):
            stroka.append('W')
        else:
            stroka.append('.')
    matrix.append(stroka)
    stroka = []

matrix[position_player[0][0]][position_player[0][1]] = 'H'

for i in range(len(location)):
    matrix[location[i][0]][location[i][1]] = 'L'

for i in range(len(position_box)):
    matrix[position_box[i][0]][position_box[i][1]] = 'B'

a = 1
while a != 'END' and a != 'end':
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

    for i in range(x):
        print(*matrix[i])

    if count == len(location):
        print('Victory')
        input()
        break

    a = input()

    if (a == 'W') and (matrix[position_player[0][0] - 1][position_player[0][1]] == '.' or matrix[position_player[0][0] - 1][position_player[0][1]] == 'L'):
        matrix[position_player[0][0]][position_player[0][1]] = '.'
        position_player[0][0] = position_player[0][0] - 1
        os.system('cls')
    elif (a == 'W'
          and (matrix[position_player[0][0] - 1][position_player[0][1]] == 'B' or matrix[position_player[0][0] - 1][position_player[0][1]] == 'Q')
          and (matrix[position_player[0][0] - 2][position_player[0][1]] == 'B' or matrix[position_player[0][0] - 2][position_player[0][1]] == 'Q')):
        os.system('cls')
        continue
    elif (a == 'W' and (matrix[position_player[0][0] - 1][position_player[0][1]] == 'B' or matrix[position_player[0][0] - 1][position_player[0][1]] == 'Q')
          and matrix[position_player[0][0] - 2][position_player[0][1]] != 'W'):
        for i in range(len(position_box)):
            if position_player[0][0] == position_box[i][0] + 1 and position_player[0][1] == position_box[i][1]:
                matrix[position_box[i][0]][position_box[i][1]] = '.'
                position_box[i][0] = position_box[i][0] - 1
                os.system('cls')
                break
    else:
        os.system('cls')

    if (a == 'S') and (matrix[position_player[0][0] + 1][position_player[0][1]] == '.' or matrix[position_player[0][0] + 1][position_player[0][1]] == 'L'):
        matrix[position_player[0][0]][position_player[0][1]] = '.'
        position_player[0][0] = position_player[0][0] + 1
        os.system('cls')
    elif (a == 'S'
          and (matrix[position_player[0][0] + 1][position_player[0][1]] == 'B' or matrix[position_player[0][0] + 1][position_player[0][1]] == 'Q')
          and (matrix[position_player[0][0] + 2][position_player[0][1]] == 'B' or matrix[position_player[0][0] + 2][position_player[0][1]] == 'Q')):
        os.system('cls')
        continue
    elif (a == 'S' and (matrix[position_player[0][0] + 1][position_player[0][1]] == 'B' or matrix[position_player[0][0] + 1][position_player[0][1]] == 'Q')
          and matrix[position_player[0][0] + 2][position_player[0][1]] != 'W'):
        for i in range(len(position_box)):
            if position_player[0][0] == position_box[i][0] - 1 and position_player[0][1] == position_box[i][1]:
                matrix[position_box[i][0]][position_box[i][1]] = '.'
                position_box[i][0] = position_box[i][0] + 1
                os.system('cls')
                break
    else:
        os.system('cls')

    if (a == 'D') and (matrix[position_player[0][0]][position_player[0][1] + 1] == '.' or matrix[position_player[0][0]][position_player[0][1] + 1] == 'L'):
        matrix[position_player[0][0]][position_player[0][1]] = '.'
        position_player[0][1] = position_player[0][1] + 1
        os.system('cls')
    elif (a == 'D'
          and (matrix[position_player[0][0]][position_player[0][1] + 1] == 'B' or matrix[position_player[0][0]][position_player[0][1] + 1] == 'Q')
          and (matrix[position_player[0][0]][position_player[0][1] + 2] == 'B' or matrix[position_player[0][0]][position_player[0][1] + 2] == 'Q')):
        os.system('cls')
        continue
    elif (a == 'D' and (matrix[position_player[0][0]][position_player[0][1] + 1] == 'B' or matrix[position_player[0][0]][position_player[0][1] + 1] == 'Q')
          and matrix[position_player[0][0]][position_player[0][1] + 2] != 'W'):
        for i in range(len(position_box)):
            if position_player[0][0] == position_box[i][0] and position_player[0][1] == position_box[i][1] - 1:
                matrix[position_box[i][0]][position_box[i][1]] = '.'
                position_box[i][1] = position_box[i][1] + 1
                os.system('cls')
                break
    else:
        os.system('cls')

    if (a == 'A') and (matrix[position_player[0][0]][position_player[0][1] - 1] == '.' or matrix[position_player[0][0]][position_player[0][1] - 1] == 'L'):
        matrix[position_player[0][0]][position_player[0][1]] = '.'
        position_player[0][1] = position_player[0][1] - 1
        os.system('cls')
    elif (a == 'A'
          and (matrix[position_player[0][0]][position_player[0][1] - 1] == 'B' or matrix[position_player[0][0]][position_player[0][1] - 1] == 'Q')
          and (matrix[position_player[0][0]][position_player[0][1] - 2] == 'B' or matrix[position_player[0][0]][position_player[0][1] - 2] == 'Q')):
        os.system('cls')
        continue
    elif (a == 'A' and (matrix[position_player[0][0]][position_player[0][1] - 1] == 'B' or matrix[position_player[0][0]][position_player[0][1] - 1] == 'Q')
          and matrix[position_player[0][0]][position_player[0][1] - 2] != 'W'):
        for i in range(len(position_box)):
            if position_player[0][0] == position_box[i][0] and position_player[0][1] == position_box[i][1] + 1:
                matrix[position_box[i][0]][position_box[i][1]] = '.'
                position_box[i][1] = position_box[i][1] - 1
                os.system('cls')
                break
    else:
        os.system('cls')


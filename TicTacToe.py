import random

table_list = [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ']

currentPlayer = 'X'
gameRunning = True


def table_Building(tables_list):  # การสร้างตาราง
    print(tables_list[0] + ' | ' + tables_list[1] + '| ' + tables_list[2])
    print('--------')
    print(tables_list[3] + ' | ' + tables_list[4] + '| ' + tables_list[5])
    print('--------')
    print(tables_list[6] + ' | ' + tables_list[7] + '| ' + tables_list[8])


def get_Input():  # รับค่าจากผู้เล่น และนำค่าไปใส่ในตาราง
    print('PLAYER TURN')
    player_num = int(input('Enter 1 to 9: '))
    if 1 <= player_num <= 9 and table_list[player_num - 1] == ' ':
        table_list[player_num - 1] = currentPlayer
    elif table_list[player_num - 1] != ' ':
        print(f'This Tie is O')
        print('Enter your number again')
        get_Input()


def com_Input():  # ให้คอมสุ่มเลือกพื้นที่
    bot_random = random.randint(0, 8)
    if table_list[bot_random] == ' ':
        table_list[bot_random] = currentPlayer
        print('BOT TURN')
        switchPlayer()
    else:
        com_Input()


def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'


def game_Check():
    global gameRunning

    if table_list[0] == 'X' and table_list[1] == 'X' and table_list[2] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[3] == 'X' and table_list[4] == 'X' and table_list[5] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[6] == 'X' and table_list[7] == 'X' and table_list[8] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[0] == 'X' and table_list[3] == 'X' and table_list[6] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[1] == 'X' and table_list[4] == 'X' and table_list[7] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[2] == 'X' and table_list[5] == 'X' and table_list[8] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[6] == 'X' and table_list[7] == 'X' and table_list[8] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[0] == 'X' and table_list[4] == 'X' and table_list[8] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[2] == 'X' and table_list[4] == 'X' and table_list[6] == 'X':
        print('WINNER IS PLAYER!!!!')
        return False
    elif table_list[0] == 'O' and table_list[1] == 'O' and table_list[2] == 'O':
        print('WINNER IS BOT!!!!')
        return False
    elif table_list[3] == 'O' and table_list[4] == 'O' and table_list[5] == 'O':
        print('WINNER IS BOT!!!!')
        return False
    elif table_list[6] == 'O' and table_list[7] == 'O' and table_list[8] == 'O':
        print('WINNER IS BOT!!!!')
        return False
    elif table_list[0] == 'O' and table_list[3] == 'O' and table_list[6] == 'O':
        print('WINNER IS BOT!!!!')
        return False
    elif table_list[1] == 'O' and table_list[4] == 'O' and table_list[7] == 'O':
        print('WINNER IS BOT!!!!')
        return False
    elif table_list[2] == 'O' and table_list[5] == 'O' and table_list[8] == 'O':
        print('WINNER IS BOT!!!!')
        return False
    elif table_list[0] == 'O' and table_list[4] == 'O' and table_list[8] == 'O':
        print('WINNER IS BOT!!!!')
        return False
    elif table_list[2] == 'O' and table_list[4] == 'O' and table_list[6] == 'O':
        print('WINNER IS BOT!!!!')
        return False


def checkTie():
    global gameRunning
    if ' ' not in table_list:
        table_Building(table_list)
        print('Not have a tie!!!')
        return False


while gameRunning:
    get_Input()
    table_Building(table_list)
    if game_Check() == False:
        break
    if checkTie() == False:
        break
    switchPlayer()
    com_Input()
    table_Building(table_list)
    if game_Check() == False:
        break
    if checkTie() == False:
        break

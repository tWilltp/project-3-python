# Legend
# X for placing ship and hit ship
# ' ' for available space
# '-' for missed shot


from random import randint

game_board = [[' '] * 9 for x in range(10)]
enemy_ships = []
player_ships = []
enemy_strikes = []
player_strikes = []
row = int in range(9)
column = str in range(20)

convert_let_to_num = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
}

convert_num_to_num = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    '0': 9,
}


def run_game():
    
    print('INSTRUCTIONS: write instructions')
    input('Play Game? press enter: ')
    generate_player_ships(game_board)
    generate_enemy_ships(game_board)
    display_board(game_board)
    attack_coordinates()
    #  check_player_strikes(row, column)


def display_board(game_board):
    print('Your board')
    print('  A B C D E F G H I J')
    row_number = 1
    for row in game_board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def generate_player_ships(game_board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 9), randint(0, 99)
        while game_board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 9), randint(0, 9)
        game_board[ship_row][ship_column] = 'X'


def generate_enemy_ships(game_board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 9), randint(0, 9)
        while game_board[ship_row][ship_column] == '0':
            ship_row, ship_column = randint(0, ), randint(0, 9)
        game_board[ship_row][ship_column] = ' '


def attack_coordinates():
    row = input('Please enter a ship row 1 - 0: ')
    while row not in '123456789':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1 - 0: ')
    column = input('Please enter a ship column A - J: ').upper()
    while column not in 'ABCDEFGHIJKLMNOPQRST':
        print('Please enter a valid column')
        column = input('Please enter a ship column A - J: ').upper()
    return int(row), convert_let_to_num[column]


def shots_fired(game_board):
    turns = 25
    while turns <= 25:
        if game_board[row][column] == '-':
            print('Area Clear')
        elif game_board[row][column] == 'X':
            print('Target Hit!')
            game_board[row][column] = 'X'
            turns -= 1
        else:
            print('Shot missed')
            game_board[row][column] = '-'
            turns -= 1
        if count_ships_hit() == 5:
            print('Enemy defeated, Well done!')
            break
        print('You have ' + str(turns) + ' shots left')
        if turns == 0:
            print("Battle Lost! we'll get 'em next time")
            break


def count_ships_hit():
    count = 0
    for row in game_board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def hit_miss():
    pass


def count_shots():
    pass


def end_of_game():
    pass


run_game()
# count_ships_hit()
# shots_fired(game_board)

# def player_info():
# pass
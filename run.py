# Legend
# X for placing ship and hit ship
# ' ' for available space
# '-' for missed shot


from random import randint

game_board = [[' '] * 9 for x in range(9)]
enemy_ships = []
player_ships = []
enemy_strikes = []
player_strikes = []
row = int in range(8)
column = str in range(8)

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
}


def run_game():
    
    print('INSTRUCTIONS: write instructions')
    input('Play Game? press enter: ')
    generate_player_ships(game_board)
    generate_enemy_ships(game_board)
    display_board(game_board)
    attack_coordinates()
    shots_fired(game_board)
    count_ships_hit()
    #  check_player_strikes(row, column)


def display_board(game_board):
    print('Your board')
    print('  A B C D E F G H I')
    row_number = 1
    for row in game_board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def generate_player_ships(game_board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while game_board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        game_board[ship_row][ship_column] = 'X'


def generate_enemy_ships(game_board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while game_board[ship_row][ship_column] == '0':
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        game_board[ship_row][ship_column] = '0'


def attack_coordinates():

    # Enter the row number between 1 to 8

    row = input('Please enter a ship row 1 - 9: ')
    while row not in '123456789':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1 - 9: ')

    # Enter the Ship column from A TO H

    column = input('Please enter a ship column A - I: ').upper()
    while column not in 'ABCDEFGHIJKLMNOPQRST':
        print('Please enter a valid column')
        column = input('Please enter a ship column A - I: ').upper()
    return int(row)-1, convert_let_to_num[column]


def shots_fired(game_board):
    turns = 25
    while turns > 0:
        display_board(game_board)
        row, column = attack_coordinates()
        if game_board[row][column] == '-':
            print('Area clear, guess again')
        elif game_board[row][column] == 'X':
            print('Friendly fire, guess again')
        elif game_board[row][column] == '0':
            print('Target Hit!')
            game_board[row][column] = 'S'
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
            if column == '0':
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
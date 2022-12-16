# Legend
# X for placing ship and hit ship
# ' ' for available space
# '-' for missed shot


from random import randint

game_board = [[' '] * 20 for x in range(9)]
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
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
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
    generate_enemy_ships(game_board)
    display_board(game_board)
    attack_coordinates()
    check_player_strikes(row, column)


def display_board(game_board):
    print('Your board')
    print('  A B C D E F G H I J K L M N O P Q R S T')
    row_number = 1
    for row in game_board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def player_ships():
    pass  # choose where to place ships


def generate_enemy_ships(enemy_board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while enemy_board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        enemy_board[ship_row][ship_column] = 'X'


def attack_coordinates():
    row = input('Please enter a ship row 1 - 8: ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1 - 8: ')
    column = input('Please enter a ship column A - H: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A - H: ').upper()
    return int(row), convert_let_to_num[column]


def count_ships_hit():
    count = 0
    for row in game_board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def enemy_strategy(game_board):
    turns = 32
    while turns > 0:
        if game_board[row][column] == '-':
            print('Area Clear')
        elif enemy_board[row][column] == 'X':
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


def hit_miss():
    pass


def count_shots():
    pass


def end_of_game():
    pass


display_board(game_board)
generate_enemy_ships(game_board)
attack_coordinates()
count_ships_hit()
enemy_strategy(game_board)

# def see_instructions():
# pass
# def player_info():
# pass
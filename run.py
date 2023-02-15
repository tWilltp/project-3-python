# Legend
# '-' for missed shot
# ' ' for available space
# 'X' for player ship
# '0' for enemy ship
# 'S' for sunken enemy ship
# 'L' for sunken player ship

from random import randint

# Game variables

game_board = [[' '] * 9 for x in range(9)]
row = int in range(8)
column = str in range(8)
turns = 20
took = 0

# Row and Column conversions

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

# Function that orders the structure of the game


def run_game():
    
    # clear_board(game_board)
    print('Positive welcome message')
    print('INSTRUCTIONS: write instructions')
    input('Play Game? press enter: ')
    generate_player_ships(game_board)
    generate_enemy_ships(game_board)
    shots_fired(game_board)
    attack_coordinates()
    count_ships_hit()
    count_comp_ships_hit()

# Function that clears the previously played board


# def clear_board(game_board):

#     if game_board[row][column] == '-':
#         game_board[row][column] = ' '

#     if game_board[row][column] == 'X':
#         game_board[row][column] = ' '
    
#     if game_board[row][column] == 'L':
#         game_board[row][column] = ' '

#     if game_board[row][column] == 'S':
#         game_board[row][column] = ' '

#     if game_board[row][column] == '0':
#         game_board[row][column] = ' '

# Function that displays the board


def display_board(game_board):

    print('Your board')
    print('  A B C D E F G H I')
    row_number = 1
    for row in game_board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

# Function that places the player's ships randomly


def generate_player_ships(game_board):

    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while game_board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        game_board[ship_row][ship_column] = 'X'

# Function that places the enemy ships randomly


def generate_enemy_ships(game_board):

    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while game_board[ship_row][ship_column] == '0':
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        game_board[ship_row][ship_column] = '0'

# Function that allows the player to target an area


def attack_coordinates():

    # Enter the row number between 1 to 9

    row = input('Please enter a ship row 1 - 9: ')
    while row not in '123456789':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1 - 9: ')

    # Enter the Ship column from A TO I

    column = input('Please enter a ship column A - I: ').upper()
    while column not in 'ABCDEFGHI':
        print('Please enter a valid column')
        column = input('Please enter a ship column A - I: ').upper()
    return int(row)-1, convert_let_to_num[column]

# Function that selects the computers targets randomly


def computer_shot(game_board):

    row, column = randint(0, 8), randint(0, 8)

    # makes sure the computer does not target its own ships

    if game_board[row][column] == '0':
        computer_shot(game_board)

    # makes sure the computer cannot hit the same ship twice

    elif game_board[row][column] == 'L':
        computer_shot(game_board)

    # makes sure the computer can't hit the same area twice

    elif game_board[row][column] == '-':
        computer_shot(game_board)

    # marks the players ships that are hit by the computer

    elif game_board[row][column] == 'X':
        print('You lost a ship')
        game_board[row][column] = 'L'

    # registers a missed shot by the computer

    elif game_board[row][column] == ' ':
        print('computer missed')
        game_board[row][column] = '-'

    # ends game if computer hits all targets

    elif count_comp_ships_hit() == 0:
        print("Battle Lost! we'll get 'em next time")
        end_game_d()

    # sets up the players next turn

    print('You have ' + str(count_comp_ships_hit()) + ' ships left')
    shots_fired(game_board)

# Function that verifies all possible outcomes by the players input


def shots_fired(game_board):

    global turns, took

    display_board(game_board)
    row, column = attack_coordinates()

    # makes sure the player cannot input the same area twice

    if game_board[row][column] == '-':
        print('Area clear, guess again')
        shots_fired(game_board)

    # makes sure the player cannot hit their own ships

    elif game_board[row][column] == 'X':
        print('Friendly fire, guess again')
        shots_fired(game_board)

    # makes sure the player cannot hit an already sunken ship

    elif game_board[row][column] == 'S':
        print('Area clear, guess again')
        shots_fired(game_board)

    # verifies a succesful hit and marks the sunken ship as 'S'

    elif game_board[row][column] == '0':
        print('Target Hit!')
        game_board[row][column] = 'S'
        turns -= 1
        took += 1
        print('You have ' + str(turns) + ' shots left')

    # marks a missed shot by '-'

    else:
        print('Shot missed')
        game_board[row][column] = '-'
        turns -= 1
        took += 1
        print('You have ' + str(turns) + ' shots left')

    # ends the game if the player runs out of shots

    if turns == 0:
        print("Battle Lost! we'll get 'em next time")
        end_game_tl()

    # ends game if the player sinks all enemy ships

    elif count_ships_hit() == 5:
        print('Enemy defeated, Well done!')
        end_game_w()

    # allows the computer to take its turn after the player

    computer_shot(game_board)

# Function that counts the sunken enemy ships so that 5 sunk ends the game


def count_ships_hit():
    count = 0
    for row in game_board:
        for column in row:
            if column == 'S':
                count += 1
    return count

# Function that counts the sunken player ships so that 5 sunk ends the game


def count_comp_ships_hit():
    count = 5
    for row in game_board:
        for column in row:
            if column == 'L':
                count -= 1
    return count

# Function that ends the game if the player wins


def end_game_w():

    print('You took ' + str(took) + ' shots to sink all ships, play again?')
    run_game()

# Function that ends the game if the player loses all turns


def end_game_tl():

    print('You had ' + str(turns) + ' shots left, play again?')
    run_game()

# Function that ends the game if the player is defeated


def end_game_d():

    print('All your ships were sunk, play again?')
    run_game()

# Function that starts the game


run_game()

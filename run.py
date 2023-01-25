# Legend
# '-' for missed shot
# ' ' for available space
# 'X' for player ship
# 'S' for sunken enemy ship
# 'L' for sunken player ship

from random import randint

# Game variables

game_board = [[' '] * 9 for x in range(9)]
row = int in range(8)
column = str in range(8)

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
    
    print('INSTRUCTIONS: write instructions')
    input('Play Game? press enter: ')
    generate_player_ships(game_board)
    generate_enemy_ships(game_board)
    display_board(game_board)
    attack_coordinates()
    shots_fired(game_board)
    count_ships_hit()

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
        end_game()

    # sets up the players next turn

    print('You have ' + str(count_comp_ships_hit()) + ' ships left')
    shots_fired(game_board)

# Function that verifies all possible outcomes by the players input


def shots_fired(game_board):

    turns = 25
    while turns > 0:

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
            print('You have ' + str(turns) + ' shots left')

        # marks a missed shot by '-'

        else:
            print('Shot missed')
            game_board[row][column] = '-'
            turns -= 1
            print('You have ' + str(turns) + ' shots left')

        # ends game if the player sinks all enemy ships

        if count_ships_hit() == 5:
            print('Enemy defeated, Well done!')
            end_game()

        # ends the game if the player runs out of shots

        elif turns == 0:
            print("Battle Lost! we'll get 'em next time")
            break

        # allows the computer to take its turn after the player

        print(turns)
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

# Function that ends the game


def end_game():

    print('You took ' + str(Turns) + ' shots to sink all ships, play again?')
    run_game()

# Function that starts the game


run_game()

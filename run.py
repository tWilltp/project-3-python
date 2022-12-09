#Legend
# X for placing ship and hit ship
# ' ' for available space
# '-' for missed shot


from random import randint


ENEMY_BOARD = [[' '] * 8 for x in range(8)]
PLAYER_BOARD = [[' '] * 8 for x in range(8)]

coordinate_conversions_letters = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

coordinate_conversions_numbers = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7
}


def display_board(board):
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def generate_enemy_ships():
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row] 


def attack_coordinates():
    pass


# def see_instructions():
    # pass
# def player_info():
    # pass


def player_ships():
    pass


def enemy_strategy():
    pass


def hit_miss():
    pass


def count_ships_hits():
    pass


def count_shots():
    pass


def end_of_game():
    pass


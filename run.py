# Legend
# X for placing ship and hit ship
# ' ' for available space
# '-' for missed shot


from random import randint


enemy_board = [[' '] * 8 for x in range(8)]
player_board = [[' '] * 8 for x in range(8)]

convert_let_to_num = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

convert_num_to_num = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7
}


def display_board(player_board, enemy_board):
    print('Your board')
    print('  A B C D E F G H')
    row_number = 1
    for row in player_board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print('Enemy board')
    print('  A B C D E F G H')
    row_number = 1
    for row in player_board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def player_ships():
    pass


def generate_enemy_ships(enemy_board):
    for ship in range(5):
        row, column = randint(0, 7), randint(0, 7)
        while enemy_board[row][column] == 'X':
            row, column = randint(0, 7), randint(0, 7)
        enemy_board[row][column] = 'X'


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
    for row in player_board, enemy_board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def enemy_strategy(player_board, enemy_board):
    turns = 32
    while turns > 0:
        display_board(player_board)
        if player_board[row][column] == '-':
            print('Area Clear')
        elif enemy_board[row][column] == 'X':
            print('Target Hit!')
            player_board[row][column] = 'X'
            turns -= 1
        else:
            print('Shot missed')
            player_board[row][column] = '-'
            turns -= 1
        if count_ships_hit() == 5:
            print('Enemy defeated, Well done!')
            break
        print('You have ' + str(turns) + 'shots left')
        if turns == 0:
            print("Battle Lost! we'll get 'em next time")
            break


def hit_miss():
    pass


def count_shots():
    pass


def end_of_game():
    pass


display_board(player_board)
generate_enemy_ships(enemy_board)
attack_coordinates()
count_ships_hit()
enemy_strategy(player_board, enemy_board)
print(enemy_board)
print(player_board)

# def see_instructions():
# pass
# def player_info():
# pass
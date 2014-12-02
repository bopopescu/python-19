#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Place In Exam for 206
# August 28, 2014
# hw1.kester.py
# Playing battleship
#---------------------------------------------------------

from random import randint
import sys

grid_size = 5

#initialize board for game play
board = []
for i in range(grid_size):
    board.append(["O"] * 5)

#initialize ships for game play
ship_two = [] # 3x1
for i in range(grid_size):
    ship_two.append(["O"] * 5)

#function to print "pretty" the game board
def print_board(board):
    for row in board:
        print " ".join(row)

#functions to set random point placement for battleship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#functions to set placement of 2x1 battleship
def ship_one_second_row(ship_row):
    chance = randint(0, 1)
    if ship_row == 0:
        return ship_row + 1
    elif ship_row == len(board) - 1:
        return ship_row - 1
    elif chance == 0:
        return ship_row + 1
    else:
        return ship_row - 1

def ship_one_second_col(ship_col):
    chance = randint(0, 1)
    if ship_col == 0:
        return ship_col + 1
    elif ship_col == len(board) - 1:
        return ship_col - 1
    elif chance == 0:
        return ship_col + 1
    else:
        return ship_col - 1

#functions to set placement of 3x1 battleship
def ship_two_second_row(ship_row):
    chance = randint(0, 1)
    if ship_row == 0 or ship_row == 1:
        return ship_row + 1
    elif ship_row == len(board) - 1 or ship_row == len(board) - 2:
        return ship_row - 1
    elif chance == 0:
        return ship_row + 1
    else:
        return ship_row - 1

def ship_two_second_col(ship_col):
    chance = randint(0, 1)
    if ship_col == 0 or ship_col == 1:
        return ship_col + 1
    elif ship_col == len(board) - 1 or ship_col == len(board) - 2:
        return ship_col - 1
    elif chance == 0:
        return ship_col + 1
    else:
        return ship_col - 1

def third_row(ship_row, ship_row2):
    if ship_row < ship_row2:
        return ship_row + 2
    elif ship_row > ship_row2:
        return ship_row - 2

def third_col(ship_col, ship_col2):
    if ship_col < ship_col2:
        return ship_col + 2
    elif ship_col > ship_col2:
        return ship_col - 2

#create variables for placement of ship two
ship_two_row = random_row(board)
ship_two_col = random_col(board)
ship_two_row2 = ship_two_second_row(ship_two_row)
ship_two_col2 = ship_two_second_col(ship_two_col)
ship_two_row3 = third_row(ship_two_row, ship_two_row2)
ship_two_col3 = third_col(ship_two_col, ship_two_col2)

#select 50/50 prob of verticle or horizontal placement of ship two
chance = randint(0, 1)
if chance == 0: #vertical shift
    s1r1 = ship_two_row
    s1r2 = ship_two_row2
    s1r3 = ship_two_row3
    s1c1 = ship_two_col
    s1c2 = ship_two_col
    s1c3 = ship_two_col
    ship_two[ship_two_row][ship_two_col] = "X"
    ship_two[ship_two_row2][ship_two_col] = "X"
    ship_two[ship_two_row3][ship_two_col] = "X"
else: #horizontal shift
    s1r1 = ship_two_row
    s1r2 = ship_two_row
    s1r3 = ship_two_row
    s1c1 = ship_two_col
    s1c2 = ship_two_col2
    s1c3 = ship_two_col3
    ship_two[ship_two_row][ship_two_col] = "X"
    ship_two[ship_two_row][ship_two_col2] = "X"
    ship_two[ship_two_row][ship_two_col3] = "X"

#create variables for placement of ship one
while True:
    ship_one_row = random_row(board)
    ship_one_col = random_col(board)
    if (ship_one_row != s1r1 and ship_one_col != s1c1) and (ship_one_row != s1r2 and ship_one_col != s1c2) and (ship_one_row != s1r3 and ship_one_col != s1c3):
        break

ship_one_row2 = ship_one_second_row(ship_one_row)
ship_one_col2 = ship_one_second_col(ship_one_col)

#select 50/50 prob of verticle or horizontal placement of ship one
chance = randint(0, 1)
if chance == 0: #vertical shift
    s2r1 = ship_one_row
    s2r2 = ship_one_row2
    s2c1 = ship_one_col
    s2c2 = ship_one_col
    ship_two[ship_one_row][ship_one_col] = "X"
    ship_two[ship_one_row2][ship_one_col] = "X"
else: #horizontal shift
    s2r1 = ship_one_row
    s2r2 = ship_one_row
    s2c1 = ship_one_col
    s2c2 = ship_one_col2
    ship_two[ship_one_row][ship_one_col] = "X"
    ship_two[ship_one_row2][ship_one_col] = "X"

###########           MAIN               ###########

print "Let's play Battleship!"
print_board(board)

turn = 0
num_turns = 3
#infinite game loop
var = 1
while var == 1:
    #request numerical guess from user
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if (guess_row == s1r1 and guess_col == s1c1) or (guess_row == s1r2 and guess_col == s1c2) or (guess_row == s1r3 and guess_col == s1c3) or (guess_row == s2r1 and guess_col == s2c1) or (guess_row == s2r2 and guess_col == s2c2):
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if guess_row == 17 and guess_col == 17:
            print_board(ship_two)
            print "YOU CHEAT!!!!!!!!"
            turn -= 1
        elif (guess_row != 17 and (guess_row < 0 or guess_row > 4)) or (guess_col != 17 and (guess_col < 0 or guess_col > 4)):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == num_turns:
            print "Game Over"
            break
        
        turn += 1
        print turn
        print_board(board)

#base code attributed to codecademy | battleship


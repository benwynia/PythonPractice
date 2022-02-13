# Ben Wynia
# ASCII Tic-Tac-Toe 3
# COMPSCIX444.4__009
# 8/8/2021


# Tic-Tac-Toe is a two-player game played on a three by three grid.
# You can draw this grid on the computer screen using the "|" ASCII character and spaces.

# Your program should:
# Draw an empty board to the screen and prompt Player X to fill in one of the squares with an X
# (your prompt should include instructions on how they indicate which square they want to fill)
# Continue to prompt each players in turn to fill in an empty square with X or O
# After each players takes his or her turn the program should display the current state of the board e.g.


def print_move_instructions():
    print("You must enter an integer that corresponds to the location on the board you want to play")
    print("The integers below show the index of each move:")
    print('|' + '1' + '|' + '2' + '|' + '3' + '|')
    print('|' + '4' + '|' + '5' + '|' + '6' + '|')
    print('|' + '7' + '|' + '8' + '|' + '9' + '|')

# create a function to print the board
def board_printer(board):
    print('|' + board['1'] + '|' + board['2'] + '|' + board['3'] + '|')
    print('|' + board['4'] + '|' + board['5'] + '|' + board['6'] + '|')
    print('|' + board['7'] + '|' + board['8'] + '|' + board['9'] + '|')

# create a function to check for a winner
def check_for_winner(board, player):
    # Top Horizontal
    if (board['1'] == board['2'] == board['3'] != ' '):
        winner = True

    # Middle Horizontal
    elif (board['4'] == board['5'] == board['6'] != ' '):
        winner = True

    # Bottom Horizontal
    elif (board['7'] == board['8'] == board['9'] != ' '):
        winner = True

    # Left Vertical
    elif (board['1'] == board['4'] == board['7'] != ' '):
        winner = True

    # Middle Vertical
    elif (board['2'] == board['5'] == board['8'] != ' '):
        winner = True

    # Right Vertical
    elif (board['3'] == board['6'] == board['9'] != ' '):
        winner = True

    # Diagonal
    elif (board['3'] == board['5'] == board['7'] != ' '):
        winner = True

    # Diagonal
    elif (board['1'] == board['5'] == board['9'] != ' '):
        winner = True
    else:
        winner = False

    if winner == True:
        print("Game Over")
        print("Player %s is the winner." % player)
    return(winner)

# create a function to request and validate a user move
def get_move(board, player):
    #print the board
    board_printer(board)

    #request and validate move
    while True:
        try:
            print('Player %s, its your turn. Where would you like to play?' % player)
            move = input()
            # Check if input is an integer
            try:
                integer= int(move)
            except:
                print("You did not enter an integer.")
                print_move_instructions()
                raise ValueError

            # Check if input is an integer in the correct range
            if integer not in range(1,10,1):
                print("This is not an integer between 1 and 9.")
                print_move_instructions()
                raise ValueError

            # Check if move spot is open on board
            if board[move] != ' ':
                print("This spot is already taken. Please choose another move.")
                print_move_instructions()
                raise ValueError
        except ValueError:
            continue
        else:
            board[move] = player
            break

# Create a Game Instance
def tictactoe_game():
    # Initialize the board as a dictionary with values
    board1 = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

    # Initialize variables
    player_X = "X"
    player_O = "O"
    move_counter = 0
    winner=False

    # Game sequence
    while move_counter < 9 and winner==False:

        # Identify who's turn it is:
        if (move_counter % 2) == 0:
            player= player_X
        else:
            player= player_O

        # Request a move from the player
        get_move(board1, player)
        move_counter += 1

        # Check for a winner
        if move_counter > 4:
            winner = check_for_winner(board1, player)
            if winner == True:
                board_printer(board1)
                break

        # Check for a draw condition-- no winner after 9 moves
        if move_counter == 9 and winner==False:
            board_printer(board1)
            print("The game is over and ended in a draw.")

# Play Again Function
def play_again():
    while True:
        try:
            print("Would you like to play again? (Yes/No)")
            new_game = input()
            if new_game.lower() == "no":
                play = False
                break
            elif new_game.lower() == "yes":
                play = True
                break
            else:
                raise ValueError
        except ValueError:
            print("I'm sorry, I didn't understand that input.")
    return(play)

# Main Game Menu
# Begin game
play = True
print('Welcome to Tic Tac Toe')
print('The rules of Tic-Tac-Toe are as follows:')
print('Players take turns filling in empty squares in the three by three grid with either an "X" or an "O".')
print('Player X always takes the first turn and fills in squares with an "X".')
print('The second player, Player O, fills in squares with an "O".')
print('The players continue to take turns until:')
print('There are three Xs in a row either horizontally, vertically, or diagonally in which case the player X wins')
print('There are three Os in a row either horizontally, vertically, or diagonally in which case the player O wins')
print('All nine squares are filled with Xs and Os but neither player has three in a row in which case the game is a draw.')
print_move_instructions()

while play == True:
    print("New Game")
    tictactoe_game()
    play = play_again()
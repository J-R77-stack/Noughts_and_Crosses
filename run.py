#---------- Global Variables ------------

# Variable containing a list to hold the board game data.
board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-",]

# Variable to let the user know if the game is finished
# set to True, will be False and break out of loop when game is over.
game_still_running = True         

# Variable to inform the user who the winner is. stays none when there is a draw
# and changes to X or O when there is a winner
winner = None

# Variable to inform the users who the current player is. Starts with player X
current_player = "X"

def show_board():
    """
    Function to print the game board to the screen on every round
    """
    print("\n")
    print("Welcome to Noughts and Crosses")
    print("\n")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("\n")

def play_the_game():
    """
    Function to play a game of Noughts and crosses.
    """

    show_board() 

    while game_still_running:
        """
        While loop to loop through which players turn it is, 
        to see if the game is over and if X or O is the winner
        or there is a tie and print the info to the console 
        and to change the player on each round.
        """
        game_turn(current_player) 

        see_if_game_is_over()

        change_player()  

    if winner == "X" or winner == "O":
        print(winner + "is the winner")
    elif winner == None:
        print("Its a draw")        

def game_turn(player):
    """
    Function to deal with the turn of each player. 
    They can enter a number to choose a position on the board.
    """ 
    number = input("Please choose a number from 1 - 9: ")
    
    """
    This will get the correct position in the borad list. 
    As board is a string convert to integer. position is 1 - 9  
    but elements in board Array are 0 - 8
    so position 1 = 0 so need to subtract 1 from number.
    """
    number = int(number) - 1

    board[number] = "X"
    show_board()

def see_if_game_is_over(): 
    """
    Fuction to see if game can end through win or draw.
    """
    see_if_winner()
    see_if_draw()  

def see_if_winner(): 
    """
    Fuction to check to see if there is a winner.
    """ 
    global winner
    row_winner = check_rows()

    diagonal_winner = check_diagonals()

    column_winner = check_columns()

    if row_winner:
        winner = row_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    elif column_winner:
        winner = column_winner()
    else:
        winner = None            
    return

def check_rows():
    """
    Function with if else statement to check the rows for a win seeing if 
    all rows have the same value and are not empty. 
    If any rows do match it will flag the while loop 
    that the game is over and return the winner X or O
    or return None/False if there is no winner and jumps out of loop.
    """
    global game_still_running

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_running = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None   

        

def check_diagonals():
    """
    Function to check the diagonals for a win seeing if 
    all diagonals have the same value and are not empty. 
    If any diagonals do match it will flag the while loop 
    that the game is over and return the winner X or O
    or return None/False if there is no winner and jumps out of loop.
    """
    global game_still_running

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_running = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None 

def check_columns():
    """
    Function to check the columns for a win seeing if 
    all columns have the same value and are not empty. 
    If any columns do match it will flag the while loop
     that the game is over and return the winner X or O
    or return None/False if there is no winner and jumps out of loop.
    """
    global game_still_running

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_running = False
    if column1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None  
                

def see_if_draw():
    """
    Function to see if there is a draw. 
    """
    return   

def change_player():
    """
    Fuction to change the player from X to O and inform the user whose turn it is.
    """
    return           

play_the_game()    
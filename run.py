# Variable containing a list to hold the board game data.
board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-",]

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

    show_board() 

    while game_still_running:
        """
        While loop to loop through which players turn it is 
        and to then see if the game is over and change the player.
        """
        game_turn(current_player) 

        see_if_game_is_over()

        change_player()  

def game_turn():
    """
    Function to deal with the turn of each player. 
    The can enter a number to choose a position on the board.
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
    return

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
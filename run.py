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

    game_turn()   

def game_turn():
    """
    Function to deal with the turn of each player. 
    The can enter a number to choose a position on the board.
    """ 
    number = input("Please choose a number from 1 - 9: ")
    
    # This will get the correct position in the borad list
    number = int(number) - 1

    board[number] = "X"
    show_board()
       

play_the_game()    
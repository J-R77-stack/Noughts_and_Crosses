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

show_board()    
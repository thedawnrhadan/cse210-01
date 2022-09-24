def main():

    board = create_board()
    current_player = 'x'


    while not (a_win(board) or a_draw(board)):
        show_board(board)
        player_input(current_player, board)
        current_player = switch_player(current_player)
        

    
    show_board(board)
    print("That's a game!")



def create_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def show_board(board):
    print(board[0], "|",board[1], "|", board[2])
    print("--+--+---")
    print(board[3], "|",board[4], "|", board[5])
    print("--+--+---")
    print(board[6], "|",board[7], "|", board[8])

def player_input(player, board):
    decision = int(input(f"{player}'s turn to choose a square 1-9:"))
    if (decision >= 1 and decision <= 9) and (board[decision - 1] != ('x' or 'o')):
        board[decision - 1] = player
    else:
        print('That does not work! Try again')


def a_win(board):
    return (board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6])

def switch_player(current_player):
    if current_player == 'x':
        current_player = 'o'
    else:
        current_player = 'x'
    return current_player

def a_draw(board):
    
    for tile in range(9):
        if board[tile] != "x" and board[tile] != "o":
            return False
    return True 





if __name__ == "__main__":
    main()
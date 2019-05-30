#Claudia Cota 60341850

import project4_logic
from project4_classes import *

def run_game():
    '''runs the console game of othello, for testing game logic'''

    print("FULL")
    row_num = int(input())
    column_num = int(input())
    first_player = input()
    top_left_color = input()
    most_or_least_wins = input()
    board = project4_logic.middle_four((project4_logic.create_board(row_num, column_num)), top_left_color, row_num, column_num)
    gamestate = Gamestate(board, first_player, most_or_least_wins, row_num, column_num)
    gamestate.all_available_places()

    game_running = True
    while game_running:
        try:
            gamestate.count_disc()
            black = gamestate.return_black_num()
            white = gamestate.return_white_num()
            print('B: {}  W: {}'.format(black, white))
            project4_logic.print_board(gamestate.board())
            print('TURN: {}'.format(gamestate.whose_turn()))         

            run = True
            while run:
                try:
                    moves = gamestate.valid_moves()
                    players_move = input().split()
                    player_move = ((int(players_move[0]), int(players_move[1])))
                    if player_move in moves:
                        print("VALID")
                        flip = gamestate.change_board(int(players_move[0]), int(players_move[1]), str(gamestate.whose_turn()))
                        gamestate.flip_places(flip)
                        gamestate.change_turn()
                        run = False
                    
                    else:
                        print("INVALID")
                        continue         
                except:
                    print("INVALID")
                    continue
                
            gamestate.valid_moves()
            if gamestate.any_moves() == False:
                gamestate.change_turn()
                gamestate.valid_moves()
                if gamestate.any_moves() == False:
                    game_running = False           

        except:
            raise InvalidMoveError()
            
    gamestate.count_disc()
    black = gamestate.return_black_num()
    white = gamestate.return_white_num()
    print('B: {}  W: {}'.format(black, white))
    project4_logic.print_board(gamestate.board()) 
    print('WINNER: {}'.format(gamestate.winner()))


if __name__ == '__main__':
    run_game()

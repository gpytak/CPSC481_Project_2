# Gregory Pytak and Nolan Winter
# CPSC 481 Project 2

from games import *

class GameOfNim(Game):

    def __init__(self, board):
        self.board = board
        moves = [(x, y) for x in range(0, len(board))
                 for y in range(1, board[x] + 1)]
        self.initial = GameState(to_move='Player', utility=0, board=board, moves=moves)
    
    def result(self, state, move):
        if move not in state.moves:
            return state
        board = state.board.copy()
        board[move[0]] = board[move[0]] - move[1]
        moves = [(x, y) for x in range(0, len(board))
                 for y in range(1, board[x] + 1)]
        return GameState(to_move=(alpha_beta_player if state.to_move == query_player else query_player),
                         utility=0, board=board, moves=moves)

    def actions(self, state):
        return state.moves

    def terminal_test(self, state):
        return state.utility != 0 or len(state.moves) == 0

    def utility(self, state, player):
        return state.utility if player == alpha_beta_player else -state.utility

    def to_move(self, state):
        return state.to_move

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    # print(nim.initial.board) # must be [0, 5, 3, 1]
    # print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    # print(nim.result(nim.initial, (1,3)))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
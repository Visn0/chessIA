from pieces import *

##########################
# MOVES
##########################
knightMove = [
    [[-2, -1], [-2, 1]],
    [[-1, -2], [-1, 2]],
    [[1, -2], [1, 2]],
    [[2, -1], [2, 1]]
]
bishopMove = [
    [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]], #leftop
    [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [6, 6], [7, 7]], #righttop
    [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]], #leftbot
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]] #rightbot
]
rookMove = [
    [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]], #left
    [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]], #top
    [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]], #right
    [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]], #bot
]
queenMove = bishopMove + rookMove #bishop + rook
kingMove = [[-1, 0], [0, -1], [0, 1], [1, 0]] #top, left, right, bot

##########################
# PIECES
##########################

#BLACK
bPawn = Piece(Type.pawn, 1, 'Bp', [[1, 0]], black=True)
bKnight = Piece(Type.knight, 3, 'Bk', knightMove, black=True)
bBishop = Piece(Type.bishop, 3.25, 'Bb', bishopMove, black=True)
bRook = Piece(Type.rook, 5, 'Br', rookMove, black=True)
bQueen = Piece(Type.queen, 9, 'BQ', queenMove, black=True)
bKing = Piece(Type.king, 9999, 'BK', kingMove, black=True)

#WHITE
wPawn = Piece(Type.pawn, 1, 'Bp', [[-1, 0]])
wKnight = Piece(Type.knight, 3, 'Bk', knightMove)
wBishop = Piece(Type.bishop, 3.25, 'Bb', bishopMove)
wRook = Piece(Type.rook, 5, 'Br', rookMove)
wQueen = Piece(Type.queen, 9, 'BQ', queenMove)
wKing = Piece(Type.king, 9999, 'BK', kingMove)

class Game(object):
    board = []
    # ['Br', 'Bk', 'Bb', 'BQ', 'BK', 'Bb', 'Bk', 'Br'],
    # ['Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp'],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp'],
    # ['Wr', 'Wk', 'Wb', 'WK', 'WQ', 'Wb', 'Wk', 'Wr']]

    def __init__(self):
        self.board = [
            [bKing, bQueen],
            [bKing, bQueen]]

    def __str__(self):
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        col = ''.join(' '+str(l)+'   ' for l in cols)
        sep = '\n  -----------------------------------------\n'
        b = sep
        # for i in range(2):
        #     b += str(8-i)
        #     for j in range(2):
        #         b += ' | ' + str(self.board[i][j].name.name)
        #     b += ' |' + sep
        b += '   '+col+'\n'

        return b

    # def start():


if __name__ == '__main__':
    print("Game class test")
    b = Game()
    print(b)
    print(b.board[0][0].name.name)
    print(queenMove)

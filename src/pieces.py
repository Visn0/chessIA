from enum import Enum

class Type(Enum):
    king = 1
    queen = 2
    rook = 3
    bishop = 4
    knight = 5 
    pawn = 6

class Piece:
    name = Type.pawn
    value = 0
    icon = '?'
    moves = []
    black = True

    def __init__(self, name, value, icon, moves, black=False,):
        self.name = name
        self.black = black
        self.value = value
        self.icon = icon
        self.moves = moves


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


if __name__ == '__main__':
    print("Piece class test")
    b = Piece(Type.king, 10, '?', [1, 2])
    print('hola')

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


if __name__ == '__main__':
    print("Piece class test")
    b = Piece(Type.king, 10, '?', [1, 2])
    print('hola')

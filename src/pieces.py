class Piece:
    icon = '?'
    moves = []

    def __init__(self, icon, moves):
        self.icon = icon
        self.moves = moves

    
class King(Piece):
    def __init__(self, icon):
        super().__init__(icon, King.getMoves())

    def getMoves():
        a = [1, 2]
        return a

class Queen(Piece):
    def __init__(self, icon):
        super().__init__(icon, Queen.getMoves())

    def getMoves():
        a = [1, 2]
        return a


class Rook(Piece):
    def __init__(self, icon):
        super().__init__(icon, Rook.getMoves())

    def getMoves():
        a = [1, 2]
        return a

class Bishop(Piece):
    def __init__(self, icon):
        super().__init__(icon, Bishop.getMoves())

    def getMoves():
        a = [1, 2]
        return a

class Knight(Piece):
    def __init__(self, icon):
        super().__init__(icon, Knight.getMoves())

    def getMoves():
        a = [1, 2]
        return a

class Pawn(Piece):
    def __init__(self, icon):
        super().__init__(icon, Pawn.getMoves())

    def getMoves():
        a = [1, 2]
        return a

if __name__ == '__main__':
    print("Piece class test")
    b = Piece('?', [1, 2])
    print('hola')
    k = King('>')
    print(k.icon)

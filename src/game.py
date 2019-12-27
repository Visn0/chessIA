from pieces import *


class Game(object):

    bPieces = {}
    wPieces = {}

    # board = {}
    # ['Br', 'Bk', 'Bb', 'BQ', 'BK', 'Bb', 'Bk', 'Br'],
    # ['Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp'],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp'],
    # ['Wr', 'Wk', 'Wb', 'WK', 'WQ', 'Wb', 'Wk', 'Wr']]

    def __init__(self):
        self.bPieces = {
            (0, 0): bRook, (0, 1): bKnight, (0, 2): bBishop, (0, 3): bQueen,
            (0, 4): bKing, (0, 5): bBishop, (0, 6): bKnight, (0, 7): bRook,
            (1, 0): bPawn, (1, 1): bPawn, (1, 2): bPawn, (1, 3): bPawn,
            (1, 4): bPawn, (1, 5): bPawn, (1, 6): bPawn, (1, 7): bPawn
        }

        self.wPieces = {
            (7, 0): wRook, (7, 1): wKnight, (7, 2): wBishop, (7, 3): wKing,
            (7, 4): wQueen, (7, 5): wBishop, (7, 6): wKnight, (7, 7): wRook,
            (6, 0): wPawn, (6, 1): wPawn, (6, 2): wPawn, (6, 3): wPawn,
            (6, 4): wPawn, (6, 5): wPawn, (6, 6): wPawn, (6, 7): wPawn
        }

    def __str__(self):
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        col = ''.join(' '+str(l)+'   ' for l in cols)
        sep = '\n  -----------------------------------------\n'
        b = sep
        for i in range(8):
            b += str(8-i)
            for j in range(8):
                b += ' | '
                if (i, j) in self.bPieces:
                    b += str(self.bPieces[(i, j)].icon)
                elif (i, j) in self.wPieces:
                    b += str(self.wPieces[(i, j)].icon)
                else:
                    b += '  '

            b += ' |' + sep
        b += '   '+col+'\n'

        return b

    def tableToCoord(row, letter):
        r = 8 - row
        c = ord(letter) - ord('a')
        return (r, c)

    def inside(x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False
        return True

    def move(self, from_r, from_c, to_r, to_c, black):
        (from_r, from_c) = Game.tableToCoord(from_r, from_c)
        (to_r, to_c) = Game.tableToCoord(to_r, to_c)

        if not Game.inside(from_r, from_c) or not Game.inside(to_r, to_c):
            print(f'Error, wrong coordinates ({from_r}, {from_c}) -> ({to_r}, {to_c})')
            return False

        if black:
            if (from_r, from_c) in self.bPieces:
                if (to_r, to_c) in self.bPieces:
                    print('Error, you cant kill yourself!')
                    return False
                else:
                    if (to_r, to_c) in self.wPieces:
                        print(f'Killed {self.wPieces[(to_r, to_c)].name.name}')
                        del self.wPieces[(to_r, to_c)]

                    self.bPieces[(to_r, to_c)] = self.bPieces[(from_r, from_c)]
                    del self.bPieces[(from_r, from_c)]
                
            else:
                print(f'Error, doesnt exist black piece on ({from_r}, {from_c})')
                return False
        else:
            if (from_r, from_c) in self.wPieces:
                if (to_r, to_c) in self.wPieces:
                    print('Error, you cant kill yourself!')
                    return False
                else:
                    if (to_r, to_c) in self.bPieces:
                        print(f'Killed {self.bPieces[(to_r, to_c)].name.name}')
                        del self.bPieces[(to_r, to_c)]

                    self.wPieces[(to_r, to_c)] = self.wPieces[(from_r, from_c)]
                    del self.wPieces[(from_r, from_c)]
            else:
                print(f'Error, doesnt exist white piece on ({from_r}, {from_c})')
                return False
        return True

    

if __name__ == '__main__':
    print("Game class test")
    g = Game()
    print(g)
    g.move(7, 'b', 6, 'b', black=True)
    g.move(7, 'b', 6, 'b', black=False)
    print(g)

    g.move(7, 'c', 2, 'c', black=True)
    print(g)

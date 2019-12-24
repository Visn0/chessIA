from pieces import *


class Game(object):
    board = {}
    # ['Br', 'Bk', 'Bb', 'BQ', 'BK', 'Bb', 'Bk', 'Br'],
    # ['Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp'],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    # ['Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp'],
    # ['Wr', 'Wk', 'Wb', 'WK', 'WQ', 'Wb', 'Wk', 'Wr']]

    def __init__(self):
        self.board = {
            (0, 0) : bRook
        }

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
    print(b.board[(0, 0)].name.name)
    print(queenMove)

class Board(object):
    game = [
        ['Br', 'Bk', 'Bb', 'BQ', 'BK', 'Bb', 'Bk', 'Br'],
        ['Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp'],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp'],
        ['Wr', 'Wk', 'Wb', 'WK', 'WQ', 'Wb', 'Wk', 'Wr'],
        

    ]
    #def __init__(self):
     #   print('ok')

    def __str__(self):
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        col = ''.join(' '+str(l)+'   ' for l in cols)
        sep = '\n  -----------------------------------------\n'
        b = sep
        for i in range(8):
            b += str(8-i)
            for j in range(8):
                b += ' | ' + str(self.game[i][j])
            b += ' |' + sep
        b += '   '+col+'\n'
    
        return b


if __name__ == '__main__':
    print("Board class test")
    b = Board()
    print(b)
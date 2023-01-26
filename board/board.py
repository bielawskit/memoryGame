from string import ascii_uppercase as letters


class Board:
    def __init__(self, matrix_x_size, matrix_y_size):
        self.matrix_x_size = matrix_x_size
        self.matrix_y_size = matrix_y_size
        self.letters = list(letters[:self.matrix_x_size])
        self.num = range(self.matrix_y_size)
        self.matrix_size = [['_' for row in range(self.matrix_x_size)] for number in range(self.matrix_y_size)]

    def drawn_board(self):
        print('  ' + ' '.join(self.letters))
        for i in self.num:
            print(i, end=" ")
            print(' '.join(self.matrix_size[i]))


easy_board = Board(4, 2)
hard_board = Board(8, 2)

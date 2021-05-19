def create_blank_board(rows, columns):
    board = []
    for i in range(rows):
        col = []
        for j in range(columns):
            col.append('--')
        board.append(col)
    return board


class Gameboard:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = create_blank_board(rows, columns)
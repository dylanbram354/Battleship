def create_blank_board(rows, columns):
    board = []
    for i in range(rows):
        col = []
        for j in range(columns):
            col.append(0)
        board.append(col)
    return board


class Player:
    def __init__(self):
        self.name = ''
        self.my_board = create_blank_board(20, 20)
        self.opponent_board = create_blank_board(20, 20)

    def place_ships(self):
        # start with ship of x dimension
        # display_my_board
        # ask user to place horizontally or vertically
        # if vertical, ask for coordinates of topmost point. Horizontal, leftmost
        pass

    def attack(self):
        pass

    def display_opponent_board(self):
        pass

    def display_my_board(self):
        pass
from gameboard import Gameboard
from ship import Ship


class Player:
    def __init__(self):
        self.name = ''
        self.my_board = Gameboard(20, 20)
        self.opponent_board = Gameboard(20, 20)
        self.destroyer = Ship('DESTROYER', 2, "D")
        self.submarine = Ship('SUBMARINE', 3, "S")
        self.battleship_1 = Ship('BATTLESHIP 1', 4, "B1")
        self.battleship_2 = Ship('BATTLESHIP 2', 4, "B2")
        self.aircraft_carrier = Ship('AIRCRAFT CARRIER', 5, "A")

    def place_ships(self):
        # start with ship of x dimension
        # display_my_board
        # ask user to place horizontally or vertically
        # if vertical, ask for coordinates of topmost point. Horizontal, leftmost
        # place ship by += 1 to each space. If space value > 1, that means there is overlap, so prompt again
        #
        print(f"Welcome {self.name}! Let's get started. Here is your board: ")
        self.display_my_board()
        print(f'\n"0" represents an empty, un-attacked space. "1" represents ships that have not been hit.'
              f'\n"X" will represent misses, "+" will represent hits.'
              f'\n\nThere are {self.my_board.rows} rows and {self.my_board.columns} columns.'
              f'\nRows are numbered 1-{self.my_board.rows} from left to right, columns are numbered '
              f'1-{self.my_board.columns} top to bottom.')
        print(f"Here are your ships: ")


    def attack(self):
        pass

    def display_opponent_board(self):
        pass

    def display_my_board(self):
        print('')
        for row in self.my_board.board:
            print(row)

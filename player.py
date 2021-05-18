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
        self.fleet = [self.destroyer, self.submarine, self.battleship_1, self.battleship_2, self.aircraft_carrier]

    def place_ships(self):
        print(f"\nWelcome {self.name}! Here is your board:\n")
        for row in self.my_board.board:
            print(row)
        print(f'\n"0" represents an empty, un-attacked space. '
              f'\n"X" will represent hits, "-" will represent misses, and your ships will be marked with '
              f'their respective indicators.'
              f'\n\nThere are {self.my_board.rows} rows and {self.my_board.columns} columns.'
              f'\nRows are numbered 1-{self.my_board.rows} from left to right, columns are numbered '
              f'1-{self.my_board.columns} top to bottom.')
        print(f"\nHere is your fleet: ")
        for ship in self.fleet:
            print(f"\n{ship.name}: takes up {ship.length} spaces. Marked on board by '{ship.placeholder}'.")
        for ship in self.fleet:
            direction = ''
            while direction == '':
                direction = input(f"\nNow placing {self.name}'s {ship.name}. "
                                  f'Would you like to place this ship vertically or horizontally?'
                                  f'\nEnter "vertical" or "horizontal". ').upper()
                if direction == 'HORIZONTAL':
                    row = ''
                    while row == '':
                        try:
                            row = input(f'\nYou chose to place {ship.name} horizontally. '
                                        f'In which row would you like to place your {ship.name} '
                                        f'(1-{self.my_board.rows})? ')
                            row = int(row)
                            if row > self.my_board.rows or row <= 0:
                                row = ''
                                print(f"\nOops! Invalid input. Rows are numbered from 1-{self.my_board.rows}, "
                                      f"top to bottom. Try again...")
                        except ValueError:
                            row = ''
                            print(f"\nOops! Invalid input. Try again...")
                    column = ''
                    while column == '':
                        try:
                            column = input(f"\nYou have chosen to place {ship.name} in row {row}. "
                                           f"Enter the the column number for the LEFTMOST point of {ship.name} "
                                           f"(1-{self.my_board.columns}): ")
                            column = int(column)
                            if column > self.my_board.columns or column <= 0:
                                column = ''
                                print(f"\nOops! Invalid input. Columns are numbered from 1-{self.my_board.columns}, "
                                      f"left to right. Try again...")
                            elif self.my_board.columns - column + 1 < ship.length:
                                column = ''
                                print(f"\nOops! {ship.name} is too long to fit in that spot. Try again!")
                        except ValueError:
                            column = ''
                            print(f"\nOops! Invalid input. Try again...")
                    row -= 1
                    column -= 1
                    row = self.my_board.board[row]
                    i = column
                    while i < column + ship.length:
                        if row[i] == 0:
                            i += 1
                        else:
                            print(f"\nOops! {ship.name} can't be placed there, as it would overlap with another "
                                  f"ship. Try again... ")
                            direction = ''
                            break
                    if direction != '':
                        i = column
                        while i < column + ship.length:
                            row[i] = ship.placeholder
                            i += 1
                        print(f"{ship.name} placed! Here is your board as of now: ")
                        for row in self.my_board.board:
                            print(row)
                elif direction == 'VERTICAL':
                    column = ''
                    while column == '':
                        try:
                            column = input(f'\nYou chose to place {ship.name} vertically. '
                                           f'In which column would you like to place your {ship.name} '
                                           f'(1-{self.my_board.columns})? ')
                            column = int(column)
                            if column > self.my_board.columns or column <= 0:
                                column = ''
                                print(f"\nOops! Invalid input. Columns are numbered from 1-{self.my_board.rows}, "
                                      f"left to right. Try again...")
                        except ValueError:
                            column = ''
                            print(f"\nOops! Invalid input. Try again...")
                    row = ''
                    while row == '':
                        try:
                            row = input(f"\nYou have chosen to place {ship.name} in column {column}. "
                                        f"Enter the the row number for the TOPMOST point of {ship.name} "
                                        f"(1-{self.my_board.rows}): ")
                            row = int(row)
                            if row > self.my_board.rows or row <= 0:
                                row = ''
                                print(f"\nOops! Invalid input. Rows are numbered from 1-{self.my_board.rows}, "
                                      f"top to bottom. Try again...")
                            elif self.my_board.rows - row + 1 < ship.length:
                                row = ''
                                print(f"\nOops! {ship.name} is too long to fit in that spot. Try again!")
                        except ValueError:
                            row = ''
                            print(f"\nOops! Invalid input. Try again...")
                    column -= 1
                    row -= 1
                    i = row
                    while i < row + ship.length:
                        if self.my_board.board[i][column] == 0:
                            i += 1
                        else:
                            print(f"\nOops! {ship.name} can't be placed there, as it would overlap with another "
                                  f"ship. Try again... ")
                            direction = ''
                            break
                    if direction != '':
                        i = row
                        while i < row + ship.length:
                            self.my_board.board[i][column] = ship.placeholder
                            i += 1
                        print(f"\n{ship.name} placed! Here is your board as of now:\n")
                        for row in self.my_board.board:
                            print(row)
                else:
                    direction = ''
                    print(f"\nOops! Invalid input. Try again...")
        print(f"\nSuccess! All ships have been placed!")

    def display_opponent_board(self):
        print('\n"X" is a hit, "-" is a miss.')
        for row in self.opponent_board.board:
            print(row)

    def display_my_board(self):
        print('\n"X" is opponent hit, "-" is opponent miss.')
        for row in self.my_board.board:
            print(row)

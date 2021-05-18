from player import Player


class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()

    def run_game(self):
        self.player_one.place_ships()
        self.attack(self.player_two, self.player_one)

    def attack(self, attacker, defender):
        print(f"\n{attacker.name}'s turn! Here is what you know of {defender.name}'s board: ")
        attacker.display_opponent_board()
        marker = ''
        while marker == '':
            row = ''
            while row == '':
                try:
                    row = input(f"\n{attacker.name}, time to attack! "
                                f"Enter the row number for the space you wish to attack. ")
                    row = int(row)
                    if row > attacker.opponent_board.rows or row < 0:
                        print(f"\nOops! Make sure you enter a valid row number from 1-{attacker.opponent_board.rows}. "
                              f"Try again...")
                except ValueError:
                    print(f"\nOops! Invalid input. Try again...")
            row -= 1
            column = ''
            while column == '':
                try:
                    column = input(f"\nRow {row+1} selected. Enter the column number for the spot you " 
                                   f"wish to attack. ")
                    column = int(column)
                    if column > attacker.opponent_board.columns or column < 0:
                        print(f"\nOops! Make sure you enter a valid column number from 1-{attacker.opponent_board.columns}. "
                              f"Try again...")
                except ValueError:
                    print(f"\nOops! Invalid input. Try again...")
            column -= 1
            if attacker.opponent_board.board[row][column] == 'X' or attacker.opponent_board.board[row][column] == '-':
                print(f"\nOops! You've already attacked that spot. Try again...")
            else:
                marker = 1
        print(f"{attacker.name} launches a missile at {defender.name}'s row {row+1}, column {column+1}...")
        attack_spot = defender.my_board.board[row][column]
        if attack_spot == 0:
            print(f"\nMiss!")
            attacker.opponent_board.board[row][column] = '-'
            defender.my_board.board[row][column] = '-'
        else:
            print(f"\nHIT!")
            attacker.opponent_board.board[row][column] = 'X'
            defender.my_board.board[row][column] = 'X'
        for ship in defender.fleet:
            alive = 'no'
            for row in defender.my_board.board:
                if ship.placeholder in row:
                    alive = 'yes'
            if alive == 'no':
                print(f"\n{attacker.name} sunk {defender.name}'s {ship.name}!")
                defender.fleet.remove(ship)


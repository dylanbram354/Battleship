from player import Player


class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()

    def run_game(self):
        print(f"\nWelcome to BATTLESHIP! "
              f"\n\nEach player will position their fleet around the game board. Players will take turns "
              f"launching missiles (blindly) at their opponent's board."
              f"\nIf an attacker's missile hits an opponent's ship, that space will be marked as a HIT! "
              f"If not, it will be marked as a MISS."
              f"\nOnce all of a ship's spaces have been hit, the ship sinks and is removed from the fleet."
              f"\nThe first player to knock out their opponent's fleet wins the game!")
        user_input = 'yes'
        while user_input == 'yes':
            self.player_one.name = input(f"\n\nPlayer One, please enter your name: ")
            self.player_one.place_ships()
            self.player_two.name = input(f"\n\nPlayer Two, please enter your name: ")
            self.player_two.place_ships()
            while len(self.player_one.fleet) > 0 and len(self.player_two.fleet) > 0:
                self.attack(self.player_one, self.player_two)
                if len(self.player_two.fleet) == 0:
                    print(f"\nGAME OVER! {self.player_two.name}'s fleet depleted!"
                          f"{self.player_one.name} wins!")
                    break
                self.attack(self.player_two, self.player_one)
                if len(self.player_one.fleet) == 0:
                    print(f"\nGAME OVER! {self.player_one.name}'s fleet depleted! "
                          f"{self.player_two.name} wins!")
            user_input = ''
            while user_input == '':
                user_input = input("\nPlay again? (yes/no) ")
                if user_input == 'no':
                    print(f'\nSee you next time!')
                elif user_input != 'yes':
                    print(f"\nInvalid input! Try again...")
                    user_input = ''


    def attack(self, attacker, defender):
        input(f"\nPress 'enter' to continue to {attacker.name}'s turn. "
              f"(No peeking, {defender.name}!)")
        print(f"\n{attacker.name}'s turn! Here is your board: ")
        attacker.display_my_board()
        print(f"\nAnd here is what you know of {defender.name}'s board: ")
        attacker.display_opponent_board()
        marker = ''
        while marker == '':
            row = ''
            while row == '':
                try:
                    row = input(f"\n{attacker.name}, time to attack! "
                                f"Enter the ROW number you wish to attack. ")
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
                    column = input(f"\nRow {row+1} selected. Enter the COLUMN number for the spot you " 
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
                print(f"\n{attacker.name} sunk {defender.name}'s {ship.name}!"
                      f"\nRemaining ships in {defender.name}'s fleet:")
                defender.fleet.remove(ship)
                for ships in defender.fleet:
                    print(ships.name)


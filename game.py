from player import Player
from gameboard import Gameboard
from random import seed
from random import randint
from datetime import datetime


class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
        self.computer_game = False

    def run_game(self):
        print(f"\nWelcome to BATTLESHIP! "
              f"\n\nEach player will position their fleet of five ships around a square game board. "
              f"Players will take turns "
              f"launching missiles (blindly) at their opponent's board."
              f"\nIf an attacker's missile hits an opponent's ship, that space will be marked as a HIT ('XX')! "
              f"If not, it will be marked as a MISS ('00')."
              f"\nOnce all of a ship's spaces have been hit, the ship sinks and is removed from the fleet."
              f"\nThe first player to knock out their opponent's fleet wins the game!")
        user_input = 'yes'
        while user_input == 'yes':
            board_size = ''
            while board_size == '':
                board_size = input(f"\nHow many rows/columns would you like on your game board? "
                                   f"Enter a number from 5-25. ")
                try:
                    board_size = int(board_size)
                    if not (5 <= board_size <= 25):
                        print(f"\nOops! That number is outside the permitted range. Please enter a"
                              f" number from 5-25.")
                        board_size = ''
                except ValueError:
                    print(f"\nOops! Invalid input. Try again...")
                    board_size = ''
            print(f"\nYou have chosen a game board size of {board_size} x {board_size}.")
            self.player_one.my_board = Gameboard(board_size, board_size)
            self.player_one.opponent_board = Gameboard(board_size, board_size)
            self.player_two.my_board = Gameboard(board_size, board_size)
            self.player_two.opponent_board = Gameboard(board_size, board_size)
            self.create_fleets()
            computer_game = ''
            while computer_game == '':
                computer_game = input(
                    f"\nPlay against a computer [Y/N]? ")[0].upper()
                if computer_game == 'Y':
                    self.computer_game = True
                elif computer_game == 'N':
                    self.computer_game = False
                else:
                    print("Invalid selection.")
                    computer_game = ''

            self.player_one.name = input(
                f"\nPlayer One, please enter your name: ")

            if self.computer_game:
                self.player_two.name = "Fred"
            else:
                self.player_two.name = input(
                    f"\nPlayer Two, please enter your name: ")
            self.player_one.place_human_ships()
            pause = input(
                f"\nPress enter to hide your board and continue to {self.player_two.name}'s turn.")
            e = 0
            while e < 30:
                print(f"|")
                e += 1
            print(f"\n(Hiding {self.player_one.name}'s board from {self.player_two.name}) "
                  f"\n{self.player_one.name}, scroll up to view your completed board.")
            pause = input(f"\nPress enter to continue to {self.player_two.name}'s turn. ")

            if self.computer_game:
                self.player_two.place_computer_ships()
                print(f"\n{self.player_two.name}'s ships placed!")
            else:
                self.player_two.place_human_ships()
                pause = input(
                    f"\nPress enter to hide your board and continue to the game.")
            e = 0
            while e < 30:
                print(f"|")
                e += 1
            print(f"\n(Hiding {self.player_two.name}'s board from {self.player_one.name}) "
                  f"\n{self.player_two.name}, scroll up to view your completed board. "
                  f"\n\nLet's start the game!")
            while len(self.player_one.fleet) > 0 and len(self.player_two.fleet) > 0:
                self.attack(self.player_one, self.player_two)
                if len(self.player_two.fleet) == 0:
                    print(f"\nGAME OVER! {self.player_two.name}'s fleet depleted! "
                          f"{self.player_one.name} wins!")
                    break
                if self.computer_game:
                    self.computer_attack(self.player_two, self.player_one)
                else:
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
        pause = input(f"\nPress 'enter' to continue to {attacker.name}'s turn. "
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
                    column = input(f"\nRow {row + 1} selected. Enter the COLUMN number for the spot you "
                                   f"wish to attack. ")
                    column = int(column)
                    if column > attacker.opponent_board.columns or column < 0:
                        print(
                            f"\nOops! Make sure you enter a valid column number from 1-{attacker.opponent_board.columns}. "
                            f"Try again...")
                except ValueError:
                    print(f"\nOops! Invalid input. Try again...")
            column -= 1
            if attacker.opponent_board.board[row][column] == 'XX' or attacker.opponent_board.board[row][column] == '00':
                print(f"\nOops! You've already attacked that spot. Try again...")
            else:
                marker = 1
        e = 0
        while e < 30:
            print(f"|")
            e += 1
        print(f"\n{attacker.name} launches a missile at {defender.name}'s row {row + 1}, column {column + 1}...")
        attack_spot = defender.my_board.board[row][column]
        if attack_spot == '--':
            print(f"\nMiss!")
            attacker.opponent_board.board[row][column] = '00'
            defender.my_board.board[row][column] = '00'
        else:
            print(f"\nHIT!")
            attacker.opponent_board.board[row][column] = 'XX'
            defender.my_board.board[row][column] = 'XX'
        for ship in defender.fleet:
            alive = 'no'
            for row in defender.my_board.board:
                if ship.placeholder in row:
                    alive = 'yes'
            if alive == 'no':
                print(f"\n{attacker.name} sunk {defender.name}'s {ship.name}!")
                defender.fleet.remove(ship)
                if len(defender.fleet) > 0:
                    print(f"\nRemaining ships in {defender.name}'s fleet:")
                    for ships in defender.fleet:
                        print(ships.name)

    def computer_attack(self, attacker, defender):
        seed(datetime.now())
        new_guess = 'invalid'
        while new_guess != 'valid':
            row = randint(0, attacker.opponent_board.rows - 1)
            column = randint(0, attacker.opponent_board.columns - 1)

            potential_spot = attacker.opponent_board.board[row][column]
            if potential_spot == '00':
                continue
            elif potential_spot == 'XX':
                continue

            new_guess = 'valid'
            print(f"\n{attacker.name} launches a missile at {defender.name}'s row {row + 1}, column {column + 1}...")
            attack_spot = defender.my_board.board[row][column]
            if attack_spot == '--':
                print(f"\nMiss!")
                attacker.opponent_board.board[row][column] = '00'
                defender.my_board.board[row][column] = '00'
            else:
                print(f"\nHIT!")
                attacker.opponent_board.board[row][column] = 'XX'
                defender.my_board.board[row][column] = 'XX'
            for ship in defender.fleet:
                alive = 'no'
                for row in defender.my_board.board:
                    if ship.placeholder in row:
                        alive = 'yes'
                if alive == 'no':
                    print(f"\n{attacker.name} sunk {defender.name}'s {ship.name}!")
                    defender.fleet.remove(ship)
                    if len(defender.fleet) > 0:
                        print(f"\nRemaining ships in {defender.name}'s fleet:")
                        for ships in defender.fleet:
                            print(ships.name)

    def create_fleets(self):
        max_fleet = [Player().destroyer, Player().submarine, Player().battleship_1,
                     Player().battleship_2, Player().aircraft_carrier]
        chosen_fleet = []
        amount_of_ships = ''
        while amount_of_ships == '':
            try:
                amount_of_ships = input("\nHow many ships would you like in each player's fleet? "
                                        "Enter a number from 1-5. ")
                amount_of_ships = int(amount_of_ships)
                if not 1 <= amount_of_ships <= 5:
                    print("\nOops! Please enter a number from 1-5. Try again...")
                    amount_of_ships = ''
            except ValueError:
                print("\nOops! Please enter a number from 1-5. Try again...")
                amount_of_ships = ''
        i = 0
        while i < amount_of_ships:
            chosen_fleet.append(max_fleet[i])
            i += 1
        self.player_one.fleet = chosen_fleet.copy()
        self.player_two.fleet = chosen_fleet.copy()
        print(f"\nEach player has been assigned a fleet of {amount_of_ships} ship(s).")

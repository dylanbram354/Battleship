from player import Player
from game import Game

if __name__ == '__main__':
    game = Game()
    p1 = game.player_one
    p2= game.player_two
    # game.run_game()
    game.attack(p1, p2)
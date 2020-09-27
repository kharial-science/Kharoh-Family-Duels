from lib.console import Console
from lib.player import Player

class Game:
    def __init__(self, player_number):
        self.player_number = player_number
        self.player_array = []

        for playerIndex in range(player_number):
            self.player_array.append(Player())

    def launch_game(self):
        """
        Method used to launch a game, will let the players design their characters and then launch the fight
        """
        self.design_characters()

    def design_characters(self):
        """
        Let the players design their character
        """
        for player in self.player_array:
            player.design()
            Console.give_pc_to_next_player()

Game(2).launch_game()

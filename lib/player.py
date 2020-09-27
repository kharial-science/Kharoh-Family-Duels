from lib.console import Console


class Player:
    def __init__(self):
        self.name = None
        self.right_hand_weapon = None
        self.left_hand_weapon = None

    def design(self):
        """
        Ask the user how he wants his character to be
        """
        self.name = Console.hello()

        self.right_hand_weapon = Console.choose_weapon()
        if self.right_hand_weapon.hand_status != 3:
            self.left_hand_weapon = Console.choose_weapon()

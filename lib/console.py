class Console:

    @staticmethod
    def sep():
        """
        Separate different blocks of text
        """
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    @staticmethod
    def give_pc_to_next_player():
        """
        Ask the current player to give the pc to the next player
        """
        Console.sep()
        return input("Merci de donner le clavier au joueur suivant et d'appuyer sur entrée.")

    @staticmethod
    def hello():
        """
        This method will ask the player its character's name
        """
        Console.sep()
        return input("Bonjour et bienvenue dans Kharoh Family Duels, \nje suis Ernuyodatchev le maître du duel de ce jeu, \ncomment t'appelles-tu jeune combattant ? \n\n")


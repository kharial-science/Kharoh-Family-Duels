from lib.weapon import weapon_list


class Console:
    @staticmethod
    def sep():
        """
        Separate different blocks of text
        """
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    @staticmethod
    def column(string, spaces=20):
        """
        Use this function to align text on columns
        """
        return string + (spaces - len(string)) * " "

    @staticmethod
    def give_pc_to_next_player():
        """
        Ask the current player to give the pc to the next player
        """
        Console.sep()
        return input(
            "Merci de donner le clavier au joueur suivant et d'appuyer sur entrée."
        )

    @staticmethod
    def hello():
        """
        This method will ask the player its character's name
        """
        Console.sep()
        return input(
            "Bonjour et bienvenue dans Kharoh Family Duels, \nje suis Ernuyodatchev le maître du duel de ce jeu, \ncomment t'appelles-tu jeune combattant ? \n\n"
        )

    @staticmethod
    def choose_weapon():
        """
        Display the weapon list and let the player choose a weapon / returns the chosen weapon
        """

        Console.sep()

        print(
            "Choisis une arme ci-dessous en renseignant le nombre correspondant : \n" 
            + "(si tu ne choisis qu'une arme à une main, il te sera redemandé d'en sélectionner une autre\n")

        # Display the weapon list
        for i in range(len(weapon_list)):
            weapon = weapon_list[i]
            print(
                str(i + 1)
                + ". "
                + Console.column(weapon.name)
                + Console.column(weapon.get_hand_status_french_name())
                + Console.column(weapon.get_damage_type_french_name())
                + Console.column(str(weapon.damage))
                + "\n"
            )

        answer = input()
        if int(answer) < len(weapon_list):
            return weapon_list[int(answer) - 1]
        Console.choose_weapon()
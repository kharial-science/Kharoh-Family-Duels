class Weapon:
    def __init__(
        self,
        # The name of the weapon
        name,
        # Whether the weapon has to be in the right-hand, left-hand or in both (1 : right, 2 : left, 3 : both)
        hand_status,
        # The type of damage of the weapon (physical, magical, distance)
        weapon_type,
        # The base damage of the weapon
        damage,
    ):

        self.name = name
        self.hand_status = hand_status
        self.weapon_type = weapon_type
        self.damage = damage

    def get_damage_type_french_name(self):
        """
        Returns the damage type in french
        """
        return ["dégâts physiques", "dégâts magiques", "dégâts à distance"][
            ["physical", "magical", "distance"].index(self.weapon_type)
        ]

    def get_hand_status_french_name(self):
        """
        Returns the hand status in french
        """
        return ["main droite", "main gauche", "deux mains"][self.hand_status - 1]


short_sword = Weapon("épée courte", 1, "physical", 20)
long_sword = Weapon("épée longue", 3, "physical", 35)
shield = Weapon("bouclier", 2, "physical", 5)

scepter = Weapon("sceptre", 1, "magical", 25)
wand = Weapon("bâton", 3, "magical", 40)
crystal_ball = Weapon("boule de cristal", 2, "magical", 1)
book = Weapon("livre", 2, "magical", 3)

sling = Weapon("fronde", 2, "distance", 13)
bow = Weapon("arc", 3, "distance", 30)

weapon_list = [
    short_sword,
    long_sword,
    shield,
    scepter,
    wand,
    crystal_ball,
    book,
    sling,
    bow,
]

class Weapon:
    def __init__(self, 

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


short_sword = Weapon("épée courte", 1, "physical", 20)
long_sword = Weapon("épée longue", 3, "physical", 35)
shield = Weapon("bouclier", 2, "physical", 5)

scepter = Weapon("sceptre", 1, "magical", 25)
wand = Weapon("bâton", 3, "magical", 40)
crystal_ball = Weapon("boule de cristal", 2, "magical", 1)
book = Weapon("livre", 2, "magical", 3)

sling = Weapon("fronde", 2, "distance", 13)
bow = Weapon("arc", 3, "distance", 30)




from random import randint
import json
class Weapon(object):

    weapon_names = [
                "Shotgun",
                "Sniper Rifle",
                "Assault Rifle",
                "Long Barrel",
                "Pistol"
    ]

    def __init__(self, name, range, damage):
        self.name = name
        self.range = range
        self.damage = damage

    def weapon_spawn(self):



        name_of_weapon = Weapon.weapon_names[randint(0, len(self.weapon_names)-1)]
        if name_of_weapon == "Shotgun":
            weapon_range = randint(2, 10)
            weapon_damage = randint(22, 59)
        elif name_of_weapon == "Sniper Rifle":
            weapon_range = randint(20, 50)
            weapon_damage = randint(22, 59)
        elif name_of_weapon == "Assault Rifle" or "Long Barrel":
            weapon_range = randint(10, 28)
            weapon_damage = randint(15, 45)
        else:
            weapon_range = randint(5, 15)
            weapon_damage = randint(10, 35)





        item_dict = {
            'weapon_name': name_of_weapon,
            'weapon_range': weapon_range,
            'weapon_damage': weapon_damage,

        }

        with open('items.json', 'w') as f:
            json.dump(item_dict, f)



        print(name_of_weapon)
        print("------------")
        print("Range: ", weapon_range)
        print("Damage: ", weapon_damage)
        print("-------------")


class KeyItem(object):

    key_items = [
            "front door key",
            "garage door opener",
            "straw doll",
    ]

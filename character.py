import sys
from random import randint
import pdb
import pickle

enemies = [
        "Large Spider Ant",
        "Mutated Dog",
        "Zombie",
    ]


class Character(object):
    pass

class Player(Character):

    def __init__(self, name, health,):
        self.name = ''
        self.hp = 0






class Enemy(Character):





    #def __init__(self, name, hp):
        #self.name = name
        #self.hp = hp
        # random encounte moduel that can be used anywhere. Moduel will load and save pickle files to use for player health and enmey health.
    def rand_encounter():
        global enemies
        #randomly roll for enemy health and save it to a pickle file.
        monster = enemies[randint(0, len(enemies)-1)]
        enemy_hp = randint(10, 45)
        pickle.dump(enemy_hp, open("enemyHP.p", 'wb'))
        print("You see a ", monster, " standing before you")
        print("It currently has ", enemy_hp, " health")
        print("What do you do?")

        choice = input("> ")
        # load the pickle file and set it to enemy_hp for use in the while statment
        pickle_in = open("enemyHP.p", 'rb')
        enemy_hp = pickle.load(pickle_in)
        # load the pickle file for playerHealth and set it to player_health for use in the while statment
        pickle_in_2 = open("playerHealth.p", 'rb')
        player_health = pickle.load(pickle_in_2)
        while enemy_hp > 0:
            dmg = randint(1, 29)# insert weapon stats at some point
            enemy_hp = enemy_hp - dmg
            print("You did ", dmg, " damage to the ", monster)
            e_dmg = randint(1, 8)
            player_health = player_health - e_dmg
            print("The ", monster, " attacks for ", e_dmg)
            print("What do you do next?")
            choice = input("> ")
            if enemy_hp <= 0:
                print("You've taken out the ", monster, ". Congratulations")
                # Once the enemy is defeated. save the current amount of health to the pickel file.
                pickle.dump(player_health, open("playerHealth.p", 'wb'))
            elif player_health <= 0:
                return 'death'

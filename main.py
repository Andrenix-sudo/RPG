import sys
import os
import cmd
import time
from random import randint
from textwrap import dedent
import pdb
from character import Enemy
from Items import Weapon
import json
from character import Player
from character import Enemy as Emy
import pickle

screen_width = 100

player_name = ''
player_health = 0
player_inventory = []
key_items = []
enemies = [
    "Large Spider Ant",
    "Mutated Dog",
    "Zombie",
]

class EnemyNames(object):

    enemies = [
        "Large Spider Ant",
        "Mutated Dog",
        "Zombie",
    ]

class Scene(object):
    pass


class Inventory(object):

    def __init__(self):
        pass


    def inventory(self):
        with open('items.json', 'r') as f:
            items = json.load(f)

            print("You currently have:")
            print("A", items['weapon_name'])
            print("It has a range of: ", items['weapon_range'])
            print("and a damage stat of: ", items['weapon_damage'])
            global player_inventory
            player_inventory = items


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map


    def play(self):
        #load the current scene from Map class then run the opening scene function
        current_scene = self.scene_map.opening_scene()
        #load the next scene labelled finished and set it to "last_scene" within Engine
        last_scene = self.scene_map.next_scene('finished')

        #set up the end, the game will not stop until the following while statement comes out true
        while current_scene != last_scene:
            # within the scenes "enter" function there is a next scene that is returned. set that to the value of "next_scene_name"
            next_scene_name = current_scene.enter()
            # set current scene to the value retunred in the above, this should load the next scene
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class TitleScreen(Scene):


    def enter(self):

        print('#################################')
        print("# Welcome to Residence of Evil  #")
        print('             - Play -            ')
        print('             - Help -            ')
        print('             - Quit -            ')
        print('#################################')

        option = input("> ")

        if option.lower() == ("play"):
            print("Please enter your name")
            global player_name
            player_name = input("> ")
            print("I will now roll the dice to determine your starting health.")
            global player_health
            player_health = randint(10,30)
            print("Your starting health is ", player_health)
            pickle.dump(player_health, open("playerHealth.p", 'wb'))
            return 'front_yard' # place holder until ready
        elif option.lower() == ("help"):
            TitleScreen.help_menu('self')
        elif option.lower() == ("quit"):
            sys.exit()




    def help_menu(self):
        print('#################################')
        print("# Welcome to Residence of Evil  #")
        print('#################################')
        print('Type North, South, West, East to move')
        print('Type "shoot" to attack enemies  ')
        print('Type "items" to check your inventory')
        TitleScreen.enter('title_screen_selections')

class Death(Scene):

    def enter(self):
        print("You died fucktard!")
        exit(1)
class FrontYard(Scene):


    def enter(self):
        print(dedent("""
                You currently stand in front of a dilapidated mansion. Lightning strikes in
                distance eluminate the nights sky. The shutters on the windows are closed and the
                front door is currently locked.

                You are currently investigated noise complaints from neighbours. They claim to have
                heard screams from the house.
                """
                ))

        encounter_num = 0
        while encounter_num < 1:
            random_encounter = randint(1, 100)
            encounter_num += 1
            print(random_encounter)
            if random_encounter <= 10:
                Emy.rand_encounter()
                encounter_num += 1
                print(encounter_num)


            # put this in another function

            else:
                print("There are no enemies in sight")
                print("What would you like to do")

        choice = input("> ")
        global player_inventory
        if choice.lower() == 'West' or choice.lower() == 'w':
            return 'side_yard'
        elif choice.lower() == 'North' or choice.lower() == 'n':

            if 'front_door_key' in player_inventory:
                print("You open the door")
                print("_________________________________")
                return 'house_hall'
            else:
                print("The door is currently locked.")

        elif choice.lower() == 'South' or choice.lower() == 's':
            print("Behind you stands a busy street")
            print("You turn to leave, but something draws you back")
            print("You turn back to the house.")
            print("___________________________")
            return 'front_yard'
        elif choice.lower() == "east" or  choice.lower() == 'e':
            global key_items
            print(key_items)
            if 'garage_door_opener' in key_items:
                print("you click the old garage door opening. A slow rumble can he heard as the old doors slowly open")
                print("______________________________")
                return 'garage_door'
            else:
                print("The garage door is locked")
                print("_______________________")
                return 'front_yard'
            print("A large garage door stands in your way.")
            print("It currently appears to be locked.")
            print("_________________________________")
            return 'front_yard'
        #w_pn = Weapon('something', 'another', 'b')
        #weapon = w_pn.weapon_spawn()
        #print(weapon)

        elif choice.lower() == "items":
            item = Inventory()
            item.inventory()
            return 'front_yard'

        elif choice.lower() == 'health':
            global player_health
            print("Your current health is: ", player_health)
            return 'front_yard'

        else:
            print("I do not understand that command")
            return 'front_yard'




class SideYard(Scene):
    def enter(self):
        print(dedent("""
        You walk to the side yard. There grass is largely uncut and and turning brown,
        it looks as if no one has been here for a while.
        """))
        print("From this location you can only travel east back to the front of the house.")
        print("What would you like to do?")

        choice = input("> ")

        if choice.lower() == "search":
            print("What would you like to search?")
            choice = input("> ")
            if choice.lower() == 'grass' or choice.lower() == "the grass":
                global key_items
                key_items.append("garage_door_opener")
                print("you found a dirty garage door opener.")
                return 'side_yard'
            else:
                print("There is nothing here by that name.")

        elif choice.lower() == "east" or choice.lower() == 'e':
            return 'front_yard'
        else:
            print("I do not understand.")


        return 'side_yard'
class Garage(Scene):
    def enter(self):
        print(dedent("""
                Dust falls from the garage door as it opens. Inside you can barely make out the shapes
                of various objects. The occasionaly flash of lighting helps you notice that there are
                some boxes in the back of the garage. If only you had a light to see better.
                """))
        print("What would you like to do?")
        choice = input("> ")
        global key_items

        if choice.lower() == 'turn on lights' or choice.lower() == 'lights':
            print("you reach close to the entrance to find a light switch. ")
            print("The lights flicker as they turn on, illuminating the room.")
            key_items.append("light")

        elif choice.lower() == 'search' and 'light' in key_items == False:
            print(lights)
            print("It's too dark to do that right now")
            print("Maybe if you could find a light switch")
        elif choice.lower() == 'search' and 'light' in key_items == True:
            print("What would you like to search?")
            choice == input("> ")
            if choice.lower() == 'boxes' or choice.lower() == 'the boxes':
                print("You find a rusty key inside one of the mouldy boxes")
                key_items.append("front_door_key")
                print("You take the front door key")
        elif choice.lower() == 'west' or choice.lower() == 'w':
            return 'front_yard'
        else:
            print("I do not understand.")
            return 'garage_door'
        return 'garage_door'


class Backyard(Scene):
    def enter(self):
        pass

class HouseHall(Scene):
    def enter(self):
        pass
class HouseKitchen(Scene):
    def enter(self):
        pass

class HouseDiningRoom(Scene):
    def enter(self):
        pass

class HouseReadingRoom(Scene):
    def enter(self):
        pass

class HouseUpStairsBdrmOne(Scene):
    def enter(self):
        pass

class HouseUpStairsBdrmTwo(Scene):
    def enter(self):
        pass

class HouseUpStairsBthRoom(Scene):
    def enter(self):
        pass

class HouseUpStairsMstrBdrm(Scene):
    def enter(self):
        pass

class Attic(Scene):
    def enter(self):
        pass

class Map(object):

    scenes = {
        'title_screen': TitleScreen(),
        'front_yard': FrontYard(),
        'side_yard': SideYard(),
        'house_hall': HouseHall(),
        'garage_door': Garage(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
a_map = Map("title_screen")
a_game = Engine(a_map)
a_game.play()

import time
import random
import enum
from datetime import datetime

weapons = ["Sword", "Bow"]
cities = ["Rivendell", "Minas Tirith"]
enemies_list = ["Orcs", "Goblins"]

weapon = random.choice(weapons)
city = random.choice(cities)
enemies = random.choice(enemies_list)


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def greeting():
    if datetime.today().hour > 18:
        return ("Evening")
    else:
        return ("Day")
    print(greeting())


def confirmation(message):
    for n in range(len(message)):
        print(message[n])
        time.sleep(1)


def print_pause(message, delay=0):
    print(Color.get_color() + message)
    time.sleep(delay)


def intro():
    print_pause(f"Good {greeting()} Adventurer!")
    print_pause("Welcome to the world of J. R. R. Tolkien")
    print_pause(f"When you are attacked by the {enemies }!")
    print_pause(f"Which mighty weapon will you use? {weapon}")
    print_pause("Will you fight or will you run away?")


def run(arsenal):
    if "Sword" in arsenal:
        print_pause("You managed to flee for the time being")
        print_pause("but now you are surrounded!")
        print_pause(f"The {enemies} you have to stay and fight!")
    else:
        print_pause(f"You arrive in a misterious city {city} "
                    "the people welcomes you!")
        print_pause("You warn the people that you where being chased by orcs")
        print_pause(f"The news is {enemies} are wreaking havoc "
                    "in the this world!")
        print_pause(f"The people of {city} "
                    "decide to forge you the mightiest sword!")
        arsenal.append("Anduril")
    command_center(arsenal)


def fight(arsenal):
    if "Anduril" in arsenal:
        print_pause("You summon army of the dead")
        print_pause(f"The {enemies} are killed by the army of the dead.")
        confirmation("YOU WIN")
    else:
        print_pause(f"You attack! but the {enemies} get "
                    "hit by an arrow to knee and die!!!")
        print_pause("You die a horrible death!")
        confirmation("GAME OVER")


def command_center(arsenal):
    response = input(f"Enter command: \n(1) Fight the {enemies} "
                     "\n(2) Run away\n")
    if response == "1":
        fight(arsenal)
    elif response == "2":
        run(arsenal)
    else:
        print_pause("Please enter a valid response!")
        command_center(arsenal)


def game_restart():
    print_pause("\nWould like to restart your adventure?")
    restart = input("Enter your command:\n(1) yes\n(2) no\n")
    if restart == "1":
        global weapon, city, enemies
        weapon = random.choice(weapons)
        city = random.choice(cities)
        enemies = random.choice(enemies_list)
        print_pause("Starting your adventure in")
        confirmation("321")
        play_adventure()
    elif restart != "2":
        print_pause("Please enter a valid response!\n")
        game_restart()
    else:
        print_pause(f"Okay Good {greeting()} thanks for playing!")
        exit(0)


def play_adventure():
    arsenal = []
    intro()
    command_center(arsenal)
    game_restart()


play_adventure()

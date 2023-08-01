import random, time

# Tried to replicate the way the text appears in RPGs with this, so it's not printed instantly
def print_wbw(text, delay=0.2):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)
    print()

# Classes for the game:

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.alive = True

    def enemy_take_damage(self):
        enemy_choice.health -= player.attack
        if enemy_choice.health == 0:
            enemy_choice.alive = False

    def enemy_attack(self):
        print_wbw(f"{self.name} attacks you!")
        Player.player_take_damage(self.attack)
        print_wbw(f"{self.name} dealt {self.attack} hit points to you!")

class Player:
    def __init__(self, name, health, items, weapon):
        self.name = name
        self.health = health
        self.items = items
        self.weapon = weapon
        self.alive = True

    def player_take_damage(self):
        player.health -= enemy_choice.attack
        if player.health == 0:
            self.alive = False

    def player_attack(self):
        print_wbw(f"You attack using {self.weapon}!")
        enemy_choice.enemy_take_damage()
        print_wbw(f"You have dealt {self.attack} hit points!")

    def select_and_use_item(self):
        print_wbw(f"{self.name}, eat something to heal!:")
        for index, (item, hp) in enumerate(self.items.items(), 1):
            print(f"{index}: {item} - {hp} HP")

        while True:
            try:
                choice = int(input("Enter the number of the item to select it: "))
                if 1 <= choice <= len(self.items):
                    selected_item = list(self.items.keys())[choice - 1]
                    heal_amount = self.items[selected_item]
                    self.health = min(self.health + heal_amount, 100)
                    print(f"{self.name} used {selected_item} and recovered {heal_amount} HP.")
                    break
                else:
                    print("That item doesn't exist, try again please!")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run_away(self):
        funny_phrases = [
            "You tried to run, but you tripped over your own feet. Not your finest moment.",
            "The ground suddenly became too interesting for you to run away.",
            "You had second thoughts about running and decided to stay for the snacks.",
            "You pondered the meaning of life and forgot about running for a moment.",
            "The enemy looked so adorable that you couldn't bear to leave.",
        ]
        print_wbw(random.choice(funny_phrases))

    def actions(self):
        self.attack = food_weapons[self.weapon]
        self.option = ["1. Attack", "2. Special Item", "3. Run"]
        print_wbw("Actions:\n")
        for option in self.option:
            print(option)
        selection = input("What will you do?:\n")
        if selection == "Attack" or selection == "1":
            Player.player_attack(self)
        elif selection == "Special Item" or selection == "2":
            Player.select_and_use_item(self)
        elif selection == "Run" or selection == "3":
            Player.run_away(self)

# General items and behaviour of the game:

enemies = [
    Enemy("Burger Basher", health=80, attack=15),
    Enemy("Pasta Pummeler", health=100, attack=20),
    Enemy("Sushi Smasher", health=70, attack=25),
    Enemy("Taco Terrorizer", health=90, attack=18),
    Enemy("Pizza Punisher", health=85, attack=22)
]

def select_enemy():
    print("Choose an enemy to fight:")
    for index, enemy in enumerate(enemies, 1):
        print(f"{index}. {enemy.name}")

food_items = {
    "Mexico": {
        "Great Taco": 35,
        "Enchilada Pack": 20,
        "Guacamole Potion": 45,
        "Salsa Amulet": 30,
    },
    "Japan": {
        "Sushi Roll": 25,
        "Ramen Noodles": 15,
        "Wasabi Potion": 20,
        "Tempura Memento": 18,
    },
    "Italy": {
        "Pizza Slice": 18,
        "Spaghetti Bowl": 12,
        "Gelato Scoop": 22,
        "Mega Risotto": 28,
    },
    "India": {
        "Curry Plate": 22,
        "Naan Bread": 10,
        "Samosa Chakra": 25,
        "Chutney Dip": 16,
    }
}

food_weapons = {
    "Pizza Cutter Dagger": 35,
    "Sushi Katana": 40,
    "Taco Sword": 30,
    "Baguette Staff": 25,
    "Chili Pepper Bow": 28,
}




print_wbw("Welcome to culinary battles!")

player_name = input("What is your name?: ")
player_health = int(input("What is your age?: ")) * 4

while True:
    player_items = input(f"From what country do you prefer the food \n {[value for value in food_items.keys()]}?:\n").capitalize()
    if player_items in food_items.keys():
        break
    else:
        print("Hmmmm are you sure? Try to pick one of the options again please")

player_items = food_items[player_items]

print_wbw("It's dangerous to go alone, pick a weapon!")

while True:
    player_weapon = int(input(f"What weapon would you like to use? \n {[value for value in enumerate(food_weapons.keys(), 1)]}?:\n"))
    if player_weapon == 1:
        player_weapon = "Pizza Cutter Dagger"
        print_wbw(f"You selected the {player_weapon}! it has {food_weapons[player_weapon]} hit points!")
        break
    elif player_weapon == 2:
        player_weapon = "Sushi Katana"
        print_wbw(f"You selected the {player_weapon}! it has {food_weapons[player_weapon]} hit points!")
        break
    elif player_weapon == 3:
        player_weapon = "Taco Sword"
        print_wbw(f"You selected the {player_weapon}! it has {food_weapons[player_weapon]} hit points!")
        break
    elif player_weapon == 4:
        player_weapon = "Baguette Staff"
        print_wbw(f"You selected the {player_weapon}! it has {food_weapons[player_weapon]} hit points!")
        break
    elif player_weapon == 5:
        player_weapon = "Chili Pepper Bow"
        print_wbw(f"You selected the {player_weapon}! it has {food_weapons[player_weapon]} hit points!")
        break
    else:
        print("Invalid selection, please use the correct number!")

player = Player(player_name, player_health, player_items, player_weapon)
print(f"Alright! We're ready to go, just to confirm, here are the details from your profile:\nName: {player_name}\nHealth: {player_health}\nItems: {player_items}\n")

print_wbw("You encounter some enemies!")

while True:
    print_wbw("Choose an enemy to battle:")
    for index, enemy in enumerate(enemies, 1):
        print_wbw(f"{index}. {enemy.name}")

    try:
        player_choice = int(input("Enter the number of the enemy to battle: "))
        if 1 <= player_choice <= len(enemies):
            enemy_choice = enemies[player_choice - 1]
            print(f"\nYou have chosen to battle {enemy_choice.name}!")
            print(f"{enemy_choice.name} - Health: {enemy_choice.health}, Attack: {enemy_choice.attack}")
            break
        else:
            print("That enemy is not on the list!")
    except ValueError:
        print("Please enter a number :(")

while player.health > 0 and enemy_choice.health > 0:
    player.actions()
    if enemy_choice.alive:
        enemy_choice.enemy_attack()

if player.health > 0 and enemy_choice.health <= 0:
    print_wbw("Congratulations! You defeated the enemy!")
elif enemy_choice.health > 0 and player.health <= 0:
    print_wbw("Oh no! The enemy has defeated you. Better luck next time!")
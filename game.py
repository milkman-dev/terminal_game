import random

food_weapons = {
    "Mexico": {
        "Taco Sword": 35,
        "Enchilada Shield": 20,
        "Guacamole Grenade": 45,
        "Salsa Spear": 30,
    },
    "Japan": {
        "Sushi Katana": 40,
        "Ramen Noodles Nunchaku": 25,
        "Wasabi Shuriken": 35,
        "Tempura Bow": 30,
    },
    "Italy": {
        "Pizza Cutter Dagger": 30,
        "Spaghetti Lasso": 25,
        "Gelato Boomerang": 35,
        "Risotto Rapier": 40,
    },
    "India": {
        "Curry Katar": 35,
        "Naan Shield": 20,
        "Samosa Bomb": 45,
        "Chutney Chakram": 30,
    }
}

class Character:
    def __init__(self, name, health, items):
        self.name = name
        self.health = health
        self.items = items

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

def attack(attacker, defender):
    damage = random.randint(attacker.attack // 2, attacker.attack)
    defender.take_damage(damage)
    print(f"{attacker.name} attacks {defender.name} and deals {damage} damage.")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


print("Welcome to culinary battles!")

player_name = input("What is your name?: ")
player_health = int(input("What is your age?: ")) * 4

while True:
    player_items = input(f"From what country do you prefer the food \n {[value for value in food_weapons.keys()]}?:\n").capitalize()
    if player_items in food_weapons.keys():
        break
    else:
        print("Hmmmm are you sure? Try to pick one of the options again please")

player_items = food_weapons[player_items]

player = Character(player_name, player_health, player_items)
print(f"Alright! We're ready to go, just to confirm, here are the details from your profile:\nName: {player_name}\nHealth: {player_health}\nItems: {player_items}\nThe items have the name of the item and also the dmg they give")

enemies = [
    Enemy("Gooey Glop", health=80, attack=15),
    Enemy("Toxic Tater", health=100, attack=20),
    Enemy("Sugary Slurper", health=70, attack=25)
]

def select_enemy():
    print("Choose an enemy to fight:")
    for index, enemy in enumerate(enemies, 1):
        print(f"{index}. {enemy.name}")

    while True:
        try:
            enemy_choice = int(input("Enter the number of your choice: "))
            if 1 <= enemy_choice <= len(enemies):
                return enemies[enemy_choice - 1]
            else:
                print("That enemy doesn't exist, pick again!")
        except ValueError:
            print("Invalid input. Please enter a number.")


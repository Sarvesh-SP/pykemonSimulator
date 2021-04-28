import random


class Pykemon():
    """A model of generic Pykemon character"""

    def __init__(self, name, element, health, speed):
        """Initialise attributes."""
        self.name = name.title()
        self.element = element
        self.current_heatlth = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True

    def light_attack(self, enemy):
        """A light attack gaurenteed to do minimal damage"""

        damage = random.randint(15, 25)

        # All Pykemon will have list moves = [light, heavy, restore, special]
        print(f"Pykemon {self.name} used {self.moves[0]}.")
        print(f"It dealt {damage} damage.")
        enemy.current_heatlth -= damage

    def heavy_attack(self, enemy):
        """A heavy attack that could deal MASSIVE damage, or no damage at all."""
        damage = random.randint(0, 50)
        print(f"Pykemon {self.name} used {self.moves[1]}.")
        if damage < 10:
            print("The attack missed!!!")
        else:
            print(f"It dealt {damage} damage.")
            enemy.current_heatlth -= damage

    def restore(self):
        """A Healing move that will restore our current health"""
        heal = random.randint(15, 25)
        print(f"Pykemon {self.name} used {self.moves[2]}")
        print(f"It healed {heal} health points.")

        self.current_heatlth += heal

        if self.current_heatlth > self.max_health:
            self.current_heatlth = self.max_health

    def faint():

    def show_stats():


class Fire():


class Water():


class Grass():


class Game():

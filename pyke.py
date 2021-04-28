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

    def heavy_attack():

    def restore():

    def faint():

    def show_stats():


class Fire():


class Water():


class Grass():


class Game():

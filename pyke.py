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

    def faint(self):
        """If you run out of health, you faint..."""
        if self.current_heatlth <= 0:
            self.is_alive = False
            print(f"Pykemon {self.name} has fainted!")
            input("Press Enter to continue.")

    def show_stats(self):
        """Display the current pykemon stats"""
        print(f"\nName: {self.name}")
        print(f"Element Type: {self.element}")
        print(f"Health: {self.current_heatlth} / {self.max_health}")
        print(f"Speed: {self.speed}")


class Fire(Pykemon):
    """A fire based Pykemon that is a child of the Pykemon parent class"""

    def __init__(self, name, element, health, speed):
        """Initialise attributes from the parent Pykemon classs."""
        super().__init__(self, name, element, health, speed)
        moves = ['Scratch', 'Ember', 'Pain Split', 'Fire Blast']

    def special_attack(self, enemy):
        """FIRE BLAST: an elemental fire move. Massive damage to grass type, normal damage to fire type, minimal damage to water type."""
        print(f"Pykemon {self.name} used {self.moves[3].upper()}!")

        if enemy.element == "GRASS":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element = "WATER":
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)

        print(f"It dealt {damage} damage.")
        enemy.current_heatlth -= damage

    def move_info():
        """Display pykemon move info"""
        print(f"\n{self.name} Moves: ")
        print(f"--{self.moves[0]}--")
        print(f"\tAn efficient attack...")
        print("\tGuarnateed to do damage within a range of 15 to 25 damage points.")

        print(f"--{self.moves[1]}--")
        print("\nAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        print(f"--{self.moves[2]}--")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")

        print(f"--{self.moves[3]}--")
        print("\tA powerful FIRE based attack...")
        print("\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon.")


class Water(Pykemon):
    """A Water based Pykemon that is a child of the Pykemon parent class"""

       def __init__(self, name, element, health, speed):
            """Initialise attributes from the parent Pykemon classs."""
            super().__init__(self, name, element, health, speed)
            moves = ['Bite', 'Splash', 'Water Absorb', 'Hydro Cannon']

        def special_attack(self, enemy):
            """HYDRO CANNON: an elemental water move. Massive damage to fire type, normal damage to water type, minimal damage to grass type."""
            print(f"Pykemon {self.name} used {self.moves[3].upper()}!")

            if enemy.element == "FIRE":
                print("It's SUPER effective!")
                damage = random.randint(35, 50)
            elif enemy.element = "GRASS":
                print("It's not very effective...")
                damage = random.randint(5, 10)
            else:
                damage = random.randint(10, 30)

            print(f"It dealt {damage} damage.")
            enemy.current_heatlth -= damage

        def move_info(self):
            """Display pykemon move info"""
            print(f"\n{self.name} Moves: ")
            print(f"--{self.moves[0]}--")
            print(f"\tAn efficient attack...")
            print("\tGuarnateed to do damage within a range of 15 to 25 damage points.")

            print(f"--{self.moves[1]}--")
            print("\nAn risky attack...")
            print(
                "\tCould deal damage up to 50 damage points or as little as 0 damage points.")

            print(f"--{self.moves[2]}--")
            print("\tA restorative move...")
            print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")

            print(f"--{self.moves[3]}--")
            print("\tA powerful WATER based attack...")
            print("\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")


class Grass(Pykemon):
  """A Grass based Pykemon that is a child of the Pykemon parent class"""

    def __init__(self, name, element, health, speed):
        """Initialise attributes from the parent Pykemon classs."""
        super().__init__(self, name, element, health, speed)
        moves = ['Vine Whip', 'Wrap', 'Leech Seed', 'Solar Beam']

    def special_attack(self, enemy):
        """SOLAR BEAM: an elemental grass move. Massive damage to water type, normal damage to grass type, minimal damage to fire type."""
        print(f"Pykemon {self.name} used {self.moves[3].upper()}!")

        if enemy.element == "WATER":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element = "FIRE":
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)

        print(f"It dealt {damage} damage.")
        enemy.current_heatlth -= damage

    def move_info(self):
        """Display pykemon move info"""
        print(f"\n{self.name} Moves: ")
        print(f"--{self.moves[0]}--")
        print(f"\tAn efficient attack...")
        print("\tGuarnateed to do damage within a range of 15 to 25 damage points.")

        print(f"--{self.moves[1]}--")
        print("\nAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        print(f"--{self.moves[2]}--")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")

        print(f"--{self.moves[3]}--")
        print("\tA powerful GRASS based attack...")
        print("\tGuaranteed to deal MASSIVE damage to WATER type Pykemon.")

class Game():

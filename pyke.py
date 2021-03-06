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

    def revive(self):
        self.current_heatlth = self.max_health


class Fire(Pykemon):
    """A fire based Pykemon that is a child of the Pykemon parent class"""

    def __init__(self, name, element, health, speed):
        """Initialise attributes from the parent Pykemon classs."""
        super().__init__(name, element, health, speed)
        self.moves = ['Scratch', 'Ember', 'Pain Split', 'Fire Blast']

    def special_attack(self, enemy):
        """FIRE BLAST: an elemental fire move. Massive damage to grass type, normal damage to fire type, minimal damage to water type."""
        print(f"Pykemon {self.name} used {self.moves[3].upper()}!")

        if enemy.element == "GRASS":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "WATER":
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
        print("\tAn risky attack...")
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
        super().__init__(name, element, health, speed)
        self.moves = ['Bite', 'Splash', 'Water Absorb', 'Hydro Cannon']

    def special_attack(self, enemy):
        """HYDRO CANNON: an elemental water move. Massive damage to fire type, normal damage to water type, minimal damage to grass type."""
        print(f"Pykemon {self.name} used {self.moves[3].upper()}!")

        if enemy.element == "FIRE":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "GRASS":
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
        print("\tAn risky attack...")
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
        super().__init__(name, element, health, speed)
        self.moves = ['Vine Whip', 'Wrap', 'Leech Seed', 'Solar Beam']

    def special_attack(self, enemy):
        """SOLAR BEAM: an elemental grass move. Massive damage to water type, normal damage to grass type, minimal damage to fire type."""
        print(f"Pykemon {self.name} used {self.moves[3].upper()}!")

        if enemy.element == "WATER":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "FIRE":
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
        print("\tAn risky attack...")
        print(
            "\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        print(f"--{self.moves[2]}--")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")

        print(f"--{self.moves[3]}--")
        print("\tA powerful GRASS based attack...")
        print("\tGuaranteed to deal MASSIVE damage to WATER type Pykemon.")


class Game():
    """A game object to controll the createion and flow of pykemon and simulater battle!"""

    def __init__(self):
        """Initialize attributes"""
        self.pykemon_elements = ['FIRE', 'WATER', 'GRASS']
        self.pykemon_names = ['Poopachu', 'Bulmasaur', 'Squirty', 'Burnmander', 'Chewdie', 'Muttle',
                              'Zantbat', 'Wiggly Poof', 'Sweetil', 'Jampot', 'Hownstooth', 'Swagilybo', 'Muttle', 'Pyonx']
        self.battles_won = 0
        self.move = 0

    def create_pykemon(self):
        """Randomly generate a Pykemon"""
        health = random.randint(70, 100)
        speed = random.randint(1, 10)

        element = self.pykemon_elements[random.randint(
            0, len(self.pykemon_elements) - 1)]
        name = self.pykemon_names[random.randint(
            0, len(self.pykemon_names) - 1)]

        if element == 'FIRE':
            pykemon = Fire(name, element, health, speed)
        elif element == 'WATER':
            pykemon = Water(name, element, health, speed)
        else:
            pykemon = Grass(name, element, health, speed)
        return pykemon

    def choose_pykemon(self):
        """A meathod to simulate choosing a starting Pykemon similar to Pokemon"""
        starters = []

        while len(starters) < 3:
            pykemon = self.create_pykemon()
            valid_pykemon = True

            for starter in starters:
                if starter.name == pykemon.name or starter.element == pykemon.element:
                    valid_pykemon = False
            if valid_pykemon:
                starters.append(pykemon)
        for pykemon in starters:
            pykemon.show_stats()
            pykemon.move_info()

        print("\nProfessor Teak presents you with three Pykemon:")
        print(f"(1) - {starters[0].name}")
        print(f"(2) - {starters[1].name}")
        print(f"(3) - {starters[2].name}")
        choice = int(input("Which Pykemon would like to choose: "))

        pykemon = starters[choice - 1]

        return pykemon

    def get_attack(self, pykemon):
        """Get a users attack choice."""
        print("\nWhat would you like to do...")
        print(f"(1) - {pykemon.moves[0]}")
        print(f"(2) - {pykemon.moves[1]}")
        print(f"(3) - {pykemon.moves[2]}")
        print(f"(4) - {pykemon.moves[3]}")
        choice = int(input("Please enter your move choice: "))

        print()
        print("---------------------------------------------------------------------------------------------------------------------------")

        return choice

    def player_attack(self, move, player, computer):
        """Attack the computer AI"""
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)

        computer.faint()

    def computer_attack(self, player, computer):
        """Let the computer AI attack the player."""
        move = random.randint(1, 4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)

        player.faint()

    def battle(self, player, computer):
        """Simulate a battle round. Faster Pykemon go first."""
        move = self.get_attack(player)
        if player.speed >= computer.speed:
            self.player_attack(move, player, computer)
            if computer.is_alive:
                self.computer_attack(player, computer)
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)


print("Welcome to Pykemon!")
print("Can you become the worlds greatest Pykemon Trainer???")
print("\nDon't worry! Prof Teak is here to help you on your quest.")
print("Here are three potential Pykemon partners.")
input("Press Enter to choose you Pykemon")

playing_main = True
while playing_main:
    game = Game()

    player = game.choose_pykemon()
    print(f"\nCongratulations Trainer, you have chosen {player.name}")
    input(f"\nYour journey with {player.name} begins now...Press Enter!")

    while player.is_alive:
        computer = game.create_pykemon()
        print(f"\nOH NO! A wild {computer.name} has approached!")
        computer.show_stats()

        while computer.is_alive and player.is_alive:
            game.battle(player, computer)

            if computer.is_alive and player.is_alive:
                player.show_stats()
                computer.show_stats()

                print("-------------------------------------------------------------------------------------------------------------------------------------")
        if player.is_alive:
            game.battles_won += 1
            player.revive()

    print(f"\nPoor {player.name} has fainted...")
    print(f"but not before defeating {game.battles_won} Pykemon!")

    choice = input("Would you like to play again (y/n): ").lower()

    if choice != 'y':
        playing_main = False
        print("Thank you for playing Pykemon!")

import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = random.randint(0, 100)
        self.speed = random.randint(0, 10)
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(f"Ninja's health: {ninja.health}")
        return self


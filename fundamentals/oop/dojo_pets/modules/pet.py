class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

        self.energy = 50
        self.health = 100

    def sleep(self):
        self.energy += 25

        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        
        return self

    def play(self):
        self.health += 5

        return self

    def noise(self):
        print('Pet makes a sound')

        return self

    def display_pet_info(self):
        print(f'\n{self.name}')
        print('-' * 20)
        print(f'Type: {self.type}')
        print(f'Tricks: {self.tricks}')
        print(f'Energy: {self.energy}')
        print(f'Health: {self.health}')
        print()

        return self

class Dog(Pet):

    def __init__(self, name, tricks):
        super().__init__(name, "Dog", tricks)

    def noise(self):
        print('Woof')


class Bird(Pet):

    def __init__(self, name, tricks):
        super().__init__(name, 'bird', tricks)

    def noise(self):
        print('Tweet')
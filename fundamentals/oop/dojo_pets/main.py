from modules.ninja import Ninja
from modules.pet import Pet, Dog, Bird
# from modules.dog import Dog
# from modules.bird import Bird

if __name__ == '__main__':
    cat = Pet('Miko', 'cat', ['beg', 'jump', 'chase'])
    ninja1 = Ninja('Joe', 'K', 'catnip', 'cat food', cat)


    ninja1.walk().feed().bathe()
    cat.display_pet_info()

    dog = Dog('Roger', ['fetch', 'rollover', 'sit'])
    dog.display_pet_info()

    bird = Bird('Carrot', ['peck', 'land on arm', 'eat out of hand'])
    bird.display_pet_info()